from dialog import QT_source
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
import cv2
import numpy as np
from  FasterRCNN_network_files import FasterRCNN,FastRCNNPredictor,AnchorsGenerator
from backbone import resnet50_fpn_backbone
from api import depth_completion_api
from api import utils as depth_api_utils
import torch

from utils import draw_box_utils,data_convert
from torchvision import transforms
import  time
import json
import yaml
import attrdict
from openni import openni2
COLORMAP = cv2.COLORMAP_TWILIGHT_SHIFTED
###加载depth_completion_config###
DEPTH_CONFIG_FILE_PATH = '/home/zzq/Desktop/QT_upper_/eval_depth_completion/config/config.yaml.sample'
print(torch.cuda.is_available())
###加载类别信息###
label_json_path = 'dateset_classes.json'
with open(label_json_path, 'r') as f:
    class_dict = json.load(f)
category_index = {str(v): str(k) for k, v in class_dict.items()}
file_sort=29

###计时函数###
def time_synchronized():
    torch.cuda.synchronize() if torch.cuda.is_available() else None
    return time.time()
###创建RCNN网络 ###
def create_RCNN_model(num_classes):
    backbone = resnet50_fpn_backbone(norm_layer=torch.nn.BatchNorm2d,
                                     trainable_layers=3)
    model = FasterRCNN(backbone=backbone, num_classes=91)
    weights_dict = torch.load("./backbone/fasterrcnn_resnet50_fpn_coco.pth", map_location='cpu')
    missing_keys, unexpected_keys = model.load_state_dict(weights_dict, strict=False)
    if len(missing_keys) != 0 or len(unexpected_keys) != 0:
        print("missing_keys: ", missing_keys)
        print("unexpected_keys: ", unexpected_keys)
    # get number of input features for the classifier
    in_features = model.roi_heads.box_predictor.cls_score.in_features
    # replace the pre-trained head with a new one
    model.roi_heads.box_predictor = FastRCNNPredictor(in_features, num_classes)
    return model

###Ui界面继承类###
class My_transparent_Ui(QMainWindow,QT_source.Ui_MainWindow):
    def __init__(self, parent=None):
        super(My_transparent_Ui, self).__init__(parent)
        self.setupUi(self)
        self.background()
        self.img_arr=None
        self.depth_arr=None
        self.img_Pix=None
        self.CAM_NUM=-1
        self.cap_RGB = cv2.VideoCapture()

        ###深度相机loading
        openni2.initialize()
        Astra_dev = openni2.Device.open_any()
        print(Astra_dev.get_device_info())
        self.Astra_depth_stream = Astra_dev.create_depth_stream()
        self.Astra_depth_stream.start()
        self.Astra_color_stream = Astra_dev.create_color_stream()
        self.Astra_color_stream.start()

        ###RCNN loading
        self.device = torch.device('cuda:0' if torch.cuda.is_available() else "cpu")
        self.model_RCNN=create_RCNN_model(num_classes=5)
        checkpoint_Rcnn=torch.load('save_whight/best_r50_fpn.pth')
        model_weights_dict = checkpoint_Rcnn["model"] if "model" in checkpoint_Rcnn else checkpoint_Rcnn
        self.model_RCNN.load_state_dict(model_weights_dict,strict=False)
        self.model_RCNN.to(self.device)
        self.model_RCNN.eval()
        self.data_transform = transforms.Compose([transforms.ToTensor()])
        with open(DEPTH_CONFIG_FILE_PATH) as fd:
            config_yaml = yaml.safe_load(fd)
        self.config_depth2depth = attrdict.AttrDict(config_yaml)
        outputImgHeight = int(self.config_depth2depth.depth2depth.yres)
        outputImgWidth = int(self.config_depth2depth.depth2depth.xres)
        self.depthcomplete = depth_completion_api.DepthToDepthCompletion(
            normalsWeightsFile=self.config_depth2depth.normals.pathWeightsFile,
            outlinesWeightsFile=self.config_depth2depth.outlines.pathWeightsFile,
            masksWeightsFile=self.config_depth2depth.masks.pathWeightsFile,
            normalsModel=self.config_depth2depth.normals.model,
            outlinesModel=self.config_depth2depth.outlines.model,
            masksModel=self.config_depth2depth.masks.model,
            depth2depthExecutable=self.config_depth2depth.depth2depth.pathExecutable,
            outputImgHeight=outputImgHeight,
            outputImgWidth=outputImgWidth,
            fx=int(self.config_depth2depth.depth2depth.fx),
            fy=int(self.config_depth2depth.depth2depth.fy),
            cx=int(self.config_depth2depth.depth2depth.cx),
            cy=int(self.config_depth2depth.depth2depth.cy),
            filter_d=self.config_depth2depth.outputDepthFilter.d,
            filter_sigmaColor=self.config_depth2depth.outputDepthFilter.sigmaColor,
            filter_sigmaSpace=self.config_depth2depth.outputDepthFilter.sigmaSpace,
            maskinferenceHeight=self.config_depth2depth.masks.inferenceHeight,
            maskinferenceWidth=self.config_depth2depth.masks.inferenceWidth,
            normalsInferenceHeight=self.config_depth2depth.normals.inferenceHeight,
            normalsInferenceWidth=self.config_depth2depth.normals.inferenceWidth,
            outlinesInferenceHeight=self.config_depth2depth.normals.inferenceHeight,
            outlinesInferenceWidth=self.config_depth2depth.normals.inferenceWidth,
            min_depth=self.config_depth2depth.depthVisualization.minDepth,
            max_depth=self.config_depth2depth.depthVisualization.maxDepth,
            tmp_dir=None)

    def background(self):
        self.init_timer()
        self.imageButton.clicked.connect(self.open_image)
        self.depthButton.clicked.connect(self.open_depth)
        self.RunButton_2.clicked.connect(self.image_detect)
        self.RunButton.clicked.connect(self.depth_complition)
        self.resetButton.clicked.connect(self.Reset_sys)
        self.camButton.clicked.connect(self.open_rgb_camera)
        self.DepthcamButton.clicked.connect(self.open_rgbd_camera)
        self.saveButton.clicked.connect(self.save_cam_source_RGB)
        self.setWindowTitle("透明物体识别和深度补全系统")
        self.setWindowIcon(QIcon('/home/zzq/Desktop/QT_upper_/dialog/icon/文件title.png'))
    def open_image(self):
        self.image = None
        self.label_rgb_out.clear()
        # 获取图像的路径
        # self.reset_sys()
        self.img_path = QFileDialog.getOpenFileName()[0]
        img_type = [".bmp", ".jpg", ".png", ".gif"]
        for ig in img_type:
            if ig not in self.img_path:
                continue
            else:
                self.image = True
                img = QPixmap(self.img_path)
                w = img.width()
                h = img.height()
                #读取图片
                self.img_Pix = img.toImage()
                self.img_arr = data_convert.PixToArray(self.img_Pix)
                ratio = max(w / self.label_rgb_in.width(), h / self.label_rgb_in.height())
                img.setDevicePixelRatio(ratio)
                self.label_rgb_in.setScaledContents(True)
                self.label_rgb_in.setAlignment(Qt.AlignCenter)
                self.label_rgb_in.setPixmap(img)
                self.label_depth_in.setScaledContents(True)
        if self.image is None:
            QMessageBox.information(self, "warning", "We don't support image files in this format！", QMessageBox.Ok)
    def open_depth(self):
        self.depth=None
        depth_path = QFileDialog.getOpenFileName()[0]
        depth_type = [".raw", ".exr"]
        for ig in depth_type:
            if ig not in depth_path:
                continue
            else:
                self.depth_arr=depth_api_utils.exr_loader(depth_path,ndim=1)
                depth_rgb=depth_api_utils.depth2rgb(self.depth_arr,min_depth=0.0, max_depth=3.0,
                                                        color_mode=COLORMAP,reverse_scale=False,
                                                        dynamic_scaling=True)
                depth_pix=data_convert.ArrayToPixmap(depth_rgb)
                w = depth_pix.width()
                h = depth_pix.height()
                ratio = max(w / self.label_depth_in.width(), h / self.label_depth_in.height())
                depth_pix.setDevicePixelRatio(ratio)
                self.label_depth_in.setPixmap(depth_pix)
                self.label_depth_in.setAlignment(Qt.AlignCenter)
                self.label_depth_in.setScaledContents(True)
                self.depth = True
        if self.depth is None:
            QMessageBox.information(self, "warning", "We don't  support depth image files in this format！", QMessageBox.Ok)
    def Reset_sys(self):
        self.img_arr=None
        self.depth_arr=None
        self.label_rgb_in.clear()
        self.label_rgb_out.clear()
        self.label_depth_in.clear()
        self.label_depth_out.clear()
        self.camButton.setEnabled(True)
        self.DepthcamButton.setEnabled(True)
        self.listWidget.clear()
        self.timer.stop()
        self.timer_rgbd.stop()
        self.label_outline_out.clear()
        self.label_surf_out.clear()
        #QMessageBox.information(self, "Reset", "Reset successful!", QMessageBox.Ok)
    def image_detect(self):
        # img = cv2.resize(img_orginal, self.imgsz)
        self.listWidget.clear()
        if self.img_arr is None:
            QMessageBox.information(self, "warning", " image wasn't entered！", QMessageBox.Ok)
            return
        img=self.img_arr
        img = self.data_transform(img)
        img = torch.unsqueeze(img, dim=0)
        t_start = time_synchronized()
        predictions = self.model_RCNN(img.to(self.device))[0]
        t_end = time_synchronized()
        print("Detect time: {}".format(t_end - t_start))
        predict_boxes = predictions["boxes"].to("cpu").detach().numpy()
        predict_classes = predictions["labels"].to("cpu").detach().numpy()
        predict_scores = predictions["scores"].to("cpu").detach().numpy()


        if len(predict_boxes) == 0:
            print("没有检测到任何目标!")
        from PIL import Image
        img_plot_box=data_convert.QpixmapToPIL(self.img_Pix)
        # self.img_plot_box=Image.fromarray(self.img_arr)
        plot_img,static_class_dic = draw_box_utils.draw_objs(img_plot_box,
                                     predict_boxes,
                                     predict_classes,
                                     predict_scores,
                                     category_index=category_index,
                                     box_thresh=0.5,
                                     line_thickness=3,
                                     font_size=30)
        QImage_plot_img=data_convert.PILToQImage(plot_img)
        w = QImage_plot_img.width()
        h = QImage_plot_img.height()
        ratio = max(w / self.label_depth_in.width(), h / self.label_depth_in.height())
        QImage_plot_img.setDevicePixelRatio(ratio)
        self.label_rgb_out.setPixmap(QImage_plot_img)
        self.label_rgb_out.setAlignment(Qt.AlignCenter)
        self.label_rgb_out.setScaledContents(True)
        for key,value in static_class_dic.items():
            if(value!=0):
                self.listWidget.addItem(key+":"+str(value))
    def depth_complition(self):
        if self.depth_arr is None or self.img_arr is None:
            QMessageBox.information(self,"warning","RGB or Depth is not entered!",QMessageBox.Ok)
            return
        try :
            t_start = time_synchronized()
            output_depth, filtered_output_depth,surface_normals_rgb,outlines_rgb = self.depthcomplete.depth_completion(
                self.img_arr,
                self.depth_arr,
                inertia_weight=float(self.config_depth2depth.depth2depth.inertia_weight),
                smoothness_weight=float(self.config_depth2depth.depth2depth.smoothness_weight),
                tangent_weight=float(self.config_depth2depth.depth2depth.tangent_weight),
                mode_modify_input_depth=self.config_depth2depth.modifyInputDepth.mode,
                dilate_mask=True
            )
            # seg_mask = np.full((outputImgHeight, outputImgWidth), True, dtype=float)
            out_depth_rgb = depth_api_utils.depth2rgb(output_depth, min_depth=0.0, max_depth=3.0,
                                                  color_mode=COLORMAP, reverse_scale=False,
                                                  dynamic_scaling=True)
            out_depth_pix = data_convert.ArrayToPixmap(out_depth_rgb)

            ###输出depth ###
            w = out_depth_pix.width()
            h = out_depth_pix.height()
            ratio = max(w / self.label_depth_out.width(), h / self.label_depth_out.height())
            out_depth_pix.setDevicePixelRatio(ratio)
            self.label_depth_out.setPixmap(out_depth_pix)
            self.label_depth_out.setAlignment(Qt.AlignCenter)
            self.label_depth_out.setScaledContents(True)

            ###输出表面法线###
            out_normals_pix=data_convert.ArrayToPixmap(surface_normals_rgb)
            w_1=out_normals_pix.width()
            h_1=out_normals_pix.height()
            ratio_1=max(w_1 / self.label_surf_out.width(), h_1 / self.label_surf_out.height())
            out_normals_pix.setDevicePixelRatio(ratio_1)
            self.label_surf_out.setPixmap(out_normals_pix)
            self.label_surf_out.setAlignment(Qt.AlignCenter)
            self.label_surf_out.setScaledContents(True)


            ###输出边界轮廓###
            out_outlines_pix = data_convert.ArrayToPixmap(outlines_rgb)
            w_2=out_outlines_pix.width()
            h_2=out_outlines_pix.height()
            ratio_2=max(w_2 / self.label_outline_out.width(), h_2 / self.label_outline_out.height())
            out_outlines_pix.setDevicePixelRatio(ratio_2)
            self.label_outline_out.setPixmap(out_outlines_pix)
            self.label_outline_out.setAlignment(Qt.AlignCenter)
            self.label_outline_out.setScaledContents(True)
            self.depth = True
            t_end = time_synchronized()
            print("complition time: {}".format(t_end - t_start))
        except depth_completion_api.DepthCompletionError as e:
            QMessageBox.informatioeln( self,"warning", "complete ERROR!", QMessageBox.Ok)
    #摄像头定时器函数
    def show_cam_source(self):
        ret,self.img_arr =self.cap_RGB.read()
        self.img_Pix=data_convert.ArrayToPixmap(self.img_arr)
        self.listWidget.clear()
        start_time = time.time()
        if ret:
            #展示图片
            fps = int(30 / (time.time() - start_time))
            w=self.img_Pix.width()
            h=self.img_Pix.height()
            ratio = max(w / self.label_rgb_in.width(), h / self.label_rgb_in.height())
            self.img_Pix.setDevicePixelRatio(ratio)
            self.label_rgb_in.setScaledContents(True)
            self.label_rgb_in.setAlignment(Qt.AlignCenter)
            self.label_rgb_in.setPixmap(self.img_Pix)
            self.label_depth_in.setScaledContents(True)
            # self.camera_detect(self.img_arr)
    def open_rgb_camera(self):
        index = 0
        self.CAM_NUM = index
        self.Reset_sys()
        flag = self.cap_RGB.open(self.CAM_NUM)
        if flag is False:
            QMessageBox.information(self, "warning", "The camera can't connectted", QMessageBox.Ok)
        else :
            self.label_rgb_in.setEnabled(True)
            self.camButton.setEnabled(False)
            self.timer.start()
            self.timer.blockSignals(False)
    def init_timer(self):
        self.timer = QTimer(self)
        self.timer_rgbd=QTimer(self)
        self.timer.timeout.connect(self.show_cam_source)
        self.timer_rgbd.timeout.connect(self.show_rgbd_cam_source)

    def show_rgbd_cam_source(self):
        frame_dep = self.Astra_depth_stream.read_frame()
        dframe_data= np.array(frame_dep.get_buffer_as_triplet()).reshape([480, 640, 2])
        dpt1 = np.asarray(dframe_data[:, :, 0], dtype='uint16')
        dpt2 = np.asarray(dframe_data[:, :, 1], dtype='uint16')
        dpt2 *= 255

        dpt = dpt1 + dpt2
        if np.all(dpt == 0):
            return
        self.depth_arr = dpt[:, ::-1]/1000
        self.depth_arr=self.depth_arr.astype(np.float32)
        depth_rgb = depth_api_utils.depth2rgb(self.depth_arr, min_depth=0.0, max_depth=4.0,
                                              color_mode=COLORMAP, reverse_scale=False,
                                              dynamic_scaling=True)
        depth_pix = data_convert.ArrayToPixmap(depth_rgb)
        w = depth_pix.width()
        h = depth_pix.height()
        ratio = max(w / self.label_depth_in.width(), h / self.label_depth_in.height())
        depth_pix.setDevicePixelRatio(ratio)
        self.label_depth_in.setPixmap(depth_pix)
        self.label_depth_in.setAlignment(Qt.AlignCenter)
        self.label_depth_in.setScaledContents(True)
        cframe = self.Astra_color_stream.read_frame()
        cframe_data = np.array(cframe.get_buffer_as_triplet()).reshape([480, 640, 3])
        R = cframe_data[:, :, 0]
        G = cframe_data[:, :, 1]
        B = cframe_data[:, :, 2]
        self.img_arr = np.transpose(np.array([B, G, R]), [1, 2, 0])
        self.img_arr = cv2.flip(self.img_arr,1)
        self.img_Pix = data_convert.ArrayToPixmap(self.img_arr)
        w = self.img_Pix.width()
        h = self.img_Pix.height()
        ratio = max(w / self.label_rgb_in.width(), h / self.label_rgb_in.height())
        self.img_Pix.setDevicePixelRatio(ratio)
        self.label_rgb_in.setScaledContents(True)
        self.label_rgb_in.setAlignment(Qt.AlignCenter)
        self.label_rgb_in.setPixmap(self.img_Pix)
        self.label_depth_in.setScaledContents(True)

    def save_cam_source_RGB(self):
        global file_sort
        if self.img_arr is None:
            QMessageBox.information(self, "warning", " image wasn't entered！", QMessageBox.Ok)
            return
        cv2.imwrite(f'/home/zzq/Desktop/QT_upper_/detect_dateset_get/{file_sort}.png',self.img_arr)
        file_sort+=1
    def open_rgbd_camera(self):
        self.Reset_sys()
        self.label_rgb_in.setEnabled(True)
        self.timer_rgbd.start()
        # self.camButton.setEnabled(False)
        self.DepthcamButton.setEnabled(False)

        # im_color = cv2.applyColorMap(cv2.convertScaleAbs(dpt, alpha=0.03), cv2.COLORMAP_JET)
    # def camera_detect(self,img_original:np.array):
    #     if img_original is None:
    #         QMessageBox.information(self, "警告", "未输入图像信息！", QMessageBox.Ok)
    #         return
    #     img = self.data_transform(img_original)
    #     img = torch.unsqueeze(img, dim=0)
    #     predictions = self.model_RCNN(img.to(self.device))[0]
    #     predict_boxes = predictions["boxes"].to("cpu").detach().numpy()
    #     predict_classes = predictions["labels"].to("cpu").detach().numpy()
    #     predict_scores = predictions["scores"].to("cpu").detach().numpy()
    #     if len(predict_boxes) == 0:
    #         print("没有检测到任何目标!")
    #     from PIL import Image
    #     img_plot_box = Image.fromarray(img_original)
    #     plot_img,static_class_dic = draw_box_utils.draw_objs(img_plot_box,
    #                                  predict_boxes,
    #                                  predict_classes,
    #                                  predict_scores,
    #                                  category_index=category_index,
    #                                  box_thresh=0.7,
    #                                  line_thickness=3,
    #                                  font_size=30)
    #     QImage_plot_img=data_convert.PILToQImage(plot_img)
    #     w = QImage_plot_img.width()
    #     h = QImage_plot_img.height()
    #     ratio = max(w / self.label_depth_in.width(), h / self.label_depth_in.height())
    #     QImage_plot_img.setDevicePixelRatio(ratio)
    #     self.label_rgb_out.setPixmap(QImage_plot_img)
    #     self.label_rgb_out.setAlignment(Qt.AlignCenter)
    #     self.label_rgb_out.setScaledContents(True)
    #     for key,value in static_class_dic.items():
    #         if(value!=0):
    #             self.listWidget.addItem(key+":"+str(value))
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow=My_transparent_Ui()
    mainWindow.show()
    sys.exit(app.exec_())

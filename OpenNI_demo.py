from openni import openni2
import numpy as np
import cv2
def depth2mi(depthValue):
    return depthValue * 0.001
def depth2xyz(u, v, depthValue):
    fx = 577.54679
    fy = 578.63325
    cx = 310.24326
    cy = 253.65539

    # depth = depth2mi(depthValue)
    depth = depthValue * 0.001

    z = float(depth)
    x = float((u - cx) * z) / fx
    y = float((v - cy) * z) / fy

    result = [x, y, z]
    return result

def mousecallback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print(y,x,dpt[y,x])
        arr = np.array(dpt)
        depthValue =float(arr[y, x])
        coordinate = depth2xyz(x, y, depthValue)
        print("coordinate:", coordinate)
if __name__ == "__main__":
    openni2.initialize()
    dev = openni2.Device.open_any()
    print(dev.get_device_info())
    depth_stream = dev.create_depth_stream()
    depth_stream.start()
    color_stream = dev.create_color_stream()
    color_stream.start()
    cv2.namedWindow('depth')
    cv2.setMouseCallback('depth', mousecallback)
    while True:
        frame_dep = depth_stream.read_frame()
        dframe_data = np.array(frame_dep.get_buffer_as_triplet()).reshape([480, 640, 2])
        dpt1 = np.asarray(dframe_data[:, :, 0], dtype='uint16')
        dpt2 = np.asarray(dframe_data[:, :, 1], dtype='uint16')
        dpt2 *= 255
        dpt = dpt1 + dpt2
        dpt = dpt[:, ::-1]
        im_color = cv2.applyColorMap(cv2.convertScaleAbs(dpt, alpha=0.03), cv2.COLORMAP_JET)
        cv2.imshow('depth', im_color)

        cframe = color_stream.read_frame()
        cframe_data = np.array(cframe.get_buffer_as_triplet()).reshape([480, 640, 3])
        R = cframe_data[:, :, 0]
        G = cframe_data[:, :, 1]
        B = cframe_data[:, :, 2]
        cframe_data = np.transpose(np.array([B, G, R]), [1, 2, 0])
        # print(cframe_data.shape)
        cv2.imshow('color', cframe_data)
        key = cv2.waitKey(1)
        if int(key) == ord('q'):
            break
    depth_stream.stop()
    dev.close()
# openni2.initialize()  # can also accept the path of the OpenNI redistribution
#
# dev = openni2.Device.open_any()
# print(dev.get_device_info())
# depth_stream = dev.create_depth_stream()
# color_stream = dev.create_color_stream()
# depth_stream.start()
# color_stream.start()
#
# while True:
#
#     # 显示深度图
#     frame = depth_stream.read_frame()
#     dframe_data = np.array(frame.get_buffer_as_triplet()).reshape([480, 640, 2])
#     dpt1 = np.asarray(dframe_data[:, :, 0], dtype='float32')
#     dpt2 = np.asarray(dframe_data[:, :, 1], dtype='float32')
#     dpt2 *= 255
#     dpt = dpt1
#     cv2.imshow('dpt', dpt)
#
#     # 显示RGB图像
#     cframe = color_stream.read_frame()
#     cframe_data = np.array(cframe.get_buffer_as_triplet()).reshape([480, 640, 3])
#     R = cframe_data[:, :, 0]
#     G = cframe_data[:, :, 1]
#     B = cframe_data[:, :, 2]
#     cframe_data = np.transpose(np.array([B, G, R]), [1, 2, 0])
#     # print(cframe_data.shape)
#     cv2.imshow('color', cframe_data)
#
#     # 按下esc键退出循环
#     key = cv2.waitKey(27)
#     if int(key) == 113:
#         break
#
#     # 关闭设备
# depth_stream.stop()
# color_stream.stop()
# dev.close()

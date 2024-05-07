
import cv2
import numpy as np
from PyQt5.QtGui import *

def PixToArray(pix):  # pix是RGBA四通道QPixmap。额外使用PIL.Image模块
    # 忘了是哪里看到的，然后翻历史记录死活找不到，作罢
    from PIL import Image
    pImg = Image.fromqpixmap(pix)
    arr = np.array(pImg)
    arr = cv2.cvtColor(arr, cv2.COLOR_RGBA2BGRA)
    arr = arr[:, :, :3]
    return arr


def PILToQImage(PILimg):
    arr = np.array(PILimg)
    arr = cv2.cvtColor(arr, cv2.COLOR_RGBA2BGRA)
    arr = cv2.cvtColor(arr,cv2.COLOR_BGRA2RGBA)

    img = QImage(arr.data, arr.shape[1], arr.shape[0],
                 arr.shape[1] * 4, QImage.Format_RGBA8888)
    return QPixmap.fromImage(img)
    # return QPixmap.fromImage(PILimg)


def QpixmapToPIL(qimage):
    from PIL import Image
    return Image.fromqpixmap(qimage)

def ArrayToQimage(arr):
    arr = cv2.cvtColor(arr, cv2.COLOR_RGBA2BGRA)
    img = QImage(arr.data, arr.shape[1], arr.shape[0],
                 arr.shape[1] * 4, QImage.Format_RGBA8888)
    return img

def ArrayToPixmap( arr):  # arr对应四通道图片。不使用PIL.Image模块
    # https://blog.csdn.net/comedate/article/details/121259033
    # https://blog.csdn.net/weixin_44431795/article/details/122016214
    arr = cv2.cvtColor(arr, cv2.COLOR_RGBA2BGRA)
    img = QImage(arr.data, arr.shape[1], arr.shape[0],
                 arr.shape[1] * 4, QImage.Format_RGBA8888)
    return QPixmap.fromImage(img)
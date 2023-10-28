import cv2
import random
import numpy as np

class ModelData:
    def __init__(self, modelName, x, y, w, h):
        self.modelName = modelName
        self.x = x
        self.y = y
        self.w = w
        self.h = h

dataObjects = [
    ModelData(modelName="person", x=0, y=92, w=166, h=1218),
    ModelData(modelName="motorcycle", x=604, y=303, w=1581, h=1365),
    ModelData(modelName="person", x=1066, y=53, w=1507, h=1110),
    ModelData(modelName="person", x=698, y=38, w=1228, h=1170),
    ModelData(modelName="person", x=1410, y=207, w=1837, h=809),
    ModelData(modelName="motorcycle", x=1419, y=388, w=1944, h=1348),
    ModelData(modelName="helmet", x=1043, y=4, w=1272, h=214),
    ModelData(modelName="helmet", x=1492, y=216, w=1693, h=408),
    ModelData(modelName="helmet", x=753, y=45, w=1049, h=341),
]

def drawRectangle(img, x, y, w, h):
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
    return img

img = cv2.imread('D:\Project\Road Motorcycle Helmet Detection\\0710.jpg')
# cv2.imshow('img',img)

for item in dataObjects:
    # img = drawRectangle(img, item.x, item.y, item.w, item.h)
    cv2.rectangle(img, (item.x, item.y), (item.x + item.w, item.y + item.h), (0, 0, 0), 2)
    # print(item.x)

img = cv2.resize(img,(0,0),fx=0.5,fy=0.5)
cv2.imshow('resize',img)
cv2.waitKey (1000000) # 显示 10000 ms 即 10s 后消失
# cv2.destroyAllWindows()


# import numpy as np
# import cv2 as cv

# img = np.zeros((320, 320, 3), np.uint8) #生成一个空灰度图像

# # 矩形左上角和右上角的坐标，绘制一个绿色矩形
# ptLeftTop = (60, 60)
# ptRightBottom = (260, 260)
# point_color = (0, 255, 0) # BGR
# thickness = 1 
# lineType = 4
# cv.rectangle(img, ptLeftTop, ptRightBottom, point_color, thickness, lineType)

# # 绘制一个红色矩形
# ptLeftTop = (120, 100)
# ptRightBottom = (200, 150)
# point_color = (0, 0, 255) # BGR
# thickness = 1
# lineType = 8
# cv.rectangle(img, ptLeftTop, ptRightBottom, point_color, thickness, lineType)

# cv.imshow('AlanWang', img)
# cv.waitKey (1000000) # 显示 10000 ms 即 10s 后消失
# cv.destroyAllWindows()

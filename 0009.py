import cv2
import numpy as np
def create_img():
    """#创建一张三通道图像"""
    img = np.zeros([50, 40, 3], dtype=np.uint8)
    img[:, :, 2] = np.ones([50, 40])*255
    #img[:,:,2]是一种切片方式，冒号表示该维度从头到尾全部切片取出
    #所以img[:,:,2]表示切片取出所有行，所有列的第三个通道（索引为2）
    #即所有行，所有列的第三个通道(R)的值都变为255，一二通道(BG)仍为0，即所有像素变为红色BGR(0，0，255)
    cv2.imshow("created_img",img)
    cv2.waitKey(0)

create_img()
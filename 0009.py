import os
import cv2
import random
import string
import numpy as np


class VerifyImage:
    def __init__(self, num, img_w=90, img_h=40, is_gray=False, img_path='verify_img'):
        self.num = num
        self.img_w = img_w
        self.img_h = img_h
        self.is_gray = is_gray
        self.img_path = img_path

    def _create_img(self, img_name):
        """#创建一张三通道图像"""
        img = np.zeros([self.img_h, self.img_w, 1 if self.is_gray else 3], dtype=np.uint8)
        # img[:, :, 2] = np.ones([50, 40])*255
        pos_w = [(int(self.img_w // 40)) * 10 * i for i in range(4)]
        pos_h = self.img_h // 2
        # img[:, :, :] = 255
        for i in range(1000):
            img[random.randint(1, 255):random.randint(1, 255):random.randint(1, 255)] = random.randint(1, 255)
        # img[:,:,2]是一种切片方式，冒号表示该维度从头到尾全部切片取出
        # 所以img[:,:,2]表示切片取出所有行，所有列的第三个通道（索引为2）
        # 即所有行，所有列的第三个通道(R)的值都变为255，一二通道(BG)仍为0，即所有像素变为红色BGR(0，0，255)
        for i in range(4):
            cv2.putText(img, str(random.choice(string.ascii_letters + string.digits)),
                        (pos_w[i] + random.randint(1, 5), pos_h + random.randint(1, 5)),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (random.randint(1, 255), random.randint(1, 255),
                                                      random.randint(1, 255)), 2)
        # cv2.imshow("created_img", img)
        if not os.path.exists(self.img_path):
            os.makedirs(self.img_path)
        cv2.imwrite(self.img_path + '/' + str(img_name) + '.jpg', img)
        # cv2.waitKey(0)

    def create_img(self):
        for i in range(self.num):
            self._create_img(i)


if __name__ == "__main__":
    img = VerifyImage(10, 200, 50)
    img.create_img()


# TODO 自动生成标签用于深度学习训练

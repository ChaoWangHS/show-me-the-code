import cv2
import random
import face_recognition

img_path = "qiyu.png"

# image = cv2.imread("gyy.png", 1)
image = cv2.imread(img_path, 1)
image_ = face_recognition.load_image_file(img_path)

# face locations in css(top, right, bottom, left) order
facelocations = face_recognition.face_locations(image_)


hats = []
for i in range(4):
    hats.append(cv2.imread('hats/hat%d.png' % i, -1))


for face in facelocations:
    print(face)
    # face locations in css(top, right, bottom, left) order
    # 随机一顶帽子
    hat = random.choice(hats)
    # 调整帽子尺寸
    face_w = face[1]-face[-1]
    # scale = face_w / hat.shape[0] * 1.25
    scale = face_w / hat.shape[0] * 1.35
    hat = cv2.resize(hat, (0, 0), fx=scale, fy=scale)
    # 根据人脸坐标调整帽子位置
    #               x +
    x_offset = int((face[1] + face[-1])/2 - hat.shape[1] / 2)
    y_offset = int( face[0] - hat.shape[0]*0.6)
    # 计算贴图位置，注意防止超出边界的情况
    x1, x2 = max(x_offset, 0), \
             min(x_offset + hat.shape[1], image.shape[1])

    y1, y2 = max(y_offset, 0), \
             min(y_offset + hat.shape[0], image.shape[0])
    hat_x1 = max(0, -x_offset)
    hat_x2 = hat_x1 + x2 - x1
    hat_y1 = max(0, -y_offset)
    hat_y2 = hat_y1 + y2 - y1


    # 透明部分的处理
    alpha_h = hat[hat_y1:hat_y2, hat_x1:hat_x2, 3] / 255
    alpha = 1 - alpha_h

    # 按3个通道合并图片
    for c in range(0, 3):
        image[y1:y2, x1:x2, c] = \
            (alpha_h * hat[hat_y1:hat_y2, hat_x1:hat_x2, c] +
             alpha * image[y1:y2, x1:x2, c])

# 保存最终结果
cv2.imwrite('res.png', image)
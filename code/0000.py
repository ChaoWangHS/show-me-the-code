import cv2


def num_notify(pic_path, num):
    '''
    在图片右上角添加数字，类似于微信消息提示
    :param pic_path: 图片的路径
    :param num: 要显示在图片的路径
    :return: None
    '''
    img = cv2.imread(pic_path)
    # font
    font = cv2.FONT_HERSHEY_SIMPLEX
    h, w, _ = img.shape

    # fontScale
    fontScale = 1
    # Red color in BGR
    color = (0, 0, 255)
    # Line thickness of 2 px
    thickness = 2
    image = cv2.putText(img, str(num), (w - 60, 30), font,
                        fontScale, color, thickness, cv2.LINE_AA)

    # Displaying the image
    cv2.imshow("window_name", image)
    cv2.waitKey()


if __name__ == "__main__":
    num_notify("dog.jpg", 100)

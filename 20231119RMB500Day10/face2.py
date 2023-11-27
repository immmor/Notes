import cv2

def crop_image_around_face(image_path):
    # 加载Haar特征级联分类器
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # 读取图片
    k = cv2.imread(image_path)
    # 调整图像大小
    image = cv2.resize(k, (492, 689))
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 进行人脸检测
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    if len(faces) == 0:
        print("No faces found in the image.")
        return

    # 仅考虑第一个检测到的人脸
    for (x, y, w, h) in faces:
        # 计算裁剪区域
        center_x = x + w / 2
        new_width = int(w * 1.6)  # 总宽度为人脸宽度的1.6倍
        left = int(center_x - new_width / 2)
        right = int(center_x + new_width / 2)

        # 确保裁剪区域不超出原始图像
        left = max(0, left)
        right = min(image.shape[1], right)

        # 裁剪图像
        cropped_image = image[y:y+h, left:right]

        # 显示裁剪后的图像
        cv2.imshow('Cropped Image', cropped_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        # 可以选择保存图片
        # cv2.imwrite('cropped_image.jpg', cropped_image)

        break  # 只处理第一个检测到的脸

# 使用示例
image_path = '0003.jpg'  # 替换为你的图片路径
crop_image_around_face(image_path)

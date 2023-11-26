import os
import cv2
import numpy as np

def process_images(folder_path):
    # 获取文件夹中的所有图片文件
    image_files = [f for f in os.listdir(folder_path) if f.endswith('.jpg') or f.endswith('.png') or f.endswith('.jpeg')]

    for image_file in image_files:
        # 读取图像
        image_path = os.path.join(folder_path, image_file)
        image = cv2.imread(image_path)

        # 检测人脸关键点
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            # 计算关键点位置
            eye_center_x = x + w // 2
            eye_center_y = y + h // 2
            left_cheek_x = x + int(0.2 * w)
            right_cheek_x = x + int(0.32 * w)
            top_distance = y
            eye_center_distance = eye_center_y - y
            left_cheek_distance = left_cheek_x - x
            right_cheek_distance = right_cheek_x - x
            chin_distance = y + h - y
            print('计算完关键点位置')

            # 根据要求进行判断
            # if abs(left_cheek_distance - right_cheek_distance) <= 2 and \
            #         2.5 <= abs(left_cheek_distance / eye_center_distance) <= 2.6 and \
            #         0.09 <= top_distance / h <= 0.19 and \
            #         0.32 <= eye_center_distance / h <= 0.46 and \
            #         0.2 <= left_cheek_distance / w <= 0.32 and \
            #         0.2 <= right_cheek_distance / w <= 0.32 and \
            #         0.6 <= chin_distance / h <= 0.78:
                # 裁剪证件照区域
            cropped_image = image[y:y+h, x:x+w]
            print('裁剪完证件照区域')

            # 修改背景色为蓝色
            b, g, r = cv2.split(cropped_image)
            blue_bg = np.zeros_like(b)
            blue_bg[:] = 255  # 蓝色背景
            modified_image = cv2.merge((blue_bg, g, r))
            print('修改完背景色为蓝色')

            # 保存修改后的图像
            output_folder = 'output'
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)
            output_path = os.path.join(output_folder, image_file)
            cv2.imwrite(output_path, modified_image)

            print(f'Successfully processed {image_file}')

# 处理指定文件夹中的图片
folder_path = 'bie'  # 替换为你的文件夹路径
process_images(folder_path)
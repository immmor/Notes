# import os, cv2
# from resize import resize_image

# for filename in os.listdir(r'F:\\VSCode Files\\Work\\20231119RMB500Day10\\1\\unhandle10'):
#     image_path = os.path.join(r'F:\\VSCode Files\\Work\\20231119RMB500Day10\\1\\unhandle10', filename)
#     # image = cv2.imread(image_k)

#     # image_path = '0003.jpg'  # 替换为你的图像文件路径
#     resized = resize_image(image_path, 300, 400)  # 替换为你想要的缩放宽度和高度  
#     cv2.imwrite(image_path, resized)


import os
import cv2
from resize import resize_image

input_dir = r'F:\VSCode Files\Work\20231119RMB500Day10\1\ununhandle'
output_dir = r'F:\VSCode Files\Work\20231119RMB500Day10\1\resized'

# 创建输出目录（如果不存在）
os.makedirs(output_dir, exist_ok=True)

for filename in os.listdir(input_dir):
    input_path = os.path.join(input_dir, filename)
    output_path = os.path.join(output_dir, filename)

    # 调用缩放函数
    resized = resize_image(input_path, 300, 400)

    # 保存缩放后的图像
    cv2.imwrite(output_path, resized)
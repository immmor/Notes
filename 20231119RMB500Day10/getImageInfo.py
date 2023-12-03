import os
import cv2

# 读取图像
# image_folder = r'F:\\VSCode Files\\Work\\20231119RMB500Day10\\1\\ununhandle'  # 替换为你的图像文件夹路径
# image_folder = r'F:\VSCode Files\Work\20231119RMB500Day10\1\resized'
image_folder = '/Users/mrok/Documents/coder/funtext/Web/Notes/20231119RMB500Day10/1/resized'

for filename in os.listdir(image_folder):
    image_path = os.path.join(image_folder, filename)
    image = cv2.imread(image_path)

    # # 查看像素值
    # pixel_value = image[100, 200]  # 获取指定像素位置的值，这里以行索引为100、列索引为200的像素为例
    # print(f"Pixel value at (100, 200) in {filename}: {pixel_value}")

    # 查看尺寸
    height, width, channels = image.shape
    print(f"Image width of {filename}: {width}")
    print(f"Image height of {filename}: {height}")
    print(f"Number of channels of {filename}: {channels}")
    print('----------------------------------------')

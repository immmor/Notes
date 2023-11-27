import cv2

def crop_image(image_path, width, height):
    # 读取图像
    image = cv2.imread(image_path)

    # 获取图像的原始宽度和高度
    image_height, image_width, _ = image.shape

    # 确保裁剪区域不超出图像边界
    if width > image_width or height > image_height:
        print("Error: The specified crop size is larger than the image size.")
        return None

    # 计算裁剪区域的起始坐标
    start_x = (image_width - width) // 2
    start_y = (image_height - height) // 2

    # 裁剪图像
    cropped_image = image[start_y:start_y+height, start_x:start_x+width]

    return cropped_image

# 测试裁剪函数
image_path = '0003.jpg'  # 替换为你的图像文件路径
cropped = crop_image(image_path, 492, 689)  # 替换为你想要的裁剪宽度和高度(492, 689)

# 显示裁剪后的图像
cv2.imshow("Cropped Image", cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()
import os
import cv2

def resize_image(image_path, width, height):
    # 读取图像
    image = cv2.imread(image_path)

    # 缩放图像
    resized_image = cv2.resize(image, (width, height))

    return resized_image

# 测试缩放函数
image_path = '0003.jpg'  # 替换为你的图像文件路径
resized = resize_image(image_path, 300, 400)  # 替换为你想要的缩放宽度和高度  
cv2.imwrite(os.path.join(r'F:\\VSCode Files\\Work\\20231119RMB500Day10\\handled', image_path), resized)

# 显示缩放后的图像
# cv2.imshow("Resized Image", resized)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

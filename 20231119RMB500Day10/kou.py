import cv2
import numpy as np

def image_segmentation(image_path):
    # 读取图像
    image = cv2.imread(image_path)

    # 将图像转换为灰度图
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 进行阈值分割
    _, threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

    # 查找图像中的轮廓
    contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 创建与原始图像相同大小的掩膜图像
    mask = np.zeros_like(image)

    # 绘制轮廓到掩膜图像上
    cv2.drawContours(mask, contours, -1, (255, 255, 255), thickness=cv2.FILLED)

    # 将掩膜图像与原始图像进行位运算，抠出目标区域
    result = cv2.bitwise_and(image, mask)

    # 保存抠图结果到当前文件夹
    output_path = 'segmented_image.jpg'
    cv2.imwrite(output_path, result)

    return output_path

# 测试图像抠图函数
image_path = '0003.jpg'  # 替换为你的图像文件路径
segmented_image_path = image_segmentation(image_path)

print("抠图结果已保存至:", segmented_image_path)
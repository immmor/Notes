import dlib
import numpy as np
import cv2

# 加载人脸检测器和关键点检测器
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")  # 下载预训练的关键点检测器模型并指定路径

def detect_hair_top(image_path):
    # 读取图像
    image = cv2.imread(image_path)

    # 将图像转换为灰度图
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 人脸检测
    faces = detector(gray)

    # 遍历检测到的人脸
    for face in faces:
        # 关键点检测
        landmarks = predictor(gray, face)

        # 提取头顶（头发）位置
        top_points = []
        for n in range(17, 27):  # 修改关键点的范围，适应头顶的位置
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            top_points.append((x, y))

        # 绘制头顶（头发）区域
        cv2.polylines(image, [np.array(top_points)], False, (0, 255, 0), thickness=2)

    # 显示带有头顶（头发）区域的图像
    cv2.imshow("Hair Top Detection", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 测试头顶（头发）检测函数
image_path = '0003.jpg'  # 替换为你的图像文件路径
detect_hair_top(image_path)
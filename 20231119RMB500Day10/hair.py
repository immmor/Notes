import dlib
import cv2

# 加载人脸检测器和关键点检测器
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")  # 替换为你的关键点检测器模型路径

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

        # 提取头顶（头发）关键点
        hair_top_points = []
        for n in range(21, 27):  # 修改关键点的范围
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            hair_top_points.append((x, y))

        # 在图像上绘制头顶（头发）关键点
        for point in hair_top_points:
            cv2.circle(image, point, 2, (0, 255, 0), -1)

    # 将带有头顶（头发）关键点的图像保存到当前路径
    output_path = 'hair_top_marked.jpg'
    cv2.imwrite(output_path, image)

    return output_path

# 测试头顶（头发）检测函数
image_path = '0003.jpg'  # 替换为你的图像文件路径
marked_image_path = detect_hair_top(image_path)

print("标记后的图像已保存至:", marked_image_path)
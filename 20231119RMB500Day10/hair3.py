import cv2
import dlib

# 加载人脸检测器
detector = dlib.get_frontal_face_detector()

# 加载人脸关键点检测器
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")  # 下载预训练的关键点检测器模型并指定路径

# 加载图像
image = cv2.imread("0003.jpg")  # 将路径替换为您的图像路径

# 将图像转换为灰度图像
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 使用人脸检测器检测图像中的所有人脸
faces = detector(gray)

# 对于每个检测到的人脸
for face in faces:
    # 检测人脸关键点
    landmarks = predictor(gray, face)
    
    # 获取头部区域的边界框（包含头部和脸部）
    x = face.left()
    y = face.top()
    w = face.width()
    h = face.height()
    
    # 在图像中绘制头部区域的矩形框
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

# 显示结果图像
cv2.imshow("Head Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
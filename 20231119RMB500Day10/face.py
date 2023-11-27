import cv2

def detect_faces(image_path):
    # 加载Haar特征级联分类器
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # 读取图片
    k = cv2.imread(image_path)
    # 调整图像大小
    image = cv2.resize(k, (492, 689))
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 进行人脸检测
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # 在检测到的人脸周围画矩形框
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
        # 在人脸上方的区域搜索头发的最高点
        hair_top = y - 80  # 假设头发的最高位置在人脸上方20个像素的位置

        # 画头顶的线
        cv2.line(image, (x, hair_top), (x+w, hair_top), (0, 255, 0), 2)  # 画头顶的线
        # cv2.line(image, (x, y+h), (x+w, y+h), (0, 255, 0), 2)  # 画下巴的线



    # 检测眼睛
    # 加载Haar特征级联分类器
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
    # 进行眼睛检测
    eyes = eye_cascade.detectMultiScale(gray, 1.1, 4)
    # 在检测到的眼睛周围画矩形框
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(image, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

    # if len(eyes) >= 2:
    #     # 计算两只眼睛的中心点
    #     eye1_center = (eyes[0][0] + eyes[0][2]//2, eyes[0][1] + eyes[0][3]//2)
    #     eye2_center = (eyes[1][0] + eyes[1][2]//2, eyes[1][1] + eyes[1][3]//2)
    #     # 画一条横线连接两只眼睛的中心点
    #     cv2.line(image, eye1_center, eye2_center, (0, 255, 0), 2)




    # 显示结果
    cv2.imshow('Face Detected', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # 可以选择保存结果
    # cv2.imwrite('face_detected.jpg', image)

# 使用示例
image_path = '0008.jpg'  # 替换为你的图片路径
detect_faces(image_path)

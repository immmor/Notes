import face_recognition
import cv2
import numpy as np
# python3.8安装成功

def face_login(target_image_path):
    # 加载目标图像
    target_image = face_recognition.load_image_file(target_image_path)
    target_encoding = face_recognition.face_encodings(target_image)[0]

    # 初始化摄像头
    cap = cv2.VideoCapture(0)

    while True:
        # 读取一帧
        ret, frame = cap.read()
        if not ret:
            break

        # 将图像从BGR颜色（OpenCV使用）转换为RGB颜色（face_recognition使用）
        rgb_frame = frame[:, :, ::-1]

        # 找到所有人脸
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            # 比较人脸
            matches = face_recognition.compare_faces([target_encoding], face_encoding)

            if matches[0]:
                # 在人脸周围画一个绿色的框
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                # 在框上方写"登录成功"
                cv2.putText(frame, "Login Successful", (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
                print("登录成功!")
            else:
                # 在人脸周围画一个红色的框
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # 显示结果
        cv2.imshow('Video', frame)

        # 按'q'退出
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 释放摄像头并关闭窗口
    cap.release()
    cv2.destroyAllWindows()

# 使用方法
target_image_path = "dian.jpg"  # 替换为您的目标图像路径
face_login(target_image_path)
import face_recognition
import cv2
import numpy as np
from flask import Flask, render_template, Response

app = Flask(__name__)

# 加载目标图像并编码人脸
target_image = face_recognition.load_image_file("dian.jpg")
target_encoding = face_recognition.face_encodings(target_image)[0]

def gen_frames():
    camera = cv2.VideoCapture(0)
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            # 将图像从BGR颜色（OpenCV使用）转换为RGB颜色（face_recognition使用）
            rgb_frame = frame[:, :, ::-1]
            
            # 在当前帧中找到所有人脸和人脸编码
            face_locations = face_recognition.face_locations(rgb_frame)
            face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

            for face_encoding in face_encodings:
                # 检查人脸是否与目标图像匹配
                matches = face_recognition.compare_faces([target_encoding], face_encoding)
                
                if matches[0]:
                    # 如果匹配，在图像上绘制绿色矩形
                    top, right, bottom, left = face_locations[0]
                    cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                    cv2.putText(frame, "Login Success", (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
                    print("登录成功")
                else:
                    # 如果不匹配，在图像上绘制红色矩形
                    top, right, bottom, left = face_locations[0]
                    cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                    cv2.putText(frame, "Login Failed", (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
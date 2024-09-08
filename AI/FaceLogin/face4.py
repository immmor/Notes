import face_recognition
import cv2
import numpy as np
from flask import Flask, render_template, Response, jsonify
import os

# 这里一直调用的是电脑摄像头

app = Flask(__name__)
# app.config['JSON_AS_ASCII'] = False

# 用户数据库
users_db = {}

# 加载用户数据
def load_users():
    global users_db
    images_dir = "user_images"
    for filename in os.listdir(images_dir):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            name = os.path.splitext(filename)[0]
            # name = os.path.splitext(filename)[0].encode('utf-8')
            image_path = os.path.join(images_dir, filename)
            image = face_recognition.load_image_file(image_path)
            encoding = face_recognition.face_encodings(image)[0]
            users_db[name] = {"name": name, "encoding": encoding}

load_users()

login_success_count = 0
login_complete = False
logged_in_user = None

def gen_frames():
    global login_success_count
    global login_complete
    global logged_in_user
    camera = cv2.VideoCapture(0)
    while not login_complete:
        success, frame = camera.read()
        if not success:
            break
        else:
            rgb_frame = frame[:, :, ::-1]
            
            face_locations = face_recognition.face_locations(rgb_frame)
            face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces([user['encoding'] for user in users_db.values()], face_encoding)
                
                if True in matches:
                    matched_user_name = list(users_db.keys())[matches.index(True)]
                    top, right, bottom, left = face_locations[0]
                    cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                    # cv2.putText(frame, f"Login Success: {matched_user_name}", (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
                    cv2.putText(frame, f"Login Success", (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

                    login_success_count += 1
                    logged_in_user = matched_user_name
                    print(matched_user_name + "登录成功")
                    if login_success_count >= 5:
                        login_complete = True
                else:
                    top, right, bottom, left = face_locations[0]
                    cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                    cv2.putText(frame, "Login Failed", (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
                    login_success_count = 0
                    logged_in_user = None

            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    camera.release()

@app.route('/')
def index():
    return render_template('index4.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/login_status')
def login_status():
    global login_complete, logged_in_user
    # login_complete = False
    return jsonify({'login_complete': login_complete, 'user': logged_in_user})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
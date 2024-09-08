from flask import Flask, render_template, request, jsonify
import face_recognition
import numpy as np
import base64
import io
from PIL import Image

app = Flask(__name__)

# 目标图像（这里你需要替换为你的目标人脸图像）
target_image = face_recognition.load_image_file("dian.jpg")
target_encoding = face_recognition.face_encodings(target_image)[0]


@app.route('/')
def index():
    return render_template('index5.html')


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    image_data = data['imageData']
    image_data = image_data.split(',')[1]
    image_bytes = io.BytesIO(base64.b64decode(image_data))
    image = Image.open(image_bytes)
    image_np = np.array(image)
    face_locations = face_recognition.face_locations(image_np)
    if len(face_locations) > 0:
        face_encodings = face_recognition.face_encodings(image_np, face_locations)[0]
        results = face_recognition.compare_faces([target_encoding], face_encodings)
        if results[0]:
            print("登录成功")
            return jsonify({"success": True})
    return jsonify({"success": False})


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")

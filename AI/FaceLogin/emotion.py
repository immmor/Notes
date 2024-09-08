import face_recognition
import numpy as np
import cv2
from keras.models import load_model
emotion_dict= {'生气': 0, '悲伤': 5, '中性': 4, '厌恶': 1, '惊讶': 6, '恐惧': 2, '高兴': 3}

image = face_recognition.load_image_file("1.png")
# 载入图像
face_locations = face_recognition.face_locations(image)
# 寻找脸部
top, right, bottom, left = face_locations[0]
# 将脸部框起来

face_image = image[top:bottom, left:right]
face_image = cv2.resize(face_image, (48,48))
face_image = cv2.cvtColor(face_image, cv2.COLOR_BGR2GRAY)
face_image = np.reshape(face_image, [1, face_image.shape[0], face_image.shape[1], 1])
# 调整到可以进入该模型输入的大小

model = load_model("./model_v6_23.hdf5")
# 载入模型

predicted_class = np.argmax(model.predict(face_image))
# 分类情绪
label_map = dict((v,k) for k,v in emotion_dict.items()) 
predicted_label = label_map[predicted_class]
# 根据情绪映射表输出情绪
print(predicted_label)

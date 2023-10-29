import pytesseract, pyautogui
from PIL import ImageGrab
import os


while True:
    # 获取屏幕截图
    # print(pyautogui.position())
    screenshot = ImageGrab.grab(bbox=(922, 413, 1226, 693))
    # 将截图转换为灰度图像
    screenshot = screenshot.convert("L")
    # 使用 PyTesseract 进行文字识别
    text = pytesseract.image_to_string(screenshot, lang='chi_sim')
    # 输出识别结果
    print(text)
    
    # 删除截图文件
    # screenshot_path = 'screenshot.png'  # 截图文件保存路径
    # if os.path.exists(screenshot_path):
    #     os.remove(screenshot_path)
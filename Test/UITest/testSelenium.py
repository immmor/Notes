from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
broswer = webdriver.Chrome(options=chrome_options)

def test_notes():
    broswer.get("http://127.0.0.1:666/eng")#访问百度页面
    # time.sleep(3)
    # broswer.find_element(By.ID, 'username').send_keys('wangdian') 
    # broswer.find_element(By.ID, 'passwordid').send_keys('wangdian123')
    # broswer.find_element(By.ID, 'submit').click()
    time.sleep(3)
    print(broswer.title, broswer.get_cookie)
    time.sleep(30)
    broswer.quit()


def test_baidu():
    broswer.get('https://www.baidu.com')
    broswer.find_element(By.ID, 'kw').send_keys('Python')
    broswer.find_element(By.ID, 'su').click()
    time.sleep(3) 
    print(broswer.title)
    # broswer.quit()


if __name__ == "__main__":
    # test_baidu()
    test_notes()

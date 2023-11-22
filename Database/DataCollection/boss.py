from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False) 
broswer = webdriver.Chrome(options=chrome_options)

broswer.get("https://www.zhipin.com/job_detail/?query=python&city=101010100")#访问百度页面
# time.sleep(3)
# broswer.find_element(By.ID, 'username').send_keys('wangdian') 
# broswer.find_element(By.ID, 'passwordid').send_keys('wangdian123')
# broswer.find_element(By.ID, 'submit').click()
time.sleep(3)
print(broswer.title, broswer.get_cookie)
broswer.quit()

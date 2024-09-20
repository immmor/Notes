import json
import requests

cookies = {
    'SECKEY_ABVK': 'UAkK9GohbL2OBf0YATu4DwQlK9V8FOm77nIcnXqs+pJRt1arTv+kuQfqvIuKuSrxn03Z9c5yCnxw/TEo8gDihg%3D%3D',
    'BMAP_SECKEY': 'UAkK9GohbL2OBf0YATu4DwQlK9V8FOm77nIcnXqs-pLC025MxpvCg8uJbH15ud8kVDziOidgSLz5U5uGkikLELaRt7VnadM-NqUo-SwqNYUyJcjSCR2EYWh-rxUpEl5bO3nzyKYUtUIuUD9k2nro5E-272aRJ1i7_oHh2twUmIDJhiuYHd1skZS6cdhBqcR20YfFYeePv9KnJNBqQPbfxpSnWL1q326YAnekwQODIP0',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'en,de;q=0.9,en-US;q=0.8,fr-FR;q=0.7,fr;q=0.6,zh-CN;q=0.5,zh;q=0.4',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    # 'Cookie': 'SECKEY_ABVK=UAkK9GohbL2OBf0YATu4DwQlK9V8FOm77nIcnXqs+pJRt1arTv+kuQfqvIuKuSrxn03Z9c5yCnxw/TEo8gDihg%3D%3D; BMAP_SECKEY=UAkK9GohbL2OBf0YATu4DwQlK9V8FOm77nIcnXqs-pLC025MxpvCg8uJbH15ud8kVDziOidgSLz5U5uGkikLELaRt7VnadM-NqUo-SwqNYUyJcjSCR2EYWh-rxUpEl5bO3nzyKYUtUIuUD9k2nro5E-272aRJ1i7_oHh2twUmIDJhiuYHd1skZS6cdhBqcR20YfFYeePv9KnJNBqQPbfxpSnWL1q326YAnekwQODIP0',
    'Origin': 'https://www.huatuogpt.cn',
    'Referer': 'https://www.huatuogpt.cn/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

json_data = {
    'sessionId': '1286392997850783744',
    'userMessage': '你是什么模型\n',
    'questionId': 0,
}


response = requests.post('https://www.huatuogpt.cn/api/questionAndGetSeeAnswer', cookies=cookies, headers=headers, json=json_data)
response.encoding = 'utf-8'  # 设置响应的编码为UTF-8

import re

# 使用正则表达式截取最后一个data:后的内容
last_data = re.findall(r'data:(.*?)(?:\n|$)', response.text)[-1].strip()

# 将last_data的内容转换成python字典格式
python_dict = json.loads(last_data)
print(python_dict['content'])
# except json.JSONDecodeError:
#     print("无法将内容转换为JSON格式。原始内容:", last_data)

# print(json_data)
# print("数据类型：", type(json_data))

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"sessionId":"1286387173204041728","userMessage":"我想要了\\n","questionId":0}'.encode()
#response = requests.post('https://www.huatuogpt.cn/api/questionAndGetSeeAnswer', cookies=cookies, headers=headers, data=data)
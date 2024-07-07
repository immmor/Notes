import requests

resp = requests.get('https://dict.youdao.com/suggest?num=5&ver=3.0&doctype=json&cache=false&le=en&q=hello')
print(resp.json())
import requests

session = requests.Session()
session.cookies.set('userInfo', '3a628e75aef28ff5525b5b80f4239dbc|779aa2e89bf90a468aaef5ae28d628a9')
response = session.get('http://127.0.0.1:666/interview')
print(response.text)

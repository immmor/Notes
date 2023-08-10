__version__ = "0.0.1"

import requests

# from fake_useragent import UserAgent
# ua = UserAgent()
# print(ua.chrome)

def fan(showIP=True):
    proxy = '127.0.0.1:1082'
    proxies = {
        'http': 'http://' + proxy,
        'https': 'https://' + proxy,
    }
    # headers = {
    #     'User-Agent': ua.chrome
    # }
    try:
        response = requests.get('http://www.bing.com', proxies=proxies)
        print(response.status_code, ' 可以连外网，但不一定是美国服务器')
        if showIP:
            resp = requests.get('http://httpbin.org/ip', proxies=proxies)
            print(resp.json()['origin'])
        return True
    except:
        print('有问题，没法翻')
        return False
    

import timeit

print('函数执行时间：', timeit.timeit(fan, number=1), '秒')

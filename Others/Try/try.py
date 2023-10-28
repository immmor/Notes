__version__ = "0.0.1"

import requests

# from fake_useragent import UserAgent
# ua = UserAgent()
# print(ua.chrome)

def win_winxray_fan(showIP=True):
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
            ip = resp.json()['origin']
            print(ip)
            r = requests.get(f'http://ip-api.com/json/{ip}?lang=zh-CN', proxies=proxies)
            print(r.text)
            # check_ip(ip)
        return True
    except:
        print('有问题，没法翻')
        return False
    

def mac_clash_fan(showIP=True):
    # proxy = '172.20.10.7:9090'
    proxy = '127.0.0.1:7890'
    proxies = {
        'http': 'http://' + proxy,
        'https': 'https://' + proxy,
    }
    # headers = {
    #     'User-Agent': ua.chrome
    # }
    # response = requests.get('http://www.bing.com', proxies=proxies)
    # print(response.status_code, ' 可以连外网，但不一定是美国服务器')
    if showIP:
        resp = requests.get('http://httpbin.org/ip', proxies=proxies)
        ip = resp.json()['origin']
        r = requests.get(f'http://ip-api.com/json/{ip}?lang=zh-CN', proxies=proxies)
        print(r.text)
        
    return True
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
    

def check_ip(ip):
    # url = "http://ip.taobao.com/service/getIpInfo.php?ip=" + ip
    url = "http://whois.pconline.com.cn/?ip=" + ip
    r = requests.get(url)
    print(r.text)


import timeit
import sys

if sys.platform.startswith('win'):
    print('Windows')
    print('函数执行时间：', timeit.timeit(win_winxray_fan, number=1), '秒')
elif sys.platform.startswith('darwin'):
    print('mac')
    print('函数执行时间：', timeit.timeit(mac_clash_fan, number=1), '秒')
elif sys.platform.startswith('linux'):
    print('Linux system')
else:
    print('Other system')

# check_ip('221.222.20.13')

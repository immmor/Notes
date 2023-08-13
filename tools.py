import csv, json, time, requests

# 获取json里面数据
def get_json_data(jsonFileName=''):
    with open(jsonFileName, 'rb') as f:  # 使用只读模型，并定义名称为f
        params = json.load(f)  # 加载json文件
        # params["code"] = "404"  # code字段对应的值修改为404
        # print(params)  # 打印
    return params  # 返回修改后的内容


def write_json_data(params, jsonFileName=''):
    # 使用写模式，名称定义为r
    # 其中路径如果和读json方法中的名称不一致，会重新创建一个名称为该方法中写的文件名
    with open(jsonFileName, 'w', encoding='utf-8') as f:
        # 将dict写入名称为r的文件中
        json.dump(params, f, ensure_ascii=False)


def get_csv():
    with open('try.csv',encoding='utf-8')as fp:
        reader = csv.reader(fp)
        # 获取标题
        header = next(reader)
        print(header)
        # 遍历数据
        for i in reader:
            print(i)

            
def write_file(content):
    with open('claudeAI.txt', 'a+') as f:
        f.write(content + '\n')
        

def claude_ai(text):
    slackToken = 'xoxp-415445285921-416003551682-5356031879952-e553f10d7af397d89db28fe1865ee985'
    def send_msg():
        sendURL = "https://slack.com/api/chat.postMessage"
        data = {
            "token": slackToken,
            "channel": "@Claude",
            "text": text
        }
        response = requests.post(sendURL, data=data)
        print(text)
        time.sleep(2)
        return response.text

    msgSent = json.loads(send_msg())

    def receive_msg():
        receiveURL = "https://slack.com/api/conversations.history"
        data = {
            "token": slackToken,
            "channel": "D052WQCP84D",
            "oldest": msgSent['ts']
        }
        response = requests.post(receiveURL, data=data)
        result = json.loads(response.text)
        try:
            if 'Typing' in result['messages'][1]['text']:
                time.sleep(2)
                return receive_msg()
            elif 'Typing' not in result['messages'][1]['text']:
                resultMessage = result['messages'][1]['text']
                return resultMessage
        except:
            if 'Typing' in result['messages'][0]['text']:
                time.sleep(2)
                return receive_msg()
            elif 'Typing' not in result['messages'][0]['text']:
                resultMessage = result['messages'][0]['text']
                return resultMessage
            
    return receive_msg()


def dify_ai(ask):
    url = 'https://api.dify.ai/v1/completion-messages'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer app-JPWdrBbT7GNtJM6VRc2wbNcZ',
    }
    payload = json.dumps({
        "inputs": {},
        "query": ask,
        "response_mode": "blocking",
        "user": "kkbb2"
    })
    response = requests.request("POST", url, headers=headers, data=payload)
    finalData = json.loads(response.text)
    print(finalData)


def trans_youdao(transContent: str):
    import requests
    data = {
        'doctype': 'json', 
        'type': 'auto',
        'i': transContent
    }
    r = requests.get("http://fanyi.youdao.com/translate",params=data)
    result = r.json()['translateResult'][0][0]['tgt']
    print(result)
    return result


def trans_baidu(transContent: str):
    import requests
    data = {
        'from': 'en',
        'to': 'zh',
        'query': transContent,
        'transtype': 'realtime',
        'simple_means_flag': '3',
        'sign': '114200.614200',
        'token': '4085722948',
        'domain': 'common'
    }
    r = requests.post('https://fanyi.baidu.com/translate?aldtype=16047&query=%E5%A4%AA%E7%BE%8E%E4%BA%86&keyfrom=baidu&smartresult=dict&lang=auto2jp#zh', data=data)


def trans_google(text, dest='zh-cn'):
    from httpcore import SyncHTTPProxy
    from googletrans import Translator
    http_proxy = SyncHTTPProxy((b'http', b'127.0.0.1', 1082, b''))
    proxies = {'http': http_proxy, 'https': http_proxy }
    translator = Translator(proxies=proxies)
    trans = translator.translate(text, dest=dest)
    print(trans.text)


def trans_micro(transContent):
    from translate import Translator
    translator=Translator(from_lang="chinese",to_lang="english")
    translation = translator.translate("你吃了吗？")
    print(translation)
    translator2=Translator(from_lang="english",to_lang="chinese")
    translation = translator2.translate(transContent)
    print(translation)

    
def fan(showIP=False):
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
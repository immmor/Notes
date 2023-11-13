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


def get_csv(fileName):
    with open(fileName, encoding='utf-8')as fp:
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
    # slackToken = 'xoxp-5188530118690-5188398037171-5733621356819-a30475dd9a71f0346814dc13f1a0465e'  # tzbg
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
            # "channel": "D055M0TE4MA",  # tzbg
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
                # print(result)  # TODO
                resultMessage = result['messages'][1]['text'].strip()
                return resultMessage
        except:
            if 'Typing' in result['messages'][0]['text']:
                time.sleep(2)
                return receive_msg()
            elif 'Typing' not in result['messages'][0]['text']:
                # print(result)
                resultMessage = result['messages'][0]['text'].strip()
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


def chatanywhere_ai(ask, stream=False):
    # 调用的openai的api
    # https://github.com/chatanywhere/GPT_API_free
    import openai
    # openai.api_key = "sk-O7hjZCtWA6saoobUYBleIdG2b1UIdDsOJzW0HsW21qnFCMrU" 
    openai.api_key = "sk-bCnBAlsepSdqg8DaM6RCGKAk4DrF46rq9tNy6tv32xJvJk6S"
    openai.api_base = "https://api.chatanywhere.com.cn/v1"
    if stream is False:
        # 非流式响应
        completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": ask}])
        result = completion.choices[0].message.content
        print(result)
        return result
    else:
        # 流式响应
        try:
            response = openai.ChatCompletion.create(
                model='gpt-3.5-turbo',
                messages=[{'role': 'user','content': ask},],
                stream=True,
            )
            completion = {'role': '', 'content': ''}
            for event in response:
                if event['choices'][0]['finish_reason'] == 'stop':
                    print(f'收到的完成数据: {completion}')
                    break
                for delta_k, delta_v in event['choices'][0]['delta'].items():
                    print(f'流响应数据: {delta_k} = {delta_v}')
                    completion[delta_k] += delta_v
            # messages.append(completion)  # 直接在传入参数 messages 中追加消息
            return (True, '')
        except Exception as err:
            return (False, f'OpenAI API 异常: {err}')


def ai(ask):
    funcs = [chatanywhere_ai, dify_ai, claude_ai]
    for func in funcs:
        try:
            func(ask)
            break
        except Exception as e:
            print(f"函数 {func.__name__} 报错: {str(e)}")


def trans_youdao(transContent: str):
    # 不可用 not available
    import requests
    data = {
        'doctype': 'json', 
        'type': 'auto',
        'i': transContent
    }
    r = requests.get("https://dict.youdao.com/webtranslate",params=data)
    # result = r.json()['translateResult'][0][0]['tgt']
    result = r.json()
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


def which_system():
    pass


def play_audio():
    from pydub import AudioSegment

    # Load the WAV file
    audio = AudioSegment.from_wav('F:\\VSCode Files\\Web\\notes\\1.wav')

    # Play the audio in a loop
    play(audio, loop=True)


def judge_answer():
    question = "[简述以下五个python标准库，os、sys、re、math、datatime。]"
    standardAnswer = """
    [当谈到Python编程时，以下五个标准库是非常重要且常用的：os、sys、re、math和datetime。以下是对每个标准库的简要描述：
    1、os（操作系统接口）：os库提供了与操作系统进行交互的功能。它允许您执行文件和目录操作，例如创建、删除、重命名文件、获取目录内容等。此外，它还提供了与进程、环境变量和路径相关的函数。os库是编写与操作系统相关代码的关键工具。
    2、sys（系统特定参数和函数）：sys库允许您访问与Python解释器和运行时环境相关的变量和函数。它提供了许多与系统交互和控制相关的功能。通过sys库，您可以访问命令行参数、标准输入输出、错误处理等。
    3、re（正则表达式操作）：re库是正则表达式的Python实现。它提供了一套功能强大的工具，用于在文本中搜索、匹配和替换模式。使用re库，您可以执行复杂的匹配和模式查找操作，从而实现高级的字符串处理和文本分析。
    4、math（数学运算）：math库提供了许多常用的数学函数和常量。它包含了各种数值计算的工具，如三角函数、指数函数、对数函数、幂运算、数值近似等。使用math库，您可以进行各种数学运算和数值处理。
    5、datetime（日期和时间操作）：datetime库提供了处理日期和时间的功能。它允许您创建、操作和格式化日期时间对象，计算日期时间之间的差异，并进行日期时间的格式化和解析。datetime库使得在Python中处理日期和时间变得更加方便。
    这些标准库是Python编程中的基础工具，通过它们，您可以进行文件操作、系统交互、正则表达式匹配、数学计算和日期时间处理等各种常见任务。它们在Python社区广泛使用，并且为开发者提供了强大的功能和灵活性。]
    """
    myAnswer = """
    [1、os
    2、sys（系统特定参数和函数）
    3、re（正则表达式操作）
    4、math
    5、datetime（日期和时间操作）]
    """
    prompt = """
    这里有一道论述题：
    """ + question + """
    这是它的标准答案：
    """ + standardAnswer + """
    这是我的回答：
    """ + myAnswer + """
    10分为满分，请问依据标准答案我的回答能拿多少分？
    """
    return claude_ai(prompt)


def ipQuery(ip):
    # 淘宝api接口
    url = "http://ip.taobao.com/outGetIpInfo?ip={}&accessKey=alibaba-inc".format(ip)
    req = requests.get(url).text
    json1 = json.loads(req)
    country = json1["data"]["country"]  # 国
    isp_id = json1["data"]["isp_id"]
    province = json1["data"]["region"]  # 省
    city = json1["data"]["city"]  # 市
    county = json1["data"]["county"]
    region = json1["data"]["region"]
    area = json1["data"]["county"]
    # return "{}-{}-{}-{}-{}-{}".format(country, province, city, county, region, area)
    return "{}-{}-{}".format(country, province, city)


def get_toutiao(playf=False):
    import requests, datetime, concurrent.futures
    from playsound import playsound 
    url = 'http://v.juhe.cn/toutiao/index'
    # categoryList = ['top', 'shehui', 'guonei', 'guoji', 'yule', 'tiyu', 'junshi', 'keji', 'caijing', 'shishang']
    categoryList = ['top', 'guoji', 'junshi', 'keji']
    # myInterestsCategoryList = ['top', 'guoji', 'junshi', 'keji']
    # categoryGen = (i for i in categoryList)
    # category = next(categoryGen)
    dataInFile = get_json_data('Statics/Others/news.json')
    today = str(datetime.datetime.now()).split(' ')[0]
    if today not in dataInFile['usedIndex']:
        dataInFile['usedIndex'][today] = 0
    elif dataInFile['usedIndex'][today] == len(categoryList) - 1:
        dataInFile['usedIndex'][today] = 0
    else:
        dataInFile['usedIndex'][today] += 1
    newsType = categoryList[dataInFile['usedIndex'][today]]
    params = {
        "type": newsType,  # 头条类型,top(头条，默认),shehui(社会),guonei(国内),guoji(国际),yule(娱乐),tiyu(体育)junshi(军事),keji(科技),caijing(财经),shishang(时尚)
        "key": "7d523054ec118517fc2b4647f883f44e",  # 您申请的接口API接口请求Key
    }
    response = requests.post(url, params)
    responseJson = json.loads(response.text)
    titleList = []
    for i in responseJson['result']['data']:
        # 报这个错的话：”TypeError: 'NoneType' object is not subscriptable“，应该是当天的额度用完了
        print(i['title'])
        titleList.append(i['title'])
    if playf:
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            # 将任务添加到线程池中
            for i in titleList:
                executor.submit(text2speech, i, playf=False, folderName=newsType)
    dataInFile['result']['data'] += responseJson['result']['data']
    write_json_data(dataInFile, jsonFileName='Statics/Others/news.json')
    if playf and sys.platform.startswith('darwin'):
        nowDay = datetime.datetime.now().strftime("%Y-%m-%d")
        if os.path.exists('MP3Files/' + nowDay + '/' + newsType):
            mp3List = os.listdir('MP3Files/' + nowDay + '/' + newsType)
            print(mp3List)
            print("本文件夹共有" + str(len(mp3List)) + "个文件")
            [playsound('MP3Files/' + nowDay + '/' + newsType + '/' + i) for i in mp3List if i.endswith('.mp3')]
    elif playf and sys.platform.startswith('win'):
        from pydub import AudioSegment
        from pydub.playback import play
        # audio = AudioSegment.from_file()
        nowDay = datetime.datetime.now().strftime("%Y-%m-%d")
        if os.path.exists('MP3Files/' + nowDay + '/' + newsType):
            mp3List = os.listdir('MP3Files/' + nowDay + '/' + newsType)
            print(mp3List)
            print("本文件夹共有" + str(len(mp3List)) + "个文件")
            [playf(AudioSegment.from_file('MP3Files/' + nowDay + '/' + newsType + '/' + i)) for i in mp3List if i.endswith('.mp3')]
        # playf(audio)


def text2speech(text, playf, folderName):
    import platform
    # from pydub import AudioSegment
    # from pydub.playback import play
    from playsound import playsound  
    ttsLink = [
        f"https://dict.youdao.com/dictvoice?audio={text}&le=zh", 
        f"https://dict.youdao.com/dictvoice?audio={text}&type=1",
        f"https://fanyi.baidu.com/gettts?lan=zh&text={text}&spd=5&source=web",
        f"https://fanyi.sogou.com/reventondc/synthesis?text={text}&speed=1&lang=zh-CHS&from=translateweb&speaker=6"
    ]
    r = requests.get(ttsLink[0])
    # print(r.content)
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    nowDay = datetime.datetime.now().strftime("%Y-%m-%d")
    # print(nowDay)
    if not os.path.exists('MP3Files/'+ nowDay + '/' + folderName):
        os.makedirs('MP3Files/' + nowDay + '/' + folderName)
    mp3FileName = 'MP3Files/' + nowDay + '/' + folderName + '/' + now + text[:2] + '.mp3'
    # mp3FileName = 'a.mp3'
    # TODO: text2speech
    with open (mp3FileName, 'wb+') as f:
        f.write(r.content)
    if playf and sys.platform.startswith('darwin'):
        playsound(mp3FileName)
    elif playf and sys.platform.startswith('win'):
        from pydub import AudioSegment
        from pydub.playback import play
        audio = AudioSegment.from_file(mp3FileName)
        playf(audio)
        # if platform.system() == 'Darwin':  # macOS
        #     playsound(mp3FileName)
        # elif platform.system() == 'Windows':  # Windows
        #     audio = AudioSegment.from_file(mp3FileName, format="mp3")
        #     playf(audio)
        # else:
        #     print("Unsupported operating system.")


def word_count(text):
    num = len(text.split(' '))
    print(num)
    return num


if __name__ == '__main__':
    # prompt = "给我3个Web UI自动化测试面试题并给出相应的答案(请用markdown格式输出)。"
    # print(claude_ai(prompt))
    # ai('今天北京天气怎么样')
    # print(ipQuery("137.2.23.1"))
    # trans_youdao('fuck shit')
    # word_count("To fully reap the benefits of outdoor exercise, it's important to find activities that align with personal interests and fitness goals.")
    content = get_json_data('Statics/Others/essayEnglish.json')
    for i in content['essay']:
        i['totalWordCount'] = 0
        for j in i['content']:
            num = int(word_count(j["paragraph"]))
            j["wordCount"] = num
            i['totalWordCount'] += num
    write_json_data(content, 'Statics/Others/essayEnglish.json')

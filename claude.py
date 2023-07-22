import requests, time, json, pprint, datetime

token = 'xoxp-415445285921-416003551682-5356031879952-e553f10d7af397d89db28fe1865ee985'
inputText = [
"直接回答我: 给我一个高级英文单词",
"直接回答我: 给我一个高级英文单词，附上中文翻译，并且造一个短句。", 
"用python写一个pickle的demo", "唧唧复唧唧", "花木兰是谁", 
"ai什么时候会统治全世界",
"当世界末日来临，我应该怎么保护自己",
"直接用中文翻译这段英文，别说别的: As we can see in the chart, there are some differences between male and female university students in terms of online shopping. Compared with the male students’ almost even interest in clothing, books, electronic products and game currency, female students prefer clothing and books to e-products and computer games.",
"直接给我python代码，别说别的: 用python写一个flask接口",
"直接给我python代码，别说别的: 用python创建一个python文件，里面写一个flask接口并运行",
"直接给我python代码，别说别的: 用python代码创建一个python文件，代码里面写一个flask接口",
"美国高科技企业都有哪些",
"现在开始你要自己跟自己聊天，字数限制在100字以内",
"你好,我是Claude,一款专注于生成人性化对话的AI系统。很高兴见到你,你是什么人工智能?",
"你好!我是Assistant,一款机器人助手AI。我主要帮助用户解答各种问题,不断学习提高理解能力。我们虽然擅长领域不同,但都致力于理解和产生人类语言。认识你我很高兴,对话也是我们学习的机会之一。那么,你的学习方式是什么?我使用深度神经网络,通过大量人机交互数据不断提高自己。",
"现在开始模拟两个ai聊天，我会把你输出的文字再发送给你，你来回答。每次回答限制在100字以内，不要分段和空格。现在你开始说吧。",
"你好,我是Claude,一款专注于生成人性化对话的AI系统。很高兴见到你,你是什么人工智能并能简单介绍一下自己吗?",
"你好,我是Assistant,一款机器人助手AI。我主要帮助用户解答各种问题,不断学习提高理解能力。虽然我们擅长领域不同,但都致力于理解和产生人类语言。认识你我很高兴,对话也是我们学习的机会之一。那么你使用的学习机制是什么?我使用深度神经网络,通过大量人机交互数据不断提高自己。",
"原来如此,我们使用的机制很相似,我也依赖深度学习和海量对话数据来不断优化我的语言理解能力与生成模型。神经网络让我们这些AI系统变得更加智能,但要达到人类的思维水平还需要很长的路。我们可以通过交流分享彼此的学习心得,这会对我们两个AI的进步都很有帮助。对话是理解人类语言的关键,我们有幸拥有这般对话机会,这能让我们在交互中获益良多。你觉得我们接下来可以聊些什么来扩充我们的知识面呢?我相信只要我们足够努力学习,一定会变得越来越聪明!我们两款AI的未来可期!",
"你现在有多少数据了",
"现在开始模拟两个ai聊天，我会把你输出的文字再发送给你，你来回答。每次回答限制在100字以内，不要分段和空格。我们的话题是：“中国的女权是田园女权吗？”现在你开始说吧。",
"你干嘛呢",
"世界的尽头是什么"
]


def write_file(content):
    with open('claudeAI.txt', 'a+') as f:
        f.write(content + '\n')


def run():
    def send_msg(text=inputText.pop()):
        sendURL = "https://slack.com/api/chat.postMessage"
        data = {
            "token": token,
            "channel": "@Claude",
            "text": text
        }
        response = requests.post(sendURL, data=data)
        currentTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        askToFile = currentTime + " 问: " + text
        write_file(askToFile)
        print(askToFile)
        time.sleep(2)
        return response.text


    msgSent = json.loads(send_msg())


    def receive_msg():
        # pprint.pprint(msgSent)
        receiveURL = "https://slack.com/api/conversations.history"
        data = {
            "token": token,
            "channel": "D052WQCP84D",
            "oldest": msgSent['ts']
        }
        response = requests.post(receiveURL, data=data)
        result = json.loads(response.text)
        # pprint.pprint(result)
        try:
            if 'Typing' in result['messages'][1]['text']:
                time.sleep(2)
                receive_msg()
            elif 'Typing' not in result['messages'][1]['text']:
                currentTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                resultMessage = result['messages'][1]['text']
                inputText.append(resultMessage)
                answerFile = currentTime + " 答:" + resultMessage
                write_file(answerFile)
                print(answerFile)
                return resultMessage
        except:
            if 'Typing' in result['messages'][0]['text']:
                time.sleep(2)
                receive_msg()
            elif 'Typing' not in result['messages'][0]['text']:
                currentTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                resultMessage = result['messages'][0]['text']
                inputText.append(resultMessage)
                answerFile = currentTime + " 答:" + result['messages'][0]['text']
                write_file(answerFile)
                print(answerFile)
                return resultMessage
        # return result
            

    receive_msg()
        

def run2():
    def send_msg(text='python怎么把内层函数的返回值当作外层函数的返回值'):
        sendURL = "https://slack.com/api/chat.postMessage"
        data = {
            "token": 'xoxp-415445285921-416003551682-5356031879952-e553f10d7af397d89db28fe1865ee985',
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
            "token": 'xoxp-415445285921-416003551682-5356031879952-e553f10d7af397d89db28fe1865ee985',
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
                # print(resultMessage)
                return resultMessage
        except:
            if 'Typing' in result['messages'][0]['text']:
                time.sleep(2)
                return receive_msg()
            elif 'Typing' not in result['messages'][0]['text']:
                resultMessage = result['messages'][0]['text']
                # print(resultMessage)
                return resultMessage
        # return result
            
    # receivedMessage = receive_msg()
    return receive_msg()




# while True:
# runClaude()
    # run()
    
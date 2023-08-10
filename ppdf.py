import json, os
from tools import claude_ai, get_json_data, write_json_data, trans_youdao

# prompt = """
# 直接用python写一个装饰器并打印装饰器的名字，名字中间要暂停1秒，不要说别的，直接给我代码。
# """
# rawData = claudeAI(prompt)
# result = rawData.strip()
# print(result)

# prompt = """
# 直接用python调用一个叫'decorator'的装饰器(不用把它写出来，我的代码里已经有了)并装饰到'fik'这个函数里，
# 'fik'是一个打印helloworld的函数，不需要运行'fik'函数，运行一个叫做'good'的函数(不用把这个函数写出来，不需要
# 被装饰，我的代码里已经有了)。不要说别的，直接给我代码。
# """
# rawData = claudeAI(prompt)
# result = rawData.strip()
# print(result)
# # exec(result)
# with open('k.py', 'a+') as f:
#     f.write('\n\n\n' + result)
# os.system('python k.py')

trans_youdao('what the fuck')
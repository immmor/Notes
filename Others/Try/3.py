import openai

# openai.log = "debug"
openai.api_key = "sk-O7hjZCtWA6saoobUYBleIdG2b1UIdDsOJzW0HsW21qnFCMrU"
openai.api_base = "https://api.chatanywhere.com.cn/v1"



# 非流式响应
completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "来一道数学题"}])
print(completion.choices[0].message.content)

def gpt_35_api_stream(messages: list):
    try:
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=messages,
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
        messages.append(completion)  # 直接在传入参数 messages 中追加消息
        return (True, '')
    except Exception as err:
        return (False, f'OpenAI API 异常: {err}')

# if __name__ == '__main__':
    # messages = [{'role': 'user','content': '写一个考研英语作文'},]
    # gpt_35_api_stream(messages)
    # print(gpt_35_api_stream(messages))
    # print(messages[1]['content'])
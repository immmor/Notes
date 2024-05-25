from openai import OpenAI
 
client = OpenAI(
    api_key = "sk-yx36FEMDwmxD7Gby4GNZ4wjYOkXsGrhOyYKppXakcrykOHVZ",
    base_url = "https://api.moonshot.cn/v1",
)
 
completion = client.chat.completions.create(
    model = "moonshot-v1-8k",
    messages = [
        # {"role": "system", "content": "你会为用户提供安全，有帮助，准确的回答。"},
        {"role": "user", "content": "这个世界会变好吗"}
    ],
    temperature = 0.3,
)
 
print(completion.choices[0].message.content)
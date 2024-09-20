import torch
from transformers import AutoModel, AutoTokenizer
# CPU设置
device = torch.device("cpu")
# 加载模型与tokenizer
model_name_or_path = 'scutcyr/BianQue-2'
model = AutoModel.from_pretrained(model_name_or_path, trust_remote_code=True)
model.to(device)
tokenizer = AutoTokenizer.from_pretrained(model_name_or_path, trust_remote_code=True)

# 单轮对话调用模型的chat函数
user_input = "我的宝宝发烧了，怎么办？"
input_text = "病人：" + user_input + "\n医生："
response, history = model.chat(tokenizer, query=input_text, history=None, max_length=2048, num_beams=1, do_sample=True, top_p=0.75, temperature=0.95, logits_processor=None)

# 多轮对话调用模型的chat函数
# 注意：本项目使用"\n病人："和"\n医生："划分不同轮次的对话历史
# 注意：user_history比bot_history的长度多1
user_history = ['你好', '我最近失眠了']
bot_history = ['我是利用人工智能技术，结合大数据训练得到的智能医疗问答模型扁鹊，你可以向我提问。']
# 拼接对话历史
context = "\n".join([f"病人：{user_history[i]}\n医生：{bot_history[i]}" for i in range(len(bot_history))])
input_text = context + "\n病人：" + user_history[-1] + "\n医生："

response, history = model.chat(tokenizer, query=input_text, history=None, max_length=2048, num_beams=1, do_sample=True, top_p=0.75, temperature=0.95, logits_processor=None)
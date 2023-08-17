# from os import environ
# from Bard import Chatbot

# Secure_1PSID = environ.get("BARD__Secure_1PSID")
# Secure_1PSIDTS = environ.get("BARD__Secure_1PSIDTS")
# chatbot = Chatbot(Secure_1PSID, Secure_1PSIDTS)

# answer = chatbot.ask("Hello, how are you?")

# print(answer['content'])
from tools import fan, trans_google

if fan:
    trans_google("рфдфырфщ")


# from gradio_client import Client

# client = Client("http://127.0.0.1:7860/")
# result = client.predict(
# 				"你在干嘛？",	# str in 'Text' Textbox component
# 				"dian",	# str (Option from: ['dian']) in 'character' Dropdown component
# 				"简体中文",	# str (Option from: ['日本語', '简体中文', 'English', 'Mix']) in 'language' Dropdown component
# 				1,	# int | float (numeric value between 0.1 and 5) in '速度 Speed' Slider component
# 				fn_index=0
# )
# print(result)
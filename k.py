# from os import environ
# from Bard import Chatbot

# Secure_1PSID = environ.get("BARD__Secure_1PSID")
# Secure_1PSIDTS = environ.get("BARD__Secure_1PSIDTS")
# chatbot = Chatbot(Secure_1PSID, Secure_1PSIDTS)

# answer = chatbot.ask("Hello, how are you?")

# print(answer['content'])
from tools import fan, trans_google

if fan:
    trans_google("Let's go for a fuck")
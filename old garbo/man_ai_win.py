import os
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

print("\n"*200)

chatbot = ChatBot('Bill Cosby')
chatbot.set_trainer(ChatterBotCorpusTrainer)

chatbot.train(".\\cosby.json")

def log(text):
    f = open('log.txt','a')
    f.write("\n"+text)
    f.close()

print("\n"*200)
log("--Restart--")

while True:
    i = input("User: ")
    log("User: " + i)
    if i != "!":
        r = str(chatbot.get_response(i))
        print("AI: " + r)
        log("AI: " + r)
        os.system("voice.exe -t " + r)

import os
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

import rmutil

r = rmutil.util()
r.do()
print("\n"*200)

chatbot = ChatBot('Bill Cosby', trainer='chatterbot.trainers.ChatterBotCorpusTrainer')

chatbot.train("chatterbot.corpus.english")

def log(text):
    f = open('memelog.txt','a')
    f.write("\n"+text)
    f.close()

print("\n"*200)
log("--Restart--")

while True:
    i = input("User: ")
    log("User: " + i)
    if i != "!":
        r = str(chatbot.get_response(i))
        os.system("cowsay " + r)
        os.system("say " + r)
        log("AI: " + r)

import os
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

import rmutil

r = rmutil.util()
r.do()

chatbot = ChatBot('Bill Cosby', trainer='chatterbot.trainers.ChatterBotCorpusTrainer')
chatbot.train("chatterbot.corpus.english")

chatbot2 = ChatBot('Cill Bosby', trainer='chatterbot.trainers.ChatterBotCorpusTrainer')
chatbot2.train("chatterbot.corpus.english")

def log(text):
    f = open('logAI2.txt','a')
    f.write("\n"+text)
    f.close()
    os.system('cowsay "' + text +'"')
    os.system('say "' + text +'"')

print("\n"*200)
log("---Restart---")

human = input("Start: ")
log("HUMAN: " + human)
c1 = str(chatbot.get_response(human))
log("1: " + c1)
while True:
    c2 = str(chatbot2.get_response(c1))
    log("2: " + c2)
    c1 = str(chatbot.get_response(c2))
    log("1: " + c1)

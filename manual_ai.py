import os
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('Bill Cosby', trainer='chatterbot.trainers.ChatterBotCorpusTrainer')

chatbot.train("chatterbot.corpus.english")

def log(text):
    f = open('log.txt','a')
    f.write("\n"+text)
    f.close()

print("\n"*200
log("--Restart--"))

while True:
    i = input("User: ")
    log("User: " + i)
    if i != "!":
        r = str(chatbot.get_response(i))
        print("AI: " + r)
        log("AI: " + r)

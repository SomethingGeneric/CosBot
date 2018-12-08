import os
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import tweepy
from time import sleep

class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status_code):
        if status_code == 420:
            return False
        print(status_code.text)

def ret(f):
    t = open(f)
    te = t.read()
    t.close()
    return str(te)

def inc():
    f = open('count','r')
    c = int(f.read())
    f.close()
    c += 1
    f = open('count','w')
    f.write(str(c))
    return c

auth = tweepy.OAuthHandler(ret("consumer_key"), ret("consumer_secret"))
auth.set_access_token(ret("access_token"), ret("access_token_secret"))
api = tweepy.API(auth)

chatbot = ChatBot('Bill Cosby', trainer='chatterbot.trainers.ChatterBotCorpusTrainer')

chatbot.train("./cosby.json")

def log(text):
    f = open('log.txt','a')
    f.write("\n"+text)
    f.close()

print("\n"*200)
log("--Restart--")

listener = MyStreamListener()
stream = tweepy.Stream(auth = api.auth, listener=listener)
# 1071223662890618880

while True:
    mentions = api.mentions_timeline(count=1)
    for mention in mentions:
        t = str(chatbot.get_response(mention.text))
        tt = str(inc())
        print(tt)
        tweet = tt + ": " + t
        api.update_status(tweet)

#r = str(chatbot.get_response(i))

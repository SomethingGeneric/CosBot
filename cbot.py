import discord
from discord.ext import commands
import asyncio
import random
from time import sleep
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('Bill Cosby', trainer='chatterbot.trainers.ChatterBotCorpusTrainer')

chatbot.train("chatterbot.corpus.english")

bot = commands.Bot(command_prefix='&', description="ChatterBot")


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command(description="Conversation")
async def c(text):
    """Have a Conversation!"""
    await bot.say(str(chatbot.get_response(text)))

bot.run(open("cbtoken","r").readline())

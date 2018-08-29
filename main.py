import discord
import asyncio
import logging
logging.basicConfig(level=logging.INFO)
print("Bringing System Online")
print("Launching CraeBot v0.2")
crae = discord.Client()
subroutine = crae.event
sendmsg = crae.send_message
extLog = discord.Object(id="478587171373056000")

async def playStatus():
    await crae.wait_until_ready()
    await crae.change_presence(game=discord.Game(name='With the Debugger'))

@subroutine
async def on_ready():
    print("Log in successful. Logged in as " + crae.user.name +"/" + crae.user.id)
    print("======")
    print("Now accepting commands")

@subroutine
async def on_message(message):

    if message.content.startswith("!test"):
        await sendmsg(message.channel, "Test successful")

    elif message.content.startswith("Riley?"):
        await sendmsg(message.channel, "Yeah?")

    elif message.content.lower().find("log this") != -1:
        if  "external-log-requests" != str(message.channel):
            print("Logged message from " + message.author.display_name)
            print(message.content)
            await sendmsg(extLog, message.content + " - " + message.author.display_name)
            print(str(message.channel) + " to " + str(extLog))
            #   The idea here is for the server to have a channel dedicated to logging
            #   That the bot will push to, which can be handy for logging if something happened
            #   in the server, or to write a note. At the moment, it just logs the message
            #   To a channel on the bot log server, which is where the bot reports crashes and feedback.
            #   Which is where I plan to log the messages, if the server hasn't set it up for themselves.
            #   That is for future plans though.

    '''elif len(message.mentions) > 0:
        print(message.mentions)
        wheremention = message.mentions.index(str(crae.user.id))
        print("detected mention")
        for user in message.mentions:
            if message.mentions(wheremention) == crae.user.id:
                print("-----")
                print("Message Author: " + str(message.author.display_name))
                print(message.content)
            else:
                print("No mention of me")'''
                
    elif message.content.lower().find("hello there") != -1:
        if crae.user.id != message.author.id:
            await sendmsg(message.channel, "General " + str(message.author.display_name) +"!")
            print("Called " + str(message.author.display_name)+ " a general")        

    elif message.content.lower().find("hello") != -1:
        if crae.user.id != message.author.id:
            await sendmsg(message.channel, "Hello " + str(message.author.display_name) +"!")
            print("Said hello to " + str(message.author.display_name))
            
crae.loop.create_task(playStatus())

import discord
import asyncio
import logging
logging.basicConfig(level=logging.INFO)
print("Bringing System Online")
print("Launching CraeBot v0.2")
crae = discord.Client()
subroutine = crae.event
sendmsg = crae.send_message

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
    if message.content.startswith("Riley I'm finished"):
        await sendmsg(message.channel, "Command incomplete.. Please wait for next update")
        await crae.remove_roles(message.author, unfinished)

    elif message.content.startswith("!test"):
        await sendmsg(message.channel, "Test successful")

    elif message.content.startswith("Riley unfinished"):
        unfinished = discord.utils.get(Server.roles, name="unfinished")
        await crae.add_roles(message.author, unfinished)
        await sendmsg(message.channel, "Role added!")

    elif message.content.startswith("Riley?"):
        await sendmsg(message.channel, "Yeah?")

    elif message.content.startswith("Hello"):
        if crae.user.id != message.author.id:
            await sendmsg(message.channel, "Hello " + str(discord.User.name) +"!")
            
crae.loop.create_task(playStatus())
token = ""
crae.run(token)

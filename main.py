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
    await crae.change_presence(game=discord.Game(name='With Shadows'))

@subroutine
async def on_ready():
    print("Log in successful. Logged in as " + crae.user.name +"/" + crae.user.id)
    print("======")
    print("Now accepting commands")

@subroutine
async def on_message(message):
    if message.content.startswith("!finished"):
        await sendmsg(message.channel, "Command incomplete.. Please wait for next update")
        await crae.remove_roles(message.author, unfinished)

    elif message.content.startswith("!test"):
        await sendmsg(message.channel, "Test successful")

    elif message.content.startswith("!unfinished"):
        unfinished = discord.utils.get(discord.Server.roles, name="unfinished")
        await crae.add_roles(message.author, unfinished)
        await sendmsg(message.channel, "Role added!")
crae.loop.create_task(playStatus())
token = ""
crae.run(token)

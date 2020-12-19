import discord
import os
from commands import *
import importlib
import inspect

prefix = 'ch '
 
class DrPirocks(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if not(message.content.startswith(prefix)) or message.author.bot or not(message.guild):
            return

        args = message.content[len(prefix):len(message.content)].strip().split()
        command = args.pop(0).lower()
        
        await message.channel.send(command)
        await message.channel.send(args)
        
        if command == 'send':
            send.execute(message, args)


client = DrPirocks()
env = os.environ.get("BOT_TOKEN")
client.run(env)

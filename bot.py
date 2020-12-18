import discord
import os
from commands import *
from collections import deque

prefix = 'ch '

class DrPirocks(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if not(message.content.startswith(prefix)) or message.author.bot or not(message.guild):
            return

        args = message.content.replace(prefix, '').strip().split()
        command = args.pop(0).lower()

        await message.channel.send(args)
        await message.channel.send(command)

client = DrPirocks()
env = os.environ.get("BOT_TOKEN")
client.run(env)

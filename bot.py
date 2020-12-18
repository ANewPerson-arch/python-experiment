import discord
import os
from commands import *
from collections import deque

prefix = 'vb '

class DrPirocks(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if not(message.content.startswith(prefix)) or message.author.bot or not(message.guild):
            return

        args = message.content[slice(len(prefix))].strip().split()
        command = deque(args).popLeft().lower()

        message.send(command)

client = DrPirocks()
env = os.environ.get("BOT_TOKEN")
client.run(env)

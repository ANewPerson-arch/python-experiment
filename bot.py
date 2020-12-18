import discord
from commands import *
from collections import deque

commands = discord.Collection()
prefix = 'vb '

class DrPirocks(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if not(message.content.startswith(prefix)) or message.author.bot or not(message.guild):
            return

        args = message.content.slice(len(prefix)).strip().split()
        command = args.popLeft().lower()

        message.send(command)

client = DrPirocks()
client.run('token')
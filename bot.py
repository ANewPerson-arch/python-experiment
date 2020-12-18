import discord
import os
from commands import *

prefix = 'ch '

class DrPirocks(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if not(message.content.startswith(prefix)) or message.author.bot or not(message.guild):
            return

        args = message.content.replace(prefix, '').strip().split()
        command = args.pop(0).lower()
        
            module = importlib.import_module('my_package.my_module')
            my_class = getattr(module, 'MyClass')
            my_instance = my_class().execute(message,args)
            

client = DrPirocks()
env = os.environ.get("BOT_TOKEN")
client.run(env)

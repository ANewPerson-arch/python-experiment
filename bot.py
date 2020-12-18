import discord
import os
from commands import *
from modulefinder import ModuleFinder

prefix = 'ch '

class DrPirocks(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if not(message.content.startswith(prefix)) or message.author.bot or not(message.guild):
            return

        args = message.content.replace(prefix, '').strip().split()
        command = args.pop(0).lower()
        
        finder = ModuleFinder()
        try:      
            components = command.split('.')
            mod = __import__(components[0])
            for comp in components[1:]:
                mod = getattr(mod, comp)
            return mod.execute(message,args)
        except:
            return
            

client = DrPirocks()
env = os.environ.get("BOT_TOKEN")
client.run(env)

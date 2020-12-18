import discord
import os
import commands
import importlib

prefix = 'ch '
 
class DrPirocks(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if not(message.content.startswith(prefix)) or message.author.bot or not(message.guild):
            return

        args = message.content.replace(prefix, '').strip().split()
        command = args.pop(0).lower()
        
        module_object = importlib.import_module(commands)
        module_class = inspect.getmembers(module_object, inspect.isclass)[0][1]
        
        print(module_class)


client = DrPirocks()
env = os.environ.get("BOT_TOKEN")
client.run(env)

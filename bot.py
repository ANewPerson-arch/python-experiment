import discord
import os
import commands

prefix = 'ch '

class getCmd: 
    def __init__(self, module_name, class_name): 
        module = __import__(module_name) 
        my_class = module_name[class_name]
        return my_class 

class DrPirocks(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if not(message.content.startswith(prefix)) or message.author.bot or not(message.guild):
            return

        args = message.content.replace(prefix, '').strip().split()
        command = args.pop(0).lower()
        
        getCmd('commands', command).execute(message,args)
            

client = DrPirocks()
env = os.environ.get("BOT_TOKEN")
client.run(env)

import discord
import os
import commands
import pyclbr as pyr

prefix = 'ch '
 
class DrPirocks(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if not(message.content.startswith(prefix)) or message.author.bot or not(message.guild):
            return

        args = message.content.replace(prefix, '').strip().split()
        command = args.pop(0).lower()
        
        module_info = pyr.readmodule('commands')
        print(module_info)

        for item in module_info.values():
            print(item.name)
            

client = DrPirocks()
env = os.environ.get("BOT_TOKEN")
client.run(env)

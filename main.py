
#import libraries
import discord
from discord.ext import commands,tasks
import json
import os

# open config.json to read
with open('./config.json', 'r') as configFile:
    config = json.load(configFile)


# intents = discord.Intents().all()
# client = commands.Bot(command_prefix='*', intents=intents, case_insensitive=True)
class client(commands.Bot):
    def __init__(self, *args, **kwargs):
        self.command_prefix='*'
        super().__init__(
            command_prefix='*',
            intents=discord.Intents().all()
        )



#Load Extension...
async def load():
    for filename in os.listdir('/Extension'):
        if filename.endswith('.py'):
            await client.load_extension(f'cogs.{filename[:-3]}')



#Console...
@client.event
async def on_ready(self):
    print(f'{client.user} is ready')

    #Bot is say in channel when it online

    #channel = client.get_channel(1036297105666490371)
    #say in chat...
    #await channel.send(f"{client.user} \nNow Online!")

#Bot Token...
client.run(config["token"])

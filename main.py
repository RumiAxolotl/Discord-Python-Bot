
#import libraries
import discord
from discord.ext import commands,tasks
import json

# open config.json to read
with open('./config.json', 'r') as configFile:
    config = json.load(configFile)


intents = discord.Intents().all()
client = commands.Bot(command_prefix='*', intents=intents)


@client.event
async def on_ready():
    print(f'{client.user} is ready')

        

client.run(config["token"])

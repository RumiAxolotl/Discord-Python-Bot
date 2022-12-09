
#import libraries
import asyncio
import discord
from discord.ext import commands,tasks
import json
import os
# import nest_asyncio
# nest_asyncio.apply()

# open config.json to read
with open('./config.json', 'r') as configFile:
    config = json.load(configFile)


intents = discord.Intents().all()
client = commands.Bot(command_prefix='*', intents=intents, case_insensitive=True)


#Load Extension...
async def load_extension():
    for filename in os.listdir(f'./Extension'):
        if filename.endswith('.py'):
            await client.load_extension(f'Extension.{filename[:-3]}')



#Console...
@client.event
async def on_ready():
    print(f'{client.user} is ready')


# Load Extension...
async def load_extension():
    for filename in os.listdir(f'./Extension'):
        if filename.endswith('.py'):
            await client.load_extension(f'Extension.{filename[:-3]}')
asyncio.run(load_extension())


#Run Bot with Token from JSON file

client.run(config["token"])


#import libraries
import asyncio
import discord
from discord.ext import commands,tasks
import json
import os

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

    #Bot is say in channel when it online

    #channel = client.get_channel(1036297105666490371)
    #say in chat...
    #await channel.send(f"{client.user} \nNow Online!")

#Bot Token...
asyncio.run(load_extension())
client.run(config["token"])

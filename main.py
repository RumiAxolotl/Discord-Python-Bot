
#import libraries
import discord
from discord.ext import commands,tasks
import json

# open config.json to read
with open('./config.json', 'r') as configFile:
    config = json.load(configFile)


intents = discord.Intents().all()
client = commands.Bot(command_prefix='*', intents=intents)

#Console...
@client.event
async def on_ready():
    print(f'{client.user} is ready')
    channel = client.get_channel(1036297105666490371)
    #say in chat...
    await channel.send(f"{client.user} \nNow Online!")




#Bot Token...
client.run(config["token"])

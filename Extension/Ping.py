# from discord.ext.commands import Cog
# from discord.ext.commands import command
# #Ping...
# class Testping(Cog):
#     def main(self,bot):
#         self.bot = bot

#     @command(name="ping", aliases=["pong!"])
#     async def ping(self, ctx):
#         await ctx.send("Pong!")
#     # @commands.Cog(name="ping", aliases=["pong!"])
#     #     async def on_message(ctx):
#     #         await ctx.send("Pong!")


#     def setup(bot):
#         bot.add_cog(testping(bot))
# 

# async def setup(client):
#     client.add_cog(ping(client))

import discord
from discord.ext import commands

class testping(commands.Cog):
    def main(self, client):
        self.client = client

    @commands.command(name="ping", aliases=["pong!"])
    async def ping(self, ctx):
        await ctx.send("Pong")

async def setup(client):
    client.add_cog(testping(client))
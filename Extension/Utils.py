import discord
from discord.ext import commands

class Utils(commands.Cog):
    def main(self, client):
        self.client = client

    @commands.command(aliases=["pong"])
    async def ping(self, ctx):
        await ctx.send("Pong")

async def setup(client):
    await client.add_cog(Utils(client))
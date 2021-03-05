import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
import random

with open('setting.json','r',encoding='utf8')as jfile:
    jdata = json.load(jfile)

class React(Cog_Extension):

    @commands.command()
    async def pic(self, ctx):
        random_pic = random.choice(jdata['pictures'])
        pic = discord.File(random_pic)
        await ctx.send(file= pic)

    @commands.command()
    async def url_pic(self, ctx):
        url_pic = (jdata['url-pic'])
        await ctx.send(url_pic)

def setup(bot):
    bot.add_cog(React(bot))
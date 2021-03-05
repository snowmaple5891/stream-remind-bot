import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json

with open('setting.json','r',encoding='utf8')as jfile:
    jdata = json.load(jfile)

class Event(Cog_Extension):
    @commands.Cog.listener()    
    async def on_member_join(self, member):
        channel = self.bot.get_channel(int(jdata['member-alter']))
        await channel.send(f"{member} 粗現啦!")

    @commands.Cog.listener()    
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(int(jdata['member-alter']))
        await channel.send(f"{member} 下去啦!")

    @commands.Cog.listener()    
    async def on_message(self, msg):
        keywords = ['哭阿','笑死']
        if msg.content in keywords:
            await msg.channel.send('抓到口頭禪!')

def setup(bot):
    bot.add_cog(Event(bot))
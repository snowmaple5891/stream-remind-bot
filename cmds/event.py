import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
import datetime

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
        keywords = ['哭阿','笑死','孤兒']
        if msg.content in keywords:
            if msg.content == "孤兒":
                await msg.channel.send('你才孤兒')
            else:
                await msg.channel.send('抓到口頭禪!')

    @commands.command()
    async def em(self, ctx):
        embed=discord.Embed(title="twitter post", url="https://twitter.com/tamg_/status/1367780521443352576", description="nice pic!", color=0xbfa3ff, timestamp=datetime.datetime.now())
        embed.set_author(name="@tamg_", url="https://twitter.com/tamg_", icon_url="https://pbs.twimg.com/profile_images/1362967300450656261/CtPPlktp_400x400.jpg")
        embed.set_thumbnail(url="https://pbs.twimg.com/profile_images/1336662989705936901/EG4zxSGo_400x400.jpg")
        embed.add_field(name="pic", value="哭阿不會弄，明天回家繼續", inline=False)
        embed.set_footer(text="此為UTC時間--->")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Event(bot))
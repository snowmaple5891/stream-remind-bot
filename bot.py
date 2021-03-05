import discord
from discord.ext import commands
import json

with open('setting.json','r',encoding='utf8')as jfile:
    jdata = json.load(jfile)

intents = discord.Intents.all()

bot = commands.Bot(command_prefix = '!', intents=intents)

@bot.event
async def on_ready():
    print("bot is online")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(int(jdata['member-alter']))
    await channel.send(f"{member} 粗現啦!")

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(int(jdata['member-alter']))
    await channel.send(f"{member} 下去啦!")

bot.run(jdata['TOKEN'])
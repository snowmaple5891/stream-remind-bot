import discord
from discord.ext import commands

intents = discord.Intents.all()

bot = commands.Bot(command_prefix = '!', intents=intents)

@bot.event
async def on_ready():
    print("bot is online")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(817082646777298954)
    await channel.send(f"{member} 粗現啦!")

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(817082646777298954)
    await channel.send(f"{member} 下去啦!")

bot.run('ODE3MDQxOTk1MDg0MDcwOTUz.YEDvpw.XitM-fG5nqZe0aWVy0w2MliPLmc')
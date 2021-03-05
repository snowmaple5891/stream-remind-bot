import discord
from discord.ext import commands
import json
import random
import os

with open('setting.json','r',encoding='utf8')as jfile:
    jdata = json.load(jfile)

intents = discord.Intents.all()

bot = commands.Bot(command_prefix = '!', intents=intents)

@bot.event
async def on_ready():
    print("bot is online")

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'loaded {extension} done.')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'unloaded {extension} done.')

@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'reloaded {extension} done.')

for filename in os.listdir('./cmds'):
    if filename.endswith(".py"):
        bot.load_extension(f'cmds.{filename[:-3]}')
    
if __name__ == "__main__":
    bot.run(jdata['TOKEN'])
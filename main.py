import os
import random 
import discord
from dotenv import load_dotenv
from discord.ext import commands


load_dotenv()
TOKEN = os.getenv('TOKEN')


intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')



@bot.command()
async def hello(ctx:any)->str:
    await ctx.send("Hello!")

@bot.command()
async def tableflip(ctx:any)->str:
    await ctx.send("(╯°□°）╯︵ ┻━┻")

@bot.command()
async def unflip(ctx:any)->str:
    await ctx.send("┬─┬﻿ ノ( ゜-゜ノ)")

@bot.command()
async def tableshrug(ctx:any)->str:
    await ctx.send("¯\_(ツ)_/¯")

@bot.command()
async def ping(ctx:any)->str:
    await ctx.send("Pong!")

@bot.command()
async def pong(ctx:any)->str:
    print(type(ctx))
    await ctx.send("Ping!")

@bot.command()
async def coinflip(ctx:any)->str:
    await ctx.send(random.choice(["Heads", "Tails"]))

def main()->None:
    bot.run(TOKEN)


if __name__ == '__main__':
    main()
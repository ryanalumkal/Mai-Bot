import os
import random 
import discord
from discord import app_commands
from dotenv import load_dotenv
from discord.ext import commands
from keep_alive import keep_alive

load_dotenv()
try:
    TOKEN = os.environ['TOKEN']
except KeyError:
    print("Error")
finally:
    TOKEN = os.getenv('TOKEN')



intents = discord.Intents.all()
intents.messages = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    synced = await bot.tree.sync()
    print(f'{bot.user} has connected to Discord!')

@bot.tree.command(name="idk")
async def idk(message: discord.Interaction):
    await message.response.send_message("I Don't Know Either!")

@bot.tree.command(name="hello")
async def hello(message: discord.Interaction):
    await message.response.send_message("Hello!")

@bot.tree.command(name="tableflip")
async def tableflip(message: discord.Interaction):
    await message.response.send_message("(╯°□°）╯︵ ┻━┻")

@bot.tree.command(name="unflip")
async def unflip(message: discord.Interaction):
    await message.response.send_message("┬─┬﻿ ノ( ゜-゜ノ)")

@bot.tree.command(name="tableshrug")
async def tableshrug(message: discord.Interaction):
    await message.response.send_message("¯\_(ツ)_/¯")

@bot.tree.command(name="ping")
async def ping(message: discord.Interaction):
    await message.response.send_message("Pong!")

@bot.tree.command(name="pong")
async def pong(message: discord.Interaction):
    await message.response.send_message("Ping!")

@bot.tree.command(name="coinflip")
async def coinflip(message: discord.Interaction):
    await message.response.send_message(random.choice(["Heads", "Tails"]))

def main()->None:
    keep_alive()
    bot.run(TOKEN)


if __name__ == '__main__':
    main()
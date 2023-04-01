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
async def hello(ctx):
    await ctx.send("Hello!")


def main():
    bot.run(TOKEN)


if __name__ == '__main__':
    main()
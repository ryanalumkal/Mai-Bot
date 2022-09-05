
import os
import discord 
from discord.ext import commands, tasks



client = discord.Client()

bot = commands.Bot(command_prefix= '!')

@client.event
async def on_ready():
    print(f' {client.user} is online!')
    
@bot.command 
async def hello(ctx, arg):
    await ctx.send(arg)
"""
@client.event
async def on_message(message):
    if message.author == client.user:
        return


USE THIS:
https://discordpy.readthedocs.io/en/stable/ext/commands/commands.html 
    
    
    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')
"""
if __name__ == '__main__':
    client.run('OTk0NzYwODczNDU1Mzk0ODU3.GJfoH1.J4gNv6PFzlgSloBEek_4kw7WMhqxhl28kzsJNE')
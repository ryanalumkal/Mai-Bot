
import os
import discord 
from discord.ext import commands, tasks



client = discord.Client()



@client.event
async def on_ready():
    print(f' {client.user} is online!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')
  
if __name__ == '__main__':
    client.run('OTk0NzYwODczNDU1Mzk0ODU3.GJfoH1.J4gNv6PFzlgSloBEek_4kw7WMhqxhl28kzsJNE')
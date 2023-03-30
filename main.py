
import os
import discord 
from discord.ext import commands, tasks
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.messages = True

client = discord.Client(intents=intents)

ClientID = os.getenv('ClientID')

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    #if message.author == client.user:
        #return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')

if __name__ == '__main__':
    client.run(ClientID)
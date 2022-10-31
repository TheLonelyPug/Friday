import discord
import os
import aiocron
from discord.ext import commands
from dotenv import load_dotenv

# credentials
load_dotenv('.env')

# define client
client = discord.Client()

# connecting
@client.event
async def on_ready():
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    print(f'{client.user} has connected to Discord!')
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

# the useless function
ID = 1035664564404101142

@aiocron.crontab('*0 12 * * FRI')
async def cronjob1():
    channel = client.get_channel(ID)
    await channel.send(file=discord.File('friday.mp4'))
"""     print('Ignore this debugging message') """

# bot token
client.run(os.getenv('token'))
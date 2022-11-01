import discord
import os
import aiocron
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
ID = <Channel ID>

@aiocron.crontab('*/1 * * * *')
async def cronjob1():
    channel = client.get_channel(ID)
    await channel.send(file=discord.File('friday.mp4'))
    # print('Ignore this debugging message')

# bot token
client.run(os.getenv('token'))
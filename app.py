import discord
import time
import asyncio

client = discord.Client()

token = process.env.TOKEN
pings = ['!d bump', 'dc!bump']
channelID = 709112418684371015

async def ping():
    await client.wait_until_ready()
    counter = 0
    channel = client.get_channel(id=channelID)
    while not client.is_closed():
        counter += 1
        for str in pings:
            await channel.send(str)
        await asyncio.sleep(7201)

@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))
    client.loop.create_task(ping())

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('_info'):
        await message.channel.send('hi')

client.run(token)

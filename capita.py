import discord
import asyncio
import random
import pickle
import os
import json
import config as cfg

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!car'):
        await client.send_message(message.channel, 'I\'m in me mums caaar. Broom, Broom. https://www.youtube.com/watch?v=LWVTsHNQIiU')
    elif message.content.startswith('!flip'):
        flip = random.choice(['Heads' , 'Tails'])
        await client.send_message(message.channel, flip)
    elif message.content.startswith('!quote'):
        await client.send_message(message.channel, '931. <@neutral> fake quotes ')
    elif message.content.startswith('!friday'):
    	await client.change_presence(game=discord.Game(name='Friday, Friday'))
    elif message.content.startswith('!clear'):
    	await client.change_presence(game=discord.Game(name=''))

client.run(cfg.auth['token'])

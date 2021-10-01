import discord
from discord.ext import commands
import requests
import os
from datetime import datetime

bot = commands.Bot(command_prefix = '%')

@bot.event
async def on_ready():
    print('Bot works!')

@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {bot.latency * 1000}ms')

@bot.command()
async def cutify(ctx, *, animal):
    if animal == 'dog':
        r = requests.get('https://dog.ceo/api/breeds/image/random')
        data = r.json()
        url = requests.get(data['message'])
        with open('temp.png','wb') as f:
            f.write(url.content)
        await ctx.send(file=discord.File('temp.png'))    
        os.remove('temp.png')

    elif animal == 'cat':
        ts = str(datetime.now())
        r = requests.get('http://thecatapi.com/api/images/get?format=src&type=gif&timestamp=' + ts)
        with open('temp.gif','wb') as f:
            f.write(r.content)
        await ctx.send(file=discord.File('temp.gif'))    
        os.remove('temp.gif')

    else:       
        await ctx.send(f'Animal is: {animal}. Sadly, I do not support those animals yet :(')

bot.run('ENTER YOUR TOKEN HERE')

import requests
import discord
from discord.ext import commands, tasks
import random



client = commands.Bot(command_prefix='!')


@client.event
async def on_ready() :
    print('Katter is ready.')
    await client.change_presence(activity=discord.Game(name="cats"))


@client.command()
async def cat(ctx) :
    url = "https://api.thecatapi.com/v1/images/search"
    headers = {'x-api-key' : "key"} # replace this with your api key
    response = requests.request("GET", url, headers=headers)
    data = response.json()
    urlpic = data[0]["url"]

    cat = discord.Embed(title="Cat")
    cat.set_image(url=urlpic)
    await ctx.send(embed=cat)
    
    client.run('token') # replace this with your discord bot token

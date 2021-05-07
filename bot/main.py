import os
import discord
#from firebase import firebase
import random
import time
import math
from discord.ext import commands

client = discord.Client()
token = os.getenv("DISCORD_BOT_TOKEN")
bot = commands.Bot(command_prefix="!")
@client.event
async def on_message(message):

    if message.content.startswith("commands"):
        await message.channel.send("31, 5v5, gulemem, helikopter,topla,cikar,bol,carp,karekok")

    if message.content.startswith("31"):
        await message.channel.send("hahahaha")
        return 
    
    if message.content.startswith("mestan") or message.content.startswith("Mestan") or message.content.startswith("MESTAN"):
        await message.channel.send("Mesto açılma artık")
        return 
        
    c = 0
    for x in message.content:
        c += 1
        if x == "+":
            a = message.content[0:c-1]
            b = message.content[c:]
            if int(a) + int(b) == 31:
                await message.channel.send("cok iyi saka kanka")
                return

        elif x == "-":
            a = message.content[0:c-1]
            b = message.content[c:]
            if int(a) - int(b) == 31:
                await message.channel.send("cok iyi saka kanka valla")
                return

        elif x == "*":
            a = message.content[0:c-1]
            b = message.content[c:]
            if int(a) * int(b) == 31:
                await message.channel.send("cok iyi saka kanka güzel çarpma tebrik ederim")
                return

        elif x == "/":
            a = message.content[0:c-1]
            b = message.content[c:]
            if int(a) / int(b) == 31:
                await message.channel.send("cok iyi saka kanka güzel bölme işlemi tebrik ederim")
                return

        elif x == ":":
            a = message.content[0:c-1]
            b = message.content[c:]
            if int(a) / int(b) == 31:
                await message.channel.send("cok iyi saka kanka en son bakkalda gördüm : bu işareti ")
                return
                

    if "31" in message.content:
        await message.channel.send("gizli saka")

    if message.content.startswith("5v5"):
                    channel = message.channel
                    await channel.send("yukarıyı oyla")
                    emoji = "\N{THUMBS UP SIGN}"
                    emoji2 = "\N{THUMBS DOWN SIGN}"
                    # or "\U0001f44d" or "👍"
                    await message.add_reaction(emoji)
                    await message.add_reaction(emoji2)



    if message.content.startswith("gülemem"):
        await message.channel.send("Gulemem kanka Gulemem s nin yanına j gelmeyince Gulemem")
    
    if message.content.startswith("helikopter"):
        await message.channel.send("pat pat")
        return
    
    if message.content.startswith("salam alaykum"):
        await message.channel.send("aleykum salam")
        
    @bot.command()
    async def test(ctx, arg):
        await ctx.send(arg)



def sub(x:float,y: float):
    return x-y

def add(x:float,y: float):
    return x+y

def div(x:float,y:float):
    return x/y

def sqrt(x:float):
    return math.sqrt((x))

def multi(x:float,y:float):
    return x*y



@commands.command()
async def topla(ctx,x:float,y:float):
    res=add(x,y)
    await ctx.send(res)

@commands.command()
async def cikar(ctx,x:float,y:float):
    res=sub(x,y)
    await ctx.send(res)

@commands.command()
async def bol(ctx,x:float,y:float):
    res=div(x,y)
    await ctx.send(res)

@commands.command()
async def carp(ctx,x:float,y:float):
    res=multi(x, y)
    await ctx.send(res)

@commands.command()
async def karekok(ctx,x:float):
    res=sqrt(x)
    await ctx.send(res)



client.run(token)

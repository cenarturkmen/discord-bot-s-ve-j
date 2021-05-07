import os
import discord
#from firebase import firebase
import random
import time
import math
from discord.ext import commands

client = discord.Client()
token = os.getenv("DISCORD_BOT_TOKEN")


"""deneme = firebase.FirebaseApplication("https://svej-d01df-default-rtdb.europe-west1.firebasedatabase.app", None)
query = deneme.get("/deneme", "caner")
print(query)
deneme.put("/deneme", "caner", 31)
query = deneme.get("/deneme", "caner")
print(query)"""

####################################################

"""duelist1= "None"
duelist2= "None"

deneme.put("/deneme", "emre", 3)
def changeDuelistScore(duelist, k):
    query = deneme.get("/deneme", str(duelist))
    if deneme.get("/deneme", str(duelist)):
        deneme.put("/deneme", str(duelist), query+k)
    else:
        deneme.put("/deneme", {str(duelist):0})
        deneme.put("/deneme", str(duelist), query+k)


def setduelist1(duelist):
    global duelist1
    duelist1= duelist
    return duelist1

def setduelist2(duelist):
    global duelist2
    duelist2= duelist
    return duelist2
"""
@client.event
async def on_message(message):
#############################################################################
    """if message.content.startswith("2Duel me"): #Duel me function
        global duelBit, duelist1 #duelBit defines if duel is active
        if duelist1 == "None":
            setduelist1(message.author)
            duelBit= True
            await message.channel.send("Rakip Bekleniyor")
        else:
            await message.channel.send("Baska Duello Aktif") 

    if message.content.startswith("2Accepted") and duelBit== True and duelist1 != message.author: #Duel accepted function
        global duelist2
        if duelist2 == "None":
            setduelist2(message.author)
            await message.channel.send(str(duelist1)+" vs "+str(duelist2))
            roll1= random.randint(0,6) #roll1
            roll2= random.randint(0,6) #roll2
            time.sleep(2)
            await message.channel.send(str(duelist1)+" rolls "+str(roll1))
            time.sleep(2)
            await message.channel.send(str(duelist2)+" rolls "+str(roll2))
            time.sleep(1)
        if roll1>roll2:#duelist1 won
            await message.channel.send("Winner is:"+str(duelist1))
            changeDuelistScore(duelist1, +1)
            changeDuelistScore(duelist2, -1)
        if roll2>roll1:#duelist2 won
            await message.channel.send("Winner is: "+str(duelist2))
            changeDuelistScore(duelist2, +1)
            changeDuelistScore(duelist1, -1)
        if roll1==roll2:
            await message.channel.send("Draw ")
        duelBit= False
        duelist1= "None" #clear duelists
        duelist2= "None" #clear duelists
        return duelist1,duelist2
    else:
        await message.channel.send("Duello onceden kabul edildi")
        
    if message.content.startswith("Total Score"):
        x= message.author
        n= 0
        while n<100:
            if duelistDatabase[n]== x:
                await message.channel.send("Score is: "+str(scoreDatabase[n]))
                break
            if n== 99:
                await message.channel.send("Score is: 0")
                break
            n= n+1"""
###############################################

    if message.content.startswith("!commands"):
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

import os
import discord

client = discord.Client()
token = os.getenv("DISCORD_BOT_TOKEN")

@client.event
async def on_message(message):

    if message.content.startswith('31'):
        await message.channel.send("hahahaha")
        return 
    
    if message.content.startswith("mestan") or message.content.startswith("Mestan") or message.content.startswith("MESTAN"):
        await message.channel.send("mestan açılma artık")
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
        return

    if message.content.startswith("5v5"):
        await message.channel.send("ben oynarim kanka yaz beni")
        await message.channel.send(reaction.embeds[0])
        return 
    
    if message.content.startswith("gülemem"):
        await message.channel.send("gülemem kanka gülemem s'nin yanına j gelmeyince gülemem")
        return
    
    if message.content.startswith("helikopter"):
        await message.channel.send("pat pat")
        return

client.run(token)

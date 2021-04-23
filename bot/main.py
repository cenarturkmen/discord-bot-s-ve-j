import os
import discord

client = discord.Client()
token = open("token.txt", "r")
print(token)
@client.event
async def on_message(message):

    if message.content.startswith('31'):
      await message.channel.send("hahahaha")
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
                await message.channel.send("cok iyi saka kanka ama eksilisi")
                return

        elif x == "*":
            a = message.content[0:c-1]
            b = message.content[c:]
            if int(a) * int(b) == 31:
                await message.channel.send("cok iyi saka kanka ama carpili")
                return

        elif x == "/":
            a = message.content[0:c-1]
            b = message.content[c:]
            if int(a) / int(b) == 31:
                await message.channel.send("cok iyi saka kanka ama bolulu")
                return

        elif x == ":":
            a = message.content[0:c-1]
            b = message.content[c:]
            if int(a) / int(b) == 31:
                await message.channel.send("cok iyi saka kanka ama bolulu")
                return

    if "31" in message.content:
        await message.channel.send("gizli saka")
        return

    elif message.content.startswith("5v5"):
        await message.channel.send("ben oynarim kanka")
        return 
        
client.run("ODM0OTMwNTU2Mzk1NDU0NTA1.YIIDrA.4rfmtbF6qrgyY3TKA5DEJPQcUmQ")

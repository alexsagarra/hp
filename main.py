import discord
from discord.ext import commands

import os
from dotenv import load_dotenv

from hpapi import Hp
from pprint import pprint as pp

load_dotenv()

DISCORD_APP_TOKEN = os.getenv("DISCORD_APP_TOKEN")
print(f"DISCORD_APP_TOKEN {DISCORD_APP_TOKEN}")


hp = Hp()

# You define the necessary intents
intents = discord.Intents.default()
intents.messages = True  # For example, this line enable the message content intent
intents.typing = False
intents.presences = False
intents.message_content = True

# And don't forget to include inside your commands.
# bot = commands.Bot(command_prefix='!', intents=intents)
client = commands.Bot(intents=intents, command_prefix="$")  # "Import" the intents
# bot = commands.Bot(command_prefix=".", intents=intents) # "Import" the intents


@client.event
async def on_ready():
    print(f"Bot ist eingeloggt als {client.user}")

    # CREATES A COUNTER TO KEEP TRACK OF HOW MANY GUILDS / SERVERS THE BOT IS CONNECTED TO.
    guild_count = 0

    # LOOPS THROUGH ALL THE GUILD / SERVERS THAT THE BOT IS ASSOCIATED WITH.
    for guild in client.guilds:
        # PRINT THE SERVER'S ID AND NAME.
        print(f"- {guild.id} (name: {guild.name})")

        # INCREMENTS THE GUILD COUNTER.
        guild_count = guild_count + 1

    # PRINTS HOW MANY GUILDS / SERVERS THE BOT IS IN.
    print("HP DiscordBot is in " + str(guild_count) + " guilds.")


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f"Hi {member.name}, welcome to my Discord server!")


# @client.event
# async def on_message(message):
#     """message"""
#     if "hp" in message.content.lower():
#         await message.channel.send("Harry Potter API 🎈🎉")


@client.event
async def on_message(message: discord.Message):
    """message"""
 
    if message.author == client.user:
        return
    
    print(f"Incomming: {message.author.name}, {message.channel.name}, {message.content}")


    if "ok" in message.content.lower():
        print("ok")
        await message.channel.send("Harry Potter API 🎈")
        return
    
    elif "characters" in message.content.lower():
        print("characters")
        characters = hp.get_characters()
        pp(characters)
        for character in characters:
           await message.channel.send(f"name: {character['actor']} id: {character['id']}") 
        # await message.channel.send(characters)
        return
    
    elif "character" in message.content.lower():
        print("character")
        character = hp.get_character()
        pp(character)
        for k,v in character.items():
           await message.channel.send(f"{k} {v}") 
        # await message.channel.send(characters)
        return

    else:
        await message.channel.send("....")
        print("else")
        return


@client.command(name="characters")
async def getCharacters(ctx):

    await ctx.send(characters)


@client.command(name="character")
async def getCharacter(ctx, character):
    service = "characters/"
    response = requests.get(api_url + service, params={})

    if response.status_code == 200:
        data = response.json()
        await ctx.send(f"Daten für {character}: {data}")
    else:
        await ctx.send("Charakter nicht gefunden")


client.run(DISCORD_APP_TOKEN)  # Discord-Bot-Token via .env Datei

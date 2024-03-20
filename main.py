import discord
from discord.ext import commands
import requests
import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_APP_TOKEN = os.getenv('DISCORD_APP_TOKEN')
print(f"DISCORD_APP_TOKEN {DISCORD_APP_TOKEN}")


# You define the necessary intents
intents = discord.Intents.default()
intents.messages = True  # For example, this line enable the message content intent

# And don't forget to include inside your commands.
# bot = commands.Bot(command_prefix='!', intents=intents)
bot = commands.Bot(command_prefix=".", intents=intents) # "Import" the intents


api_url = "https://hp-api.onrender.com/api/"

@bot.event
async def on_ready():
    print(f'Bot ist eingeloggt als {bot.user}')

    # CREATES A COUNTER TO KEEP TRACK OF HOW MANY GUILDS / SERVERS THE BOT IS CONNECTED TO.
    guild_count = 0

    # LOOPS THROUGH ALL THE GUILD / SERVERS THAT THE BOT IS ASSOCIATED WITH.
    for guild in bot.guilds:
        # PRINT THE SERVER'S ID AND NAME.
        print(f"- {guild.id} (name: {guild.name})")

        # INCREMENTS THE GUILD COUNTER.
        guild_count = guild_count + 1

    # PRINTS HOW MANY GUILDS / SERVERS THE BOT IS IN.
    print("SampleDiscordBot is in " + str(guild_count) + " guilds.")

@bot.event
async def on_message(message):
	# CHECKS IF THE MESSAGE THAT WAS SENT IS EQUAL TO "HELLO".
	if message.content == "hello":
		# SENDS BACK A MESSAGE TO THE CHANNEL.
		await message.channel.send("hey dirtbag")
                
@bot.event
async def on_ready():

    print(f'Bot ist eingeloggt als {bot.user}')

    # for guild in bot.guilds:
    #     if guild.name == GUILD:
    #         break

    print(
        f'{bot.user} is connected to the following guild:\n'
        #f'{guild.name}(id: {guild.id})'
    )

@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@bot.event
async def on_message(message):
    if 'hp' in message.content.lower():
        await message.channel.send('Harry Potter API 🎈🎉')


@bot.command()
async def getCharacters(ctx):
    service = 'characters/'
    #api_key = 'your_api_key_here'  # Hier musst du deinen eigenen API-Schlüssel einfügen wenn benötigt
    #response = requests.get(api_url, params={'key': api_key})

    response = requests.get(api_url+service, params={})

    if response.status_code == 200:
        data = response.json()
        await ctx.send(f'Daten für {character}: {data}')
    else:
        await ctx.send('Charakter nicht gefunden')

@bot.command("hello")
async def getCharacter(ctx, character):
    service = 'characters/'
    response = requests.get(api_url+service, params={})

    if response.status_code == 200:
        data = response.json()
        await ctx.send(f'Daten für {character}: {data}')
    else:
        await ctx.send('Charakter nicht gefunden')

bot.run(DISCORD_APP_TOKEN)  # Discord-Bot-Token via .env Datei

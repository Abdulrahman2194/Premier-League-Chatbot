import os
from dotenv import load_dotenv
import discord


load_dotenv()
discord_token = os.getenv("DISCORD_TOKEN")
football_api_key = os.getenv("FOOTBALL_API_KEY")


intents=discord.Intents.default()
intents.message_content=True


client=discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"{client.user} is online")



@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!hello"):
        await message.channel.send("⚽ Premier League bot here.")



client.run(discord_token)
import os
from dotenv import load_dotenv
import discord
import requests


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
    if message.content.startswith("!table"):
        table=get_table()
        await message.channel.send(table)





def get_table():
    headers = {
        "X-Auth-Token": football_api_key
    }
    response = requests.get("https://api.football-data.org/v4/competitions/PL/standings", headers=headers)
    data = response.json()
    lines = []
    for team in data["standings"][0]["table"]:
        team_name = team["team"]["name"]
        team_position = team["position"]
        team_played = team["playedGames"]
        team_points = team["points"]

        lines.append(f"{team_position}. {team_name} - Played: {team_played}, Points: {team_points}")
    return "\n".join(lines)



client.run(discord_token)
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

    if message.content.startswith("!topscorers"):
        top_scorers=get_top_scorers()
        await message.channel.send(top_scorers)





def get_table():
    headers = {
        "X-Auth-Token": football_api_key
    }
    response = requests.get("https://api.football-data.org/v4/competitions/PL/standings", headers=headers)
    data = response.json()
    lines = []
    for team in data["standings"][0]["table"]:
        team_name = team["team"]["shortName"]
        team_position = team["position"]
        team_played = team["playedGames"]
        team_points = team["points"]

        lines.append(f"{team_position}. {team_name} - Played: {team_played}, Points: {team_points}")
    return "\n".join(lines)

def get_top_scorers():
    headers={
        "X-Auth-Token": football_api_key
    }
    response=requests.get("https://api.football-data.org/v4/competitions/PL/scorers", headers=headers)
    data=response.json()
    lines=[]
    for scorer in data["scorers"]:
        player_name=scorer["player"]["name"]
        team_name=scorer["team"]["name"]
        goals=scorer["goals"]

        lines.append(f"{player_name} ({team_name}) - Goals: {goals}")
    return "\n".join(lines)

client.run(discord_token)
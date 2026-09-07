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

    if message.content.startswith("!form"):
        split=message.content.split("!form ")
        if len(split) < 2:
            await message.channel.send("Please provide a team name after !form command.")
            return
        team_name=split[1]
        form=get_form(team_name)
        await message.channel.send(form)

    if message.content.startswith("!next"):
        split=message.content.split("!next ")
        if len(split) < 2:
            await message.channel.send("Please provide a team name after !next command.")
            return
        team_name=split[1]
        next_match=get_next_match(team_name)
        await message.channel.send(next_match)
        





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

def get_form(team_name):
    headers={
        "X-Auth-Token": football_api_key
    }
    response=requests.get("https://api.football-data.org/v4/competitions/PL/standings", headers=headers)
    data=response.json()

    for team in data["standings"][0]["table"]:
        if team["team"]["shortName"].lower() == team_name.lower():
            form = team["form"]
            if form is None:
                return f"{team_name} has no recent form data available."
            
            return f"{team_name} recent form: {form}"

    return f"Team {team_name} not found in the Premier League standings recheck !table."

def get_next_match(team_name):
    headers = {
        "X-Auth-Token": football_api_key
    }
    
    standings_response = requests.get("https://api.football-data.org/v4/competitions/PL/standings", headers=headers)
    standings_data = standings_response.json()
    
    for team in standings_data["standings"][0]["table"]:
        if team["team"]["shortName"].lower() == team_name.lower():
            team_id = team["team"]["id"]
            
            matches_response = requests.get(f"https://api.football-data.org/v4/teams/{team_id}/matches?status=SCHEDULED", headers=headers)
            matches_data = matches_response.json()
            
            if len(matches_data["matches"]) == 0:
                return f"{team_name} has no upcoming matches."
            
            next_match = matches_data["matches"][0]
            
            
            if next_match["homeTeam"]["id"] == team_id:
                opponent = next_match["awayTeam"]["name"]
            else:
                opponent = next_match["homeTeam"]["name"]
                
            match_date = next_match["utcDate"]
            
            return f"{team_name} next match: vs {opponent} on {match_date}"

    return f"Team '{team_name}' not found."

client.run(discord_token)
import requests
import os
from dotenv import load_dotenv


load_dotenv()
discord_token = os.getenv("DISCORD_TOKEN")
football_api_key = os.getenv("FOOTBALL_API_KEY")






headers = {
    "X-Auth-Token": football_api_key
}

response = requests.get("https://api.football-data.org/v4/competitions/PL/standings", headers=headers)
data=response.json()



for team in data["standings"][0]["table"]:
    team_name = team["team"]["name"]
    team_position = team["position"]
    team_played = team["playedGames"]
    team_points=team["points"]

    print(f"{team_position}. {team_name} - Played: {team_played}, Points: {team_points}")
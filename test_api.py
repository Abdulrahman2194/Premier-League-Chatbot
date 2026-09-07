import requests
import os
from dotenv import load_dotenv


load_dotenv()
discord_token = os.getenv("DISCORD_TOKEN")
football_api_key = os.getenv("FOOTBALL_API_KEY")






headers = {
    "X-Auth-Token": football_api_key
}

response = requests.get("https://api.football-data.org/v4/teams/57/matches?status=SCHEDULED", headers=headers)
data=response.json()

print(len(data["matches"]))
print(data["matches"][0].keys())



for match in data["matches"][:3]:
    print(match["utcDate"])
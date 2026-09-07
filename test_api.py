import requests
import os
from dotenv import load_dotenv


load_dotenv()
discord_token = os.getenv("DISCORD_TOKEN")
football_api_key = os.getenv("FOOTBALL_API_KEY")






headers = {
    "X-Auth-Token": football_api_key
}

response = requests.get("https://api.football-data.org/v4/competitions/PL/scorers", headers=headers)
data=response.json()


print(data["scorers"][0]["player"].keys())
print(data["count"])
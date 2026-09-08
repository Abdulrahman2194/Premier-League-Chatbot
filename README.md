# Premier League Discord Bot

A Discord bot that answers Premier League questions using live data from the football-data.org API.

## Commands

| Command | What it does |
|---|---|
| `!hello` | Confirms the bot is online |
| `!table` | Current Premier League standings — position, games played, points |
| `!topscorers` | Top 10 goalscorers with their club and goal count |
| `!form <team>` | Recent form for a team, e.g. `!form Arsenal` |
| `!next <team>` | Next scheduled fixture for a team, e.g. `!next Chelsea` |

Team names should match the short names shown in `!table` (e.g. `Man City`, not `Manchester City FC`). Matching is case-insensitive.

## Requirements

- Python 3
- discord.py
- requests
- python-dotenv

## You will need

- **A Discord bot token** — create an application at https://discord.com/developers/applications, add a bot, and enable the **Message Content Intent** under the Bot tab.
- **A football-data.org API key** — free tier available at https://www.football-data.org

## Setup

```
git clone https://github.com/Abdulrahman2194/Premier-League-Chatbot.git
cd Premier-League-Chatbot
py -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Then create a `.env` file in the project root:

```
DISCORD_TOKEN=your_discord_bot_token
FOOTBALL_API_KEY=your_football_data_api_key
```

The `.env` file is gitignored and must never be committed.

## Usage

```
python bot.py
```

The bot stays running and listens for commands until stopped with Ctrl+C.

## Notes

- The API's `form` field is empty until teams have played around five matches, so early in a season `!form` reports that no form data is available yet rather than showing nothing.
- `!next` returns the next fixture across **all** competitions, not just the Premier League — so it may show a Champions League or cup match.
- All API calls go through a single `fetch_api()` helper that handles non-200 responses and network errors, so a failed request produces a friendly message instead of a silent crash.
- The free tier of football-data.org is limited to 10 requests per minute.

## Possible next steps

- Format kickoff times as readable dates instead of raw ISO timestamps
- Render `!table` as a monospaced block so columns align
- Add `!results` for recent match results
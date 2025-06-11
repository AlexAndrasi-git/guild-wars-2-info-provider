Guild Wars 2 API Data Fetcher

In this project, we use the requests library to fetch general data from the Guild Wars 2 MMORPG Game open API. The project uses an existing player's Bearer token to retrieve information about some of the the player's progress and compares it with general game data.

This project verifies and tracks:
- Daily Quests: Fetches and tracks the current daily quests in the game.
- World Boss Progress: Monitors the progress of world boss kills across the game world.
- Gem/Coin Economy: Provides general information about the in-game economy, including Gem-to-Coin conversion rates.

Requirements
Python 3.x
requests library (Install via pip install requests)

Usage: To get the current meta team compositions, you can trigger it manually via the workflow_dispatch event, but by default, GitHub Actions runs this script automatically.

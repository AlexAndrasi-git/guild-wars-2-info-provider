import requests
import os

# General Endpoints
def get_daily_world_boss_request():
    return requests.get("https://api.guildwars2.com/v2/worldbosses")

def get_daily_crafting_request():
    return requests.get("https://api.guildwars2.com/v2/dailycrafting")

def get_daily_chest_request():
    return requests.get("https://api.guildwars2.com/v2/mapchests")


# Account Related Endpoints
def get_titles_of_specific_account():
    user_token = os.getenv("BEARER_TOKEN")
    return requests.get("https://api.guildwars2.com/v2/account/titles", headers={'Authorization': f'Bearer {user_token}'})


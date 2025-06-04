import requests
from config import THIRI_BEARER_TOKEN

# General Endpoints
def get_daily_world_boss_request():
    return requests.get("https://api.guildwars2.com/v2/worldbosses")

def get_daily_crafting_request():
    return requests.get("https://api.guildwars2.com/v2/dailycrafting")

def get_daily_chest_request():
    return requests.get("https://api.guildwars2.com/v2/mapchests")


# Economy Related Endpoints
def get_coin_to_gem_exchange_rate():
    return requests.get("https://api.guildwars2.com/v2/commerce/exchange/coins?quantity=100000")

def get_gem_to_coin_exchange_rate():
    return requests.get("https://api.guildwars2.com/v2/commerce/exchange/gems?quantity=100")


# Account Related Endpoints
def get_world_bosses_of_specific_account():
    return requests.get("https://api.guildwars2.com/v2/account/worldbosses", headers={'Authorization': f'Bearer {THIRI_BEARER_TOKEN}'})
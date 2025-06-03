from guildwars_api import get_daily_world_boss_request, get_daily_chest_request, get_daily_crafting_request
from datetime import datetime

def get_daily_world_boss_list():
    daily_world_boss_list = get_daily_world_boss_request().json()

    formatted_bosses = []
    for boss in daily_world_boss_list:
        formatted_boss_name = boss.replace("_"," ").title()
        formatted_bosses.append(formatted_boss_name)

    return formatted_bosses


def get_daily_chest_list():
    daily_chest_list = get_daily_chest_request().json()

    formatted_chests = []
    for chest in daily_chest_list:
        formatted_chest_name = chest.replace("_"," ").title()
        formatted_chests.append(formatted_chest_name)

    return formatted_chests


def get_daily_crafting_list():
    daily_crafting_list = get_daily_crafting_request().json()

    formatted_crafts = []
    for craft in daily_crafting_list:
        formatted_craft_name = craft.replace("_"," ").title()
        formatted_crafts.append(formatted_craft_name)

    return formatted_crafts


def format_general_daily_information(get_daily_world_boss_list,get_daily_chest_list,get_daily_crafting_list):
    print(f"The daily objectives to this date: ({datetime.today()}) are the following: \n- World boss list: {get_daily_world_boss_list}\n- Chest list: {get_daily_chest_list}\n- Crafting list: {get_daily_crafting_list}")


def run_information_for_players():
    format_general_daily_information(get_daily_world_boss_list(),get_daily_chest_list(),get_daily_crafting_list())
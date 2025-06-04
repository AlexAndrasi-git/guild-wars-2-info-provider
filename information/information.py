from guildwars_api import get_daily_world_boss_request, get_daily_chest_request, get_daily_crafting_request, \
    get_world_bosses_of_specific_account, get_gem_to_coin_exchange_rate, get_coin_to_gem_exchange_rate
from datetime import datetime


# General Information
def get_daily_world_boss_list():
    daily_world_boss_list = get_daily_world_boss_request().json()

    formatted_bosses = []
    for boss in daily_world_boss_list:
        formatted_boss_name = boss.replace("_", " ").title()
        formatted_bosses.append(formatted_boss_name)

    return formatted_bosses


def get_daily_chest_list():
    daily_chest_list = get_daily_chest_request().json()

    formatted_chests = []
    for chest in daily_chest_list:
        formatted_chest_name = chest.replace("_", " ").title()
        formatted_chests.append(formatted_chest_name)

    return formatted_chests


def get_daily_crafting_list():
    daily_crafting_list = get_daily_crafting_request().json()

    formatted_crafts = []
    for craft in daily_crafting_list:
        formatted_craft_name = craft.replace("_", " ").title()
        formatted_crafts.append(formatted_craft_name)

    return formatted_crafts


# Specific User Information
def get_remaining_world_bosses(formatted_bosses, get_world_bosses_of_specific_account):
    remaining_world_bosses = []
    eliminated_bosses = get_world_bosses_of_specific_account.json()
    for boss in formatted_bosses:
        if boss.lower() not in [eliminated_boss.lower().replace("_", " ") for eliminated_boss in eliminated_bosses]:
            remaining_world_bosses.append(boss)

    return remaining_world_bosses


# Economy Related Information
def get_coin_to_gem_exchange_rate_details(get_coin_to_gem_exchange_rate):
    coin_to_gem_calculation = get_coin_to_gem_exchange_rate.json()
    return coin_to_gem_calculation['coins_per_gem'], coin_to_gem_calculation['quantity']


def get_gem_to_coin_exchange_rate_details(get_gem_to_coin_exchange_rate):
    gem_to_coin_calculation = get_gem_to_coin_exchange_rate.json()
    return gem_to_coin_calculation['coins_per_gem'], gem_to_coin_calculation['quantity']


# Formatter and Runner
def format_general_daily_information(get_daily_world_boss_list, get_daily_chest_list, get_daily_crafting_list,
                                     get_remaining_world_bosses, coin_to_gem_amount, coin_to_gem_quantity,
                                     gem_to_coin_amount, gem_to_coin_quantity):
    print(
        f"The daily objectives to this date: ({datetime.today()}) are the following: \n"
        f"- World boss list: {get_daily_world_boss_list}\n"
        f"  You still have to eliminate {len(get_remaining_world_bosses)} out of {len(get_daily_world_boss_list)} world bosses: {get_remaining_world_bosses}\n"
        f"- Chest list: {get_daily_chest_list}\n"
        f"- Crafting list: {get_daily_crafting_list}"
        f"  \n\nInformation about the current state of the economy:\n"
        f"- The number of coins you required for a single gem: {coin_to_gem_amount} / The number of gems you get for 100000 coins: {coin_to_gem_quantity}\n"
        f"- The number of coins you get for a single gem: {gem_to_coin_amount} / The number of coins you get for 100 gems: {gem_to_coin_quantity}"
    )


def run_information_for_players():
    formatted_world_boss_list = get_daily_world_boss_list()
    formatted_chest_list = get_daily_chest_list()
    formatted_crafting_list = get_daily_crafting_list()
    coin_to_gem_amount, coin_to_gem_quantity = get_coin_to_gem_exchange_rate_details(get_coin_to_gem_exchange_rate())
    gem_to_coin_amount, gem_to_coin_quantity = get_gem_to_coin_exchange_rate_details(get_gem_to_coin_exchange_rate())

    format_general_daily_information(formatted_world_boss_list,
                                     formatted_chest_list,
                                     formatted_crafting_list,
                                     get_remaining_world_bosses(formatted_world_boss_list,
                                     get_world_bosses_of_specific_account()),
                                     coin_to_gem_amount, coin_to_gem_quantity,
                                     gem_to_coin_amount, gem_to_coin_quantity)

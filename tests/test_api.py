from guildwars_api import get_daily_chest_request, get_daily_world_boss_request, get_daily_crafting_request
from pprint import pprint


def test_daily_world_boss_endpoint():
    daily_world_boss_response = get_daily_world_boss_request()
    assert daily_world_boss_response.status_code == 200, f"""
    Unexpected Status Code: {daily_world_boss_response.status_code}
    Response Body: {daily_world_boss_response.text}
    """

    daily_boss_list = daily_world_boss_response.json()
    pprint(f"Daily Boss list: {daily_boss_list}")
    assert isinstance(daily_boss_list, list)
    assert len(daily_boss_list) > 0

def test_daily_crafting_endpoint():
    daily_crafting_response = get_daily_crafting_request()
    assert daily_crafting_response.status_code == 200, f"""
    Unexpected Status Code: {daily_crafting_response.status_code}
    Response Body: {daily_crafting_response.text}
    """

    daily_crafting_list = daily_crafting_response.json()
    pprint(f"Daily Crafting list: {daily_crafting_list}")
    assert isinstance(daily_crafting_list, list)
    assert len(daily_crafting_list) > 0


def test_daily_chest_endpoint():
    daily_chest_response = get_daily_chest_request()
    assert daily_chest_response.status_code == 200, f"""
    Unexpected Status Code: {daily_chest_response.status_code}
    Response Body: {daily_chest_response.text}
    """

    daily_chest_list = daily_chest_response.json()
    pprint(f"Daily Chest List: {daily_chest_list}")
    assert isinstance(daily_chest_list, list)
    assert len(daily_chest_list) > 0


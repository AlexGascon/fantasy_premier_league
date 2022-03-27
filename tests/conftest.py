from fantasy_premier_league.models.gameweek import Gameweek

from datetime import datetime, timezone

from pytest import fixture


@fixture
def gameweek():
    return Gameweek(
        id=1,
        name='Gameweek 1',
        deadline_time=datetime(year=2021, month=8, day=13, hour=17, minute=30, second=0, tzinfo=timezone.utc),
        average_entry_score=69,
        finished=True,
        data_checked=True,
        highest_scoring_entry=5059647,
        deadline_time_epoch=1628875800,
        deadline_time_game_offset=0,
        highest_score=150,
        is_previous=False,
        is_current=False,
        is_next=False,
        cup_leagues_created=False,
        h2h_ko_matches_created=False,
        chip_plays=[{"chip_name": "bboost", "num_played": 145658}, {"chip_name": "3xc", "num_played": 225749}],
        most_selected=275,
        most_transferred_in=1,
        top_element=277,
        top_element_info={"id": 277, "points": 20},
        transfers_made=0,
        most_captained=233,
        most_vice_captained=277
    )
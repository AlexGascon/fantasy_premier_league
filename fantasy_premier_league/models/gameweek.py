from fantasy_premier_league.utils import Utils

from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List

from dataclasses_json import dataclass_json, config


@dataclass_json
@dataclass
class Gameweek:
    id: int
    average_entry_score: int
    chip_plays: List
    cup_leagues_created: bool
    data_checked: bool
    deadline_time_epoch: int
    deadline_time_game_offset: int
    finished: bool
    h2h_ko_matches_created: bool
    highest_scoring_entry: int
    highest_score: int
    is_previous: bool
    is_current: bool
    is_next: bool
    most_selected: int
    most_transferred_in: int
    most_captained: int
    most_vice_captained: int
    name: str
    top_element: int
    top_element_info: Dict[str, int]
    transfers_made: int
    deadline_time: datetime = field(
        metadata=config(
            encoder=Utils.format_datetime_as_utc,
            decoder=Utils.parse_utc_datetime
        )
    )

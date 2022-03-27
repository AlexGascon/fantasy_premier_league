from fantasy_premier_league.models.gameweek import Gameweek


class TestGameweek:
    GAMEWEEK_FIXTURE_PATH = 'tests/fixtures/gameweek.json'

    def test_parses_from_json(self, gameweek):
        expected_gameweek = gameweek

        json_gameweek = open(self.GAMEWEEK_FIXTURE_PATH).read()
        assert Gameweek.from_json(json_gameweek) == expected_gameweek

    def test_formats_to_json_correctly(self, gameweek):
        assert Gameweek.from_json(gameweek.to_json()) == gameweek

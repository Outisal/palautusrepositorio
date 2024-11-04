import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

# Luodaan stub-luokka, joka palauttaa ennalta määritellyt pelaajat
class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),     # 16 points
            Player("Lemieux", "PIT", 45, 54),     # 99 points
            Player("Kurri", "EDM", 37, 53),       # 90 points
            Player("Yzerman", "DET", 42, 56),     # 98 points
            Player("Gretzky", "EDM", 35, 89),     # 124 points
        ]

# Testiluokka StatisticsService-luokalle
class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # Injektoidaan StatisticsService-oliolle PlayerReaderStub-olio
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search_finds_player(self):
        # Tarkistetaan, että pelaaja löytyy haettaessa nimellä
        player = self.stats.search("Kurri")
        self.assertIsNotNone(player)
        self.assertEqual(player.name, "Kurri")
    
    def test_search_returns_none_if_player_not_found(self):
        # Tarkistetaan, että None palautuu, jos pelaajaa ei löydy
        player = self.stats.search("Nonexistent Player")
        self.assertIsNone(player)

    def test_team_returns_correct_players(self):
        # Tarkistetaan, että joukkueen pelaajat palautetaan oikein
        team_players = self.stats.team("EDM")
        self.assertEqual(len(team_players), 3)
        self.assertEqual(team_players[0].name, "Semenko")
        self.assertEqual(team_players[1].name, "Kurri")
        self.assertEqual(team_players[2].name, "Gretzky")

    def test_team_returns_empty_list_if_no_players_in_team(self):
        # Tarkistetaan, että tyhjä lista palautetaan, jos joukkueessa ei ole pelaajia
        team_players = self.stats.team("Nonexistent Team")
        self.assertEqual(len(team_players), 0)

    def test_top_returns_sorted_by_points(self):
        top_players = self.stats.top(5, SortBy.POINTS)
        expected_names = ["Gretzky", "Lemieux", "Yzerman", "Kurri", "Semenko"]
        self.assertEqual([player.name for player in top_players], expected_names)

    def test_top_returns_sorted_by_goals(self):
        top_players = self.stats.top(5, SortBy.GOALS)
        expected_names = ["Lemieux", "Yzerman", "Kurri", "Gretzky", "Semenko"]
        self.assertEqual([player.name for player in top_players], expected_names)

    def test_top_returns_sorted_by_assists(self):
        top_players = self.stats.top(5, SortBy.ASSISTS)
        expected_names = ["Gretzky", "Yzerman", "Lemieux", "Kurri", "Semenko"]
        self.assertEqual([player.name for player in top_players], expected_names)

    def test_top_returns_fewer_players_if_how_many_exceeds_list_length(self):
        top_players = self.stats.top(15)  # Requesting more than available
        self.assertEqual(len(top_players), 5)  # Should return all 5 players

    def test_top_returns_exact_number_if_how_many_matches(self):
        top_players = self.stats.top(5)  # Requesting exactly 10 players
        self.assertEqual(len(top_players), 5)  # Should return all 5 players

    def test_top_handles_empty_list(self):
        empty_reader = PlayerReaderStub()
        empty_reader.get_players = lambda: []  # Override to return empty list
        stats_empty = StatisticsService(empty_reader)
        top_players = stats_empty.top(5)  # Requesting from an empty list
        self.assertEqual(len(top_players), 0)  # Should return an empty list
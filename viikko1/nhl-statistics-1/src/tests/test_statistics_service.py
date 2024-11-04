import unittest
from statistics_service import StatisticsService
from player import Player

# Luodaan stub-luokka, joka palauttaa ennalta määritellyt pelaajat
class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri", "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89),

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

    def test_top_returns_correct_number_of_top_players(self):
        # Tarkistetaan, että oikea määrä parhaita pelaajia palautetaan
        top_players = self.stats.top(2)
        self.assertEqual(len(top_players), 3)  # Mukaan lukien index 0
        self.assertEqual(top_players[0].name, "Gretzky")
        self.assertEqual(top_players[1].name, "Lemieux")
        self.assertEqual(top_players[2].name, "Yzerman")

    def test_top_returns_all_players_if_how_many_exceeds_list_length(self):
        # Tarkistetaan, että kaikki pelaajat palautetaan, jos luku ylittää pelaajamäärän
        top_players = self.stats.top(10)
        self.assertEqual(len(top_players), 5)  # Kaikki pelaajat mukana
        self.assertEqual(top_players[0].name, "Gretzky")
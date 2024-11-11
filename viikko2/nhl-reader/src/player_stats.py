
class PlayerStats:
    def __init__(self, reader) -> None:
        self.players = reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        top_players = filter(lambda player: player.nationality == nationality, self.players)
        # Järjestäminen pisteiden (goals + assists) mukaan laskevasti
        return sorted(top_players, key=lambda player: player.points(), reverse=True)
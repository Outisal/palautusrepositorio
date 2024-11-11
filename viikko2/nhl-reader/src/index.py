import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
    response = requests.get(url).json()

    players = [Player(player_data) for player_data in response]

    # Suodatus suomalaisiin pelaajiin
    finnish_players = filter(lambda player: player.nationality == "FIN", players)

    # Järjestäminen pisteiden (goals + assists) mukaan laskevasti
    sorted_players = sorted(finnish_players, key=lambda player: player.points(), reverse=True)

    # Tulostus
    print("Players from FIN\n")
    for player in sorted_players:
        print(player)

if __name__ == "__main__":
    main()

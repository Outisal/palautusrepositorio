import requests
import re
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
from player_reader import PlayerReader
from player import Player
from player_stats import PlayerStats

def get_available_nationalities(players_data):
    nationalities = set()  # Using a set to avoid duplicates
    for player in players_data:
        nationality = player.nationality
        nationalities.add(nationality)
    return sorted(nationalities)

def get_available_seasons():
    url = "https://studies.cs.helsinki.fi/nhlstats/"
    response = requests.get(url)
    available_seasons = []
    lines = response.text.splitlines()
    for line in lines:
        # Look for the line containing the seasons (e.g., "following seasons available 2018-19, 2019-20, ...")
        if "following seasons available" in line:
            available_seasons = line.split("following seasons available")[1].strip().split(", ")
            break
    available_seasons = [re.sub(r'<.*?>','', season).strip() for season in available_seasons]
    return available_seasons    
    # Look for the line containing the "following seasons available"

def main():
    available_seasons = get_available_seasons()
    # Rich Console
    console = Console()
    console.print("NHL Statistics by nationality\n")

    # Ask the user for input (season and nationality)
    season = Prompt.ask("Select season", choices=available_seasons)
    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    
    reader = PlayerReader(url)
    player_data = reader.get_players()
    stats = PlayerStats(reader)
    while True:
        available_nationalities = get_available_nationalities(player_data)
        nationality = Prompt.ask("Select nationality", choices=available_nationalities)

        players = stats.top_scorers_by_nationality(nationality)

        # Luo Rich Table tulostusta varten
        table = Table(title=f"Top scorers from {nationality} season {season}")

        # Lisää sarakkeet taulukkoon
        table.add_column("Name", style="cyan", no_wrap=True)
        table.add_column("Team", style="magenta")
        table.add_column("Goals", justify="right", style="green")
        table.add_column("Assists", justify="right", style="green")
        table.add_column("Points", justify="right", style="bold yellow")

        # Lisää pelaajat taulukkoon
        for player in players:
            table.add_row(
                player.name,
                player.team,
                str(player.goals),
                str(player.assists),
                f"{player.goals + player.assists}"
            )

        # Tulostetaan taulukko
        console.print(table)

if __name__ == "__main__":
    main()

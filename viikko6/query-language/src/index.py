from player_statistics import Statistics
from player_reader import PlayerReader
from matchers import Not, HasFewerThan, All, And, HasAtLeast, PlaysIn

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    matcher = And(
        HasAtLeast(5, "goals"),
        HasAtLeast(20, "assists"),
        PlaysIn("PHI")
    )

    matcher1 = And(
    Not(HasAtLeast(2, "goals")),
    PlaysIn("NYR"))

    matcher2 = And(
    HasFewerThan(2, "goals"),
    PlaysIn("NYR")
    )


    for player in stats.matches(matcher1):
        print(player)
    for player in stats.matches(matcher2):
        print(player)
    
    filtered_with_all = stats.matches(All())
    print(len(filtered_with_all))

if __name__ == "__main__":
    main()

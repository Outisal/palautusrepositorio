class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.team = dict['team']
        self.goals = dict['goals']
        self.assists = dict['assists']
        self.nationality = dict['nationality']

    def points(self):
        return self.goals + self.assists
    
    def __str__(self):
        return f"{self.name:20} {self.team} {self.goals:2} + {self.assists:2} = {self.points()}"

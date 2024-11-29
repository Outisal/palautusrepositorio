class TennisGame:

    Love = 0
    Fifteen = 1
    Thirty = 2
    Forty = 3

    SCORE_NAMES = {Love: "Love", Fifteen: "Fifteen", Thirty: "Thirty", Forty: "Forty"}

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score += 1
        elif player_name == "player2":
            self.player2_score += 1

    def is_tied(self):
        return self.player1_score == self.player2_score
    
    def get_score_tied(self):
        if self.player1_score >= self.Forty:
            return "Deuce"
        return f"{self.SCORE_NAMES[self.player1_score]}-All"

    def is_in_end_game(self):
        return self.player1_score > self.Forty or self.player2_score> self.Forty
    
    def get_score_end_game(self):
        score_difference = self.player1_score - self.player2_score
        if score_difference == 1:
            return f"Advantage {self.player1_name}"
        if score_difference == -1:
            return f"Advantage {self.player2_name}"
        if score_difference >= 2:
            return f"Win for {self.player1_name}"
        return f"Win for {self.player2_name}"
    
    def get_score_during_game(self):
        return f"{self.SCORE_NAMES[self.player1_score]}-{self.SCORE_NAMES[self.player2_score]}"

    def get_score(self):
        if self.is_tied():
            return self.get_score_tied()
        if self.is_in_end_game():
            return self.get_score_end_game()
        return self.get_score_during_game()

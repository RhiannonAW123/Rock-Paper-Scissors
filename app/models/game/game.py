class Game():

    def __init__(self, players):
        self.players = players
        # if players[0].choice == "rock":
        #     if players[1].choice == "rock":
        #         self.winner = None
        #     if players[1].choice == "paper":
        #         self.winner = players[1]
        #     if players[1].choice == "scissors":
        #         self.winner = players[0]

        # if players[0].choice == "paper":
        #     if players[1].choice == "rock":
        #         self.winner = players[0]
        #     if players[1].choice == "paper":
        #         self.winner = None
        #     if players[1].choice == "scissors":
        #         self.winner = players[1]

        # if players[0].choice == "scissors":
        #     if players[1].choice == "rock":
        #         self.winner = players[1]
        #     if players[1].choice == "paper":
        #         self.winner = players[0]
        #     if players[1].choice == "scissors":
        #         self.winner = None

    def play_game(self):
        if self.players[0].choice == "rock":
            if self.players[1].choice == "rock":
                self.winner = None
            if self.players[1].choice == "paper":
                self.winner = self.players[1]
            if self.players[1].choice == "scissors":
                self.winner = self.players[0]

        if self.players[0].choice == "paper":
            if self.players[1].choice == "rock":
                self.winner = self.players[0]
            if self.players[1].choice == "paper":
                self.winner = None
            if self.players[1].choice == "scissors":
                self.winner = self.players[1]

        if self.players[0].choice == "scissors":
            if self.players[1].choice == "rock":
                self.winner = self.players[1]
            if self.players[1].choice == "paper":
                self.winner = self.players[0]
            if self.players[1].choice == "scissors":
                self.winner = None
        return self.winner
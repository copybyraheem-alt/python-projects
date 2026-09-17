class Player:
    def __init__(self, name, postion):
        self.name=name
        self.postion=postion

class Team:
    def __init__(self, team_name):
        self.team_name=team_name
        self.players=[]

    def add_players(self, player):
        self.players.append(player)

    def display_roster(self):
        for py in self.players:
            print(f"{py.name} plays as {py.postion}")

p1 = Player("Ronaldo", "Forward")
p2 = Player("lucaaaa", "Midfielder")

madrid = Team("Real Madrid")
madrid.add_players(p1)
madrid.add_players(p2)

madrid.display_roster()
class Player:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.postion = position  # backward compatibility alias

class Team:
    def __init__(self, team_name):
        self.team_name = team_name
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    add_players = add_player  # alias for backward compatibility

    def display_roster(self):
        for py in self.players:
            print(f"{py.name} plays as {py.position}")


if __name__ == "__main__":
    p1 = Player("Ronaldo", "Forward")
    p2 = Player("lucaaaa", "Midfielder")

    madrid = Team("Real Madrid")
    madrid.add_player(p1)
    madrid.add_player(p2)

    madrid.display_roster()

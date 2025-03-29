class BallPlayer:
    def __init__(self, name: str, number: int, goals: int, passes: int, minutes: int):
        self.name = name
        self.number = number
        self.goals = goals
        self.passes = passes
        self.minutes = minutes

    def __str__(self):
        return (f'BallPlayer(name={self.name}, number={self.number}, '
            f'goals={self.goals}, passes={self.passes}, minutes={self.minutes})')


# Write your solution here
def most_goals(ball_players: list) -> int :

    return sorted(ball_players, key = lambda ball_player: ball_player.goals  ,reverse=True)[0].name

def most_points(ball_players: list) -> tuple  :

    ballplayer = sorted(ball_players, key = lambda ball_player: ball_player.goals + ball_player.passes ,reverse=True)[0]
    return ballplayer.name,ballplayer.number

def least_minutes(ball_players: list) -> BallPlayer:
    return sorted(ball_players, key = lambda ball_player: ball_player.minutes)[0]

if __name__ == "__main__":
    player1 = BallPlayer("Archie Bonkers", 13, 5, 12, 46)
    player2 = BallPlayer("Speedy Tickets", 7, 2, 26, 55)
    player3 = BallPlayer("Cruella De Hill", 9, 1, 32, 26)
    player4 = BallPlayer("Devilled Tasmanian", 12, 1, 11, 41)
    player5 = BallPlayer("Donald Quack", 4, 3, 9, 12)
    
    team = [player1, player2, player3, player4, player5]
    print(most_goals(team))
    print(most_points(team))
    print(least_minutes(team))

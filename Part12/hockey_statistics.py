# Write your solution here
import json

filename = input("file name: ")

with open(filename) as player_data_file:
  data = player_data_file.read()

players = json.loads(data)

print(f"read the data of {len(players)} players")

def help():
  print()
  print("commands:")
  print("0 quit")
  print("1 search for player")
  print("2 teams")
  print("3 countries")
  print("4 players in team")
  print("5 players from country")
  print("6 most points")
  print("7 most goals")

help()

def print_player_data(player_name: str, team:str, goals: int, assists: int):

  goals_template = goals if goals >= 10 else f"{goals:2}"
  assists_template = assists if assists >= 10 else f"{assists:2}"
  total_score = goals+assists if goals+assists >= 100 else f"{goals+assists:3}"
  
  print(f"{player_name:21}{team:5}{goals_template} + {assists_template} = {total_score}")

def search_player():
  player_name = input("name: ")
  player = list(filter(lambda cur_player: cur_player["name"] == player_name,players))[0]

  print_player_data(player["name"],player["team"],player["goals"],player["assists"])

def list_teams():
  teams = set(map(lambda player: player["team"],players))

  for team in sorted(teams, key=lambda team: team):
    print(team)

def list_countries():
  countries = set(map(lambda player: player["nationality"],players))

  for country in sorted(countries, key=lambda country:country):
    print(country)

def players_in_team():
  team = input("team: ")
  team_players = list(filter(lambda player: player["team"] == team,players))

  for player in sorted(team_players,key = lambda cur_player: cur_player["goals"] + cur_player["assists"],reverse=True):
    
    print_player_data(player["name"],player["team"],player["goals"],player["assists"])

def players_in_country():
  country = input("country: ")
  team_players = list(filter(lambda player: player["nationality"] == country,players))
  
  for player in sorted(team_players,key = lambda cur_player: cur_player["goals"] + cur_player["assists"],reverse=True):
    print_player_data(player["name"],player["team"],player["goals"],player["assists"])

def players_with_most_points():
  how_many = int(input("how many: "))
  
  # first order by goals in reverse order
  players_by_goals = sorted(players,key = lambda player: player["goals"],reverse=True)
  # then order by scores
  players_by_scores = sorted(players_by_goals,key = lambda player: player["goals"] + player["assists"],reverse=True)

  for player in players_by_scores[0:how_many]:
    print_player_data(player["name"],player["team"],player["goals"],player["assists"])

def players_with_most_goals():
  how_many = int(input("how many: "))

  # first order by games in reverse order
  players_by_games = sorted(players,key=lambda player: player["games"])

  # then order by scores
  players_by_scores = sorted(players_by_games,key=lambda player: player["goals"] ,reverse=True)

  for player in players_by_scores[0:how_many]:
    print_player_data(player["name"],player["team"],player["goals"],player["assists"])

while True:
  print()
  command = int(input("command: "))

  if command == 0:
    break

  if command == 1:
    search_player()

  if command == 2:
    list_teams()

  if command == 3:
    list_countries()
  
  if command == 4:
    players_in_team()

  if command == 5:
    players_in_country()

  if command == 6:
    players_with_most_points()

  if command == 7:
    players_with_most_goals()

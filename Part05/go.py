# Write your solution here

def who_won(game_board: list):
  player_1_piece = 0
  player_2_piece = 0

  for row in game_board:
    for piece in row:
      if piece == 1:  player_1_piece += 1
      if piece == 2:  player_2_piece += 1

  if player_1_piece == player_2_piece: return 0
  if player_1_piece > player_2_piece: return 1
  
  return 2

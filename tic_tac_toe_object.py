class Game:
  def __init__(self):
    self.order = 1
    self.player1 = Player("X")
    self.player2 = Player("O")
    self.grid = Grid()
    self.grid.print()

  def is_game_over(self) -> bool:
    if self.grid.has_won():
      print("Won")
      return True
    elif self.is_tie():
      print("Tie")
      return True

  def is_tie(self) -> bool: 
    return self.order > 9 and not self.grid.has_won()

  def update(self):
    if self.order % 2:
      player = self.player1
    else:
      player = self.player2

    player_position = player.return_position()
    self.grid.place_symbol_at_position(player.symbol, player_position)
    self.grid.print()
    self.order += 1
    
class Player:
  def __init__(self, symbol: str):
    self.symbol = symbol

  def return_position(self) -> int:
    return int(input("choose position: "))

class Grid:
  def __init__(self):
    self.grid = [
      "0", "1", "2",
      "3", "4", "5",
      "6", "7", "8",
    ]
    
  def place_symbol_at_position(self, symbol: str, player_position: int):
    self.grid[player_position] = symbol

  def print(self):
    print(f"\n{self.grid[:3]}\n{self.grid[3:6]}\n{self.grid[6:]}\n")

  def has_won(self) -> bool:
    grid_slices = [
      slice(0, 9, 4), slice(2, 7, 2),                   # diagonals 
      slice(0, 3, 1), slice(3, 6, 1), slice(6, 9, 1),   # rows
      slice(0, 9, 3), slice(1, 9, 3), slice(2, 9, 3),   # columns
    ]
    
    for element in grid_slices:
      if len(set(self.grid[element])) == 1:
          return True
        
    return False

def main():
  tic_tac_toe_game = Game()
  
  while not tic_tac_toe_game.is_game_over():
    tic_tac_toe_game.update()
  

main()



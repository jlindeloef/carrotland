from random import randint
import os

"""
Carrot class
"""
class Carrot:
  def __init__(self, size, land, location):
    self.size = size

    if land == 'horizontal' or land == 'vertical':
      self.land = land
    else:
      raise ValueError("Value must be 'horizontal' or 'vertical'.")
    
    if land == 'horizontal':
      if location['row'] in range(row_size):
        self.placement = []
        for index in range(size):
          if location['col'] + index in range(col_size):
            self.placement.append({'row': location['row'], 'col': location['col'] + index})
          else:
            raise IndexError("Column is not in the land.")
      else:
        raise IndexError("Row is not in the land.")
    elif land == 'vertical':
      if location['col'] in range(col_size):
        self.placement = []
        for index in range(size):
          if location['row'] + index in range(row_size):
            self.placement.append({'row': location['row'] + index, 'col': location['col']})
          else:
            raise IndexError("Row is not in the land.")
      else:
        raise IndexError("Column is not in the land.")

    if self.filled():
      print_board(board)
      print(" ".join(str(place) for place in self.placement))
      raise IndexError("You searched there already")
    else:
      self.fillBoard()


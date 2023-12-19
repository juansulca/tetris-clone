WIDTH = 10
HEIGHT = 20
TILE_SIZE = 8

TETROMINOES = {
  'T': [(0, 0), (-1, 0), (1, 0), (0, -1)],
  'O': [(0, 0), (0, -1), (1, 0), (1, -1)],
  'J': [(0, 0), (-1, 0), (0, -1), (0, -2)],
  'L': [(0, 0), (1, 0), (0, -1), (0, -2)],
  'I': [(0, 0), (0, 1), (0, -1), (0, -2)],
  'S': [(0, 0), (-1, 0), (0, -1), (1, -1)],
  'Z': [(0, 0), (1, 0), (0, -1), (-1, -1)],
}

T_COLORS = {
  'T': 1,
  'O': 1,
  'J': 5,
  'L': 8,
  'I': 1,
  'S': 5,
  'Z': 8,
}

STARTING_POSITIONS = (WIDTH // 2 - 1 , 0)
NEXT_POSITIONS = (int(WIDTH * 1.3) , int(HEIGHT * 0.45))

MOVE_DIRECTIONS = { 'left': (-1, 0), 'right': (1, 0), 'down': (0, 1) }

ALPHABET = 'c a t'. split()#'a e o c t u'. split()
import pyxel
from constants import WIDTH, HEIGHT, TILE_SIZE, STARTING_POSITIONS, NEXT_POSITIONS
from tetromino import Tetromino

class Tetris:
  def __init__(self, app) -> None:
    self.app = app
    self.tetromino = Tetromino(self)
    self.next_tetromino = Tetromino(self, False)
    self.hold = None
    self.hold_pressed = False
    self.grid = [[0]*WIDTH for _ in range(HEIGHT)]
    self.score = 0
    self.points_per_lines = {0: 0, 1: 100, 2: 300, 3: 700, 4: 1500}

  def draw_hud(self):
    hud_x, next_y = WIDTH*1.15*TILE_SIZE, NEXT_POSITIONS[1]*TILE_SIZE - 30
    pyxel.text(hud_x, 5, 'Score:', 7)
    pyxel.text(hud_x, 15, str(self.score), 7)
    pyxel.text(hud_x, next_y, 'Next', 7)
    pyxel.text(hud_x, next_y + TILE_SIZE*6, 'Hold:', 7)
  
  def draw_grid(self):
    for x in range(WIDTH):
      for y in range(HEIGHT):
        if self.grid[y][x]:
          color = self.grid[y][x].color
          pyxel.rect(x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE, color)
        else:
          pyxel.rectb(x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE, 13)

  def is_game_over(self):
    if self.tetromino.blocks[0].x == STARTING_POSITIONS[0] and self.tetromino.blocks[0].y == STARTING_POSITIONS[1]:
      return True
  
  def check_tetromino_landed(self):
    if self.tetromino.landed:
      if self.is_game_over():
        print('Game Over')
      else:
        self.put_blocks_in_grid()
        self.tetromino = self.next_tetromino
        self.tetromino.is_current = True
        self.next_tetromino = Tetromino(self, False)
        self.hold_pressed = False

  def put_blocks_in_grid(self):
    for block in self.tetromino.blocks:
      x, y = block.x, block.y
      self.grid[y][x] = block

  def check_full_lines(self):
    full_lines = 0
    row = HEIGHT - 1
    for y in range(HEIGHT - 1, -1, -1):
      for x in range(WIDTH):
        self.grid[row][x] = self.grid[y][x]
      
      if self.grid[y][x]:
        self.grid[y][x].x = x
        self.grid[y][x].y = y

      if sum(map(bool, self.grid[row])) < WIDTH:
        row -= 1
      else:
        for x in range(WIDTH):
          self.grid[row][x] = 0
        full_lines += 1
      
    self.score += self.points_per_lines[full_lines]
        
  def hold_tetromino(self):
    if self.hold_pressed:
      return
    self.hold_pressed = True
    if self.hold is None:
      self.hold = self.tetromino
      self.hold.is_current = False
      self.hold.is_on_hold = True
      self.tetromino = self.next_tetromino
      self.tetromino.is_current = True
      self.tetromino.is_on_hold = False
      self.next_tetromino = Tetromino(self, False, False)
    else:
      temp = self.tetromino
      self.tetromino = self.hold
      self.tetromino.reset_position()
      self.tetromino.is_current = True
      self.tetromino.is_on_hold = False
      self.hold = temp
      self.hold.is_current = False
      self.hold.is_on_hold = True
      # self.next_tetromino = Tetromino(self, False)

  def update(self):
    self.tetromino.update()
    self.check_tetromino_landed()
    self.check_full_lines()

  def control(self):
    if pyxel.frame_count % 4 == 0:
      if pyxel.btn(pyxel.KEY_LEFT):
        self.tetromino.move('left')
      if pyxel.btn(pyxel.KEY_RIGHT):
        self.tetromino.move('right')
      if pyxel.btn(pyxel.KEY_DOWN):
        self.tetromino.move('down')
    if pyxel.btnp(pyxel.KEY_SPACE):
      self.tetromino.rotate()
    if pyxel.btnp(pyxel.KEY_B):
      self.hold_tetromino()

  def draw(self):
    self.draw_hud()
    self.draw_grid()
    self.tetromino.draw()
    self.next_tetromino.draw()
    self.hold.draw() if self.hold else None

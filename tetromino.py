import time
import pyxel
import random
from constants import TILE_SIZE, WIDTH, HEIGHT, TETROMINOES, MOVE_DIRECTIONS, STARTING_POSITIONS, T_COLORS, NEXT_POSITIONS, ALPHABET

class Block:
  def __init__(self, tetromino, pos, color, letter):
    self.tetromino = tetromino
    self.x = pos[0] + STARTING_POSITIONS[0]
    self.y = pos[1] + STARTING_POSITIONS[1]
    self.next_x = pos[0] + NEXT_POSITIONS[0]
    self.next_y = pos[1] + NEXT_POSITIONS[1]
    self.color = color
    self.letter = letter

  def reset_position(self, pos):
    self.x = pos[0] + STARTING_POSITIONS[0]
    self.y = pos[1] + STARTING_POSITIONS[1]

  def rotate(self, pivot):
    translatedX, translatedY = self.x - pivot[0], self.y - pivot[1]
    rotatedX, rotatedY = translatedY, -translatedX
    return (rotatedX + pivot[0], rotatedY + pivot[1])


  def draw(self):
    if self.tetromino.is_current:
      pyxel.rect(self.x * TILE_SIZE, self.y * TILE_SIZE, TILE_SIZE, TILE_SIZE, self.color)
      pyxel.text(self.x * TILE_SIZE + 2, self.y * TILE_SIZE + 2, self.letter, 7)
    else:
      extra_offset = 5 if self.tetromino.is_on_hold else 0
      pyxel.rect(self.next_x * TILE_SIZE, (self.next_y + extra_offset) * TILE_SIZE, TILE_SIZE, TILE_SIZE, self.color)
      pyxel.text(self.next_x * TILE_SIZE + 2, (self.next_y + extra_offset) * TILE_SIZE + 2, self.letter, 7)

  def is_colliding(self):
    if 0 <= self.x < WIDTH and self.y < HEIGHT:
      return False
    return True

class Tetromino:
  def __init__(self, tetris, current=True, hold=False):
    self.tetris = tetris
    self.is_current = current
    self.is_on_hold = hold
    self.last_movement = time.time()
    self.update_interval = 0.8
    self.shape = random.choice(list(TETROMINOES.keys()))
    self.color = T_COLORS[self.shape]
    self.letter = random.choice(ALPHABET)
    self.blocks = [Block(self, pos, self.color, self.letter) for pos in TETROMINOES[self.shape]]
    self.landed = False

  def move(self, direction):
    move_direction = MOVE_DIRECTIONS[direction]
    new_block_positions = [(b.x + move_direction[0], b.y + move_direction[1]) for b in self.blocks]
    if not self.is_colliding(new_block_positions):
      for b in self.blocks:
        b.x += move_direction[0]
        b.y += move_direction[1]
    elif direction == 'down':
      self.landed = True

  def check_collision(self, pos):
    x, y = pos
    if 0 <= x < WIDTH and y < HEIGHT and ( y < 0 or not self.tetris.grid[y][x]):
        return False
    return True

  def is_colliding(self, block_positions):
    return any(map(self.check_collision, block_positions))
  
  def rotate(self):
    pivot = self.blocks[0]
    rotated_block_positions = [b.rotate((pivot.x, pivot.y)) for b in self.blocks]
    if not self.is_colliding(rotated_block_positions):
      for i, b in enumerate(self.blocks):
        b.x, b.y = rotated_block_positions[i]

  def update(self):
    current_time = time.time()
    if current_time - self.last_movement > self.update_interval:
      self.last_movement = current_time
      self.move('down')

  def draw(self):
    for b in self.blocks:
      b.draw()
  
  def reset_position(self):
    self.blocks = [Block(self, pos, self.color, self.letter) for pos in TETROMINOES[self.shape]]

import pyxel
from constants import TILE_SIZE, WIDTH, HEIGHT
from tetris import Tetris

class App:
  def __init__(self):
    self.tetris = Tetris(self)
    pyxel.init(int((WIDTH * TILE_SIZE)* 1.7), HEIGHT * TILE_SIZE)
    pyxel.run(self.update, self.draw)

  def update(self):
    self.tetris.control()
    self.tetris.update()

  def draw(self):
    pyxel.cls(0)
    self.tetris.draw()

App()

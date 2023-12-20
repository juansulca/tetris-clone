import pyxel
from constants import TILE_SIZE, WIDTH, HEIGHT


class Title:
  def __init__(self, app):
    self.app = app

  def draw(self):
    pyxel.text(WIDTH//2 * TILE_SIZE, HEIGHT * 0.25 * TILE_SIZE, "English tetris", pyxel.frame_count % 16)
    pyxel.text(WIDTH//2 * TILE_SIZE, HEIGHT * 0.5 * TILE_SIZE, "- PRESS SPACE -", 13)

  def update(self):
    if pyxel.btnp(pyxel.KEY_SPACE):
      self.app.screen = 'game'

import pyxel
from constants import TILE_SIZE, WIDTH, HEIGHT
from tetris import Tetris
from title import Title
from game_over import GameOver
import nltk

nltk.download('words')

class App:
  def __init__(self):
    self.tetris = Tetris(self)
    self.title = Title(self)
    self.game_over = GameOver(self)
    self.screen = 'title'
    pyxel.init(int((WIDTH * TILE_SIZE)* 1.7), HEIGHT * TILE_SIZE)
    pyxel.run(self.update, self.draw)

  def update(self):
    if self.screen == 'title':
      self.title.update()
    if self.screen == 'game':
      self.update_game()
    if self.screen == 'game_over':
      self.game_over.update()

  def draw(self):
    pyxel.cls(0)
    if self.screen == 'title':
      self.title.draw()
    if self.screen == 'game':
      self.draw_game()
    if self.screen == 'game_over':
      self.game_over.draw()

  def update_game(self):
    self.tetris.control()
    self.tetris.update()

  def draw_game(self):
    self.tetris.draw()

App()

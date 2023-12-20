import pyxel

class GameOver:
  def __init__(self, app):
    self.app = app

  def draw(self):
    pyxel.text(20, 20, "Game Over", 8)
    pyxel.text(20, 30, "Press space to restart", 8)

  def update(self):
    if pyxel.btnp(pyxel.KEY_SPACE):
      self.app.screen = 'game'


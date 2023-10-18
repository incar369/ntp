from random import *
from game import Game
from ursina import *
import numpy

app = Ursina()

window.borderless = False

scene.fog_density = (50, 200)
game = Game()

app.run()

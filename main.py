from ursina import *

from game import Game
#add new comment
app = Ursina()

window.borderless = False

scene.fog_density = (50, 200)
game = Game()

app.run()

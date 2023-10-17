from ursina import *
from config import *
import random

class Player:
    def __init__(self, model, _rgb, scale, _collider, position):
        self.unit = Entity(model=model, color=_rgb, scale=scale, collider=_collider, position=position)
        self.init()

    def render(self):
        self.unit.z += PLAYER_SPEED

    def init(self):
        self.unit.update = self.render

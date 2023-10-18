from ursina import *
from config import *
import random


class Player:
    def __init__(self, model, _rgb, scale, _collider, position):
        self.unit = Entity(model=model, color=color.gray, texture='white_cube', scale=scale, collider=_collider, position=position)
        self.init()

    def render(self):
        self.unit.z += time.dt * PLAYER_SPEED

    def init(self):
        self.unit.update = self.render

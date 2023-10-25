from player import Player as _Player
from camera import Camera as _Camera
from terrain_generator import Terrain as _Terrain
from config import *


class Game:
    def __init__(self):
        self.player = _Player('cube', PLAYER_COLOR, PLAYER_SIZE, 'box', PLAYER_POSITION)
        self.camera = _Camera(self.player)
        self.terrain = _Terrain(self.player)

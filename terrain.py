from ursina import *
from chunk import Chunk as _Chunk
from config import *
import random


class Terrain:
    def __init__(self, player):
        self.p = player.unit
        self.chunk = _Chunk
        self.terrain = []
        self.terrain_count = 3

        self.init_terrain()

    def init_terrain(self):
        c = self.chunk.create_chunk(self.chunk, 1, 1)
        self.terrain.append(c)

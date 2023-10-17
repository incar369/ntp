from config import *
from random import *


class Chunk:
    def __init__(self):
        pass

    @staticmethod
    def create_chunk_fragment(x, y, z):
        return Entity(model='cube', color=rgb(24, 60 + randrange(11), 24), scale=(1, 1, 3), collider='box',
                      position=(x, y, z))

    def create_chunk(self, x, y):
        chunk = []
        for _x in range(x, x + CHUNK_SIZE):
            for _y in range(y, y + CHUNK_SIZE):
                chunk.append(self.create_chunk_fragment(_x, -8, _y))
        return chunk

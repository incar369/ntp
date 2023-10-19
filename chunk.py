from config import *


class Chunk:
    def __init__(self):
        pass

    @staticmethod
    def create_chunk_fragment(x, y, z):
        return Entity(model='cube', color=color.white, texture='white_cube', scale=(CUBE_SIZE, CUBE_SIZE, CUBE_SIZE), collider='box',
                      position=(x, y, z))

    def create_chunk(self, x, y):
        chunk = []
        for _x in range(x, x + CHUNK_SIZE):
            for _y in range(y, y + CHUNK_SIZE):
                chunk.append(self.create_chunk_fragment(_x * CUBE_SIZE, -8, _y * CUBE_SIZE))
        return chunk

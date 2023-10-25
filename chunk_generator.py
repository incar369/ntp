import random
from ursina import color

from config import *


class ChunkGenerator:
    def __init__(self):
        self._texture = 'white_cube'

    def create_chunk_fragment(self, x, y, z, fragment_color):

        _model = Plane(subdivisions=(1, 1))
        _scale = (CUBE_SIZE, CUBE_SIZE, CUBE_SIZE)
        _pos = (x, y, z)
        _color = fragment_color

        element = Entity(model=_model, texture=self._texture, scale=_scale, collider='box', position=_pos, color=_color)
        return element

    def create_chunk(self, x, z):
        _color = color.random_color()
        _pool = []
        for _x in range(x, x + CHUNK_SIZE):
            for _z in range(z, z + CHUNK_SIZE):
                _pool.append(self.create_chunk_fragment(_x * CUBE_SIZE, -8, _z * CUBE_SIZE, _color))

        return _pool

from chunk_generator import ChunkGenerator as _ChunkGenerator
from config import *


class Terrain:
    def __init__(self, player):
        self.p = player
        self.terrain = []
        self.chunk_generator = _ChunkGenerator()
        self.start_x = 0
        self.start_y = 0
        self.start_z = 0

        self.init_start_terrain()

    def init_start_terrain(self):
        _x = int(self.p.unit.position.x / CHUNK_SIZE)
        _z = int(self.p.unit.position.z / CHUNK_SIZE)

        _left_pos = -TERRAIN_SIDE_COUNT
        _right_pos = TERRAIN_SIDE_COUNT
        _back_pos = -TERRAIN_BACK_COUNT
        _front_pos = TERRAIN_FRONT_COUNT

        for x in range(_left_pos, _right_pos):
            for z in range(_back_pos, _front_pos):

                pos_generation_x = x * CHUNK_SIZE
                pos_generation_z = z * CHUNK_SIZE

                # print(pos_generation_x, pos_generation_z)

                self.terrain.append(self.chunk_generator.create_chunk(pos_generation_x, pos_generation_z))

from chunk import Chunk as _Chunk
from config import *


class Terrain:
    def __init__(self, player):
        self.p = player.unit
        self.chunk = _Chunk
        self.terrain = []

        self.init_terrain()

    def init_terrain(self):
        for w in range(TERRAIN_WIDTH_COUNT):
            for d in range(TERRAIN_DEPTH_COUNT):

                max_width_terrain_length = TERRAIN_WIDTH_COUNT * CHUNK_SIZE
                max_depth_terrain_length = TERRAIN_DEPTH_COUNT * CHUNK_SIZE

                start_point_width = (max_width_terrain_length / 2) - max_width_terrain_length
                start_point_depth = (max_depth_terrain_length / 2) - max_depth_terrain_length

                current_position_width = int(start_point_width + (CHUNK_SIZE * w))
                current_position_depth = int(start_point_depth + (CHUNK_SIZE * d))

                c = self.chunk.create_chunk(self.chunk, current_position_width, current_position_depth)
                self.terrain.append(c)

    def update(self):
        print(time)

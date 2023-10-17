from ursina import *
from config import *


class Camera:
    def __init__(self, player):
        self.cam = EditorCamera()
        self.p = player.unit
        self.init()

    def render(self):
        self.cam.z = self.p.z - CAMERA_DISTANCE

    def init(self):
        self.cam.update = self.render

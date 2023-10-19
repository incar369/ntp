from config import *


class Camera:
    def __init__(self, player):
        self.cam = EditorCamera()

        self.cam.y += 5
        self.cam.rotation_x += 15

        self.p = player.unit
        self.init()

    def render(self):
        self.cam.z = self.p.z - CAMERA_DISTANCE

    def init(self):
        self.cam.update = self.render

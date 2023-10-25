from config import *


class Camera:
    def __init__(self, player):
        self.cam = EditorCamera()
        self.dist = CAMERA_DISTANCE

        self.cam.y += 5
        self.cam.rotation_x += 15

        self.p = player.unit
        self.init()

    def render(self):
        self.cam.z = self.p.z - self.dist

        self.dist -= held_keys['w'] * 1
        self.dist += held_keys['s'] * 1
        self.cam.x += held_keys['d'] * 100 * time.dt
        self.cam.x -= held_keys['a'] * 100 * time.dt
        self.cam.rotation_y += held_keys['e'] * 100 * time.dt
        self.cam.rotation_y -= held_keys['q'] * 100 * time.dt

    def init(self):
        self.cam.update = self.render

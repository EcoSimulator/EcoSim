# Matthew Severance, 4/18/2016

import WorldMap
from Sprite import Sprite

class DeerSprite(Sprite):

    def __init__(self, image, image_rect, type):
        Sprite.__init__(self, image, image_rect, type)

    def update(self):
        WorldMap.mouse_monitor(WorldMap.buttons_global)
        Sprite.update(self)
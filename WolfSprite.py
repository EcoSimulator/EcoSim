from Sprite import Sprite

class WolfSprite(Sprite):

    def __init__(self, image, image_rect, type, screen):
        Sprite.__init__(self, image, image_rect, type, screen)

        radius = 50

    def update(self):
        Sprite.update(self)

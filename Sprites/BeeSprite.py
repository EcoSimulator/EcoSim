# Matthew Severance 5/2/2016

import pygame

import Global
import Utils
from Sprite import Sprite


class BeeSprite(Sprite):

    def __init__(self, image_rect):
        Sprite.__init__(self, pygame.image.load("Resources/sprites/bees.png"), image_rect, "bees")
        self.speed = 15
        self.radius = 250
        Global.bee_group.add_internal(self)

    def update(self):
        Sprite.button_ops(self)
        if self.health_monitor():
            return
        if not Sprite.hunt(self, Global.plant_group):
            Sprite.update(self)

    def health_monitor(self):
        self.health -= 2
        if self.health <= 0:
            dirtyrect = Utils.clean_screen.subsurface(self.rect).copy()
            self.screen.blit(dirtyrect, self.rect)
            pygame.display.flip()
            Global.bee_group.remove_internal(self)
            return True

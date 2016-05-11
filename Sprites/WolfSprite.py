import pygame
import Global
import Utils
from Sprite import Sprite


__author__ = "Matthew Severance"
__date__ = "4/18/2016"


class WolfSprite(Sprite):
    """
    Wolf sprite class
    """
    def __init__(self, image_rect):
        """
        Calls Spite.init as super
        Sets speed, radius and runningAway (a boolean)
        Adds to global deer_group
        """
        Sprite.__init__(self, pygame.image.load("Resources/sprites/wolf.png"), image_rect, "wolf")
        self.speed = 15
        self.radius = 100
        self.stealth = 60
        Global.wolf_group.add_internal(self)

    def update(self):
        """
        Updates the deer sprite
        Either dies, hunts deer,  or calls Sprite.update
        """
        Sprite.button_ops(self)
        if self.health_monitor():
            return
        if not Sprite.hunt(self, Global.deer_group):
            Sprite.update(self)

    def health_monitor(self):
        """
        Decreases the sprite's health each update
        Returns true and kills the sprite if health <= 0
        """
        self.health -= 3
        if self.health <= 0:
            dirtyrect = Utils.clean_screen.subsurface(self.rect).copy()
            self.screen.blit(dirtyrect, self.rect)
            pygame.display.flip()
            Global.wolf_group.remove_internal(self)
            return True

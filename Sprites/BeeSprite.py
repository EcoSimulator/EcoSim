import pygame
import Global
import Utils
from Sprite import Sprite

__author__ = "Matthew Severance"


class BeeSprite(Sprite):
    """
    Bee sprite class
    """
    def __init__(self, image_rect):
        """
        Calls Spite.init as super
        Sets speed and radius
        Adds to global bee_group
        """
        Sprite.__init__(self, pygame.image.load("Resources/sprites/bees.png"), image_rect, "bees")
        self.speed = 15
        self.radius = 250
        Global.bee_group.add_internal(self)

    def update(self):
        """
        Updates the bee sprite
        Either dies, calls Sprite.hunt for plants or calls Sprite.update
        """
        Sprite.button_ops(self)
        if self.health_monitor():
            return
        if not Sprite.hunt(self, Global.plant_group):
            Sprite.update(self)

    def health_monitor(self):
        """
        Decreases the sprite's health each update
        Returns true and kills the sprite if health <= 0
        """
        self.health -= 2
        if self.health <= 0:
            dirtyrect = Utils.clean_screen.subsurface(self.rect).copy()
            self.screen.blit(dirtyrect, self.rect)
            pygame.display.flip()
            Global.bee_group.remove_internal(self)
            return True

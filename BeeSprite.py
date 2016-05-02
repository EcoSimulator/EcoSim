# Matthew Severance 5/2/2016

from Sprite import Sprite
import WorldMap
import pygame
import Utils


class BeeSprite(Sprite):

    def __init__(self, image_rect):
        Sprite.__init__(self, pygame.image.load("Resources/sprites/bees.png"), image_rect, "bees")
        self.speed = 15
        self.radius = 250
        WorldMap.bee_group.add_internal(self)

    def update(self):
        if self.health_monitor():
            return
        WorldMap.mouse_monitor(WorldMap.buttons_global)
        if not Sprite.hunt(self, WorldMap.plant_group):
            Sprite.update(self)

    def health_monitor(self):
        self.health -= 2
        if self.health <= 0:
            dirtyrect = Utils.clean_screen.subsurface(self.rect).copy()
            self.screen.blit(dirtyrect, self.rect)
            pygame.display.flip()
            WorldMap.bee_group.remove_internal(self)
            return True

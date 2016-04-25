# Matthew Severance, 4/18/2016


from Sprite import Sprite
import WorldMap
import pygame
import math
import Utils


class WolfSprite(Sprite):

    def __init__(self, image_rect):
        Sprite.__init__(self, pygame.image.load("Resources/sprites/wolf.png"), image_rect, "wolf")
        self.speed = 15
        self.radius = 150
        self.stealth = 60

    def update(self):
        if self.health_monitor():
            return
        WorldMap.mouse_monitor(WorldMap.buttons_global)
        if not Sprite.hunt(self, WorldMap.deer_group):
            Sprite.update(self)

    def health_monitor(self):
        print self.health
        self.health -= 1
        if self.health <= 0:
            dirtyrect = Utils.clean_screen.subsurface(self.rect).copy()
            self.screen.blit(dirtyrect, self.rect)
            pygame.display.flip()
            WorldMap.wolf_group.remove_internal(self)
            return True

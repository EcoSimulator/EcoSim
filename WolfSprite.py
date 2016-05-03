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
        self.radius = 100
        self.stealth = 60
        WorldMap.wolf_group.add_internal(self)

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = True
                    WorldMap.pause(paused)
        if self.health_monitor():
            return
        WorldMap.mouse_monitor(WorldMap.buttons_global)
        if not Sprite.hunt(self, WorldMap.deer_group):
            Sprite.update(self)

    def health_monitor(self):
        self.health -= 3
        if self.health <= 0:
            dirtyrect = Utils.clean_screen.subsurface(self.rect).copy()
            self.screen.blit(dirtyrect, self.rect)
            pygame.display.flip()
            WorldMap.wolf_group.remove_internal(self)
            return True

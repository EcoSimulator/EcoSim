# Matthew Severance, 4/18/2016


import pygame
import random
import math
import Utils

class Sprite(pygame.sprite.DirtySprite):

    def __init__(self, image, rect, type, screen):
        pygame.sprite.Sprite.__init__(self)

        self.image = image
        self.rect = rect
        self.type = type
        self.screen = screen

    def add_internal(self, group):
        pygame.sprite.Sprite.add_internal(self, group)

    def remove_internal(self, group):
        pygame.sprite.Sprite.remove_internal(self, group)

    def blit(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        direction = math.radians(random.randint(0, 361))
        dirtyrect = Utils.clean_screen.subsurface(self.rect).copy()
        self.screen.blit(dirtyrect, self.rect)
        self.rect.move_ip(10*math.cos(direction), 10*math.sin(direction))
        self.blit()
        pygame.display.flip()
        # rect.clamp moves one rectangle inside another
        # good for wolf catching deer probably

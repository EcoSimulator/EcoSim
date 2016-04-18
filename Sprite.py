# Matthew Severance, 4/18/2016


import pygame
import random
import math


class Sprite(pygame.sprite.DirtySprite):

    clean_screen = pygame.image.load("Resources/randomterrain.jpg")

    def __init__(self, image, image_rect, type, screen):
        pygame.sprite.Sprite.__init__(self)

        self.image = image
        self.image_rect = image_rect
        self.type = type
        self.screen = screen

    def add_internal(self, group):
        pygame.sprite.Sprite.add_internal(self, group)

    def remove_internal(self, group):
        pygame.sprite.Sprite.remove_internal(self, group)

    def blit(self):
        self.screen.blit(self.image, self.image_rect)

    def update(self):
        direction = math.radians(random.randint(0, 361))
        magnitude = 1   # change to incorporate speed
        dirtyrect = self.clean_screen.subsurface(self.image_rect).copy()
        self.screen.blit(dirtyrect, self.image_rect)
        self.image_rect.move_ip(10*math.cos(direction), 10*math.sin(direction))
        self.blit()
        pygame.display.flip()
        # rect.clamp moves one rectangle inside another
        # good for wolf catching deer probably

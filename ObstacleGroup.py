# Matthew Severance 4/19/2016

import pygame


class ObstacleGroup(pygame.sprite.Group):

    _spritegroup = "obstacle"

    def __init__(self):
        pygame.sprite.Group.__init__(self)

    def add_internal(self, sprite):
        pygame.sprite.Group.add_internal(self, sprite)

    def remove_internal(self, sprite):
        pygame.sprite.Group.remove_internal(self, sprite)

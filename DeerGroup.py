# Matthew Severance, 4/18/2016


import pygame


class DeerGroup(pygame.sprite.Group):

    _spritegroup = "deer"

    def __init__(self):
        pygame.sprite.Group.__init__(self)

    def add_internal(self, sprite):
        pygame.sprite.Group.add_internal(self, sprite)

    def remove_internal(self, sprite):
        pygame.sprite.Group.remove_internal(self, sprite)

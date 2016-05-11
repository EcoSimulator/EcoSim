# Matthew Severance, 4/18/2016


import pygame

__author__ = "Matthew Severance"


class DeerGroup(pygame.sprite.Group):
    """
    Group for deer sprites
    Group Name = "deer"
    """
    _spritegroup = "deer"

    def __init__(self):
        pygame.sprite.Group.__init__(self)

    def add_internal(self, sprite):
        pygame.sprite.Group.add_internal(self, sprite)

    def remove_internal(self, sprite):
        pygame.sprite.Group.remove_internal(self, sprite)

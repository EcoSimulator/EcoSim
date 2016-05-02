# Matthew Severance, 5/2/2016


import pygame


class BeeGroup(pygame.sprite.Group):

    _spritegroup = "bees"

    def __init__(self):
        pygame.sprite.Group.__init__(self)

    def add_internal(self, sprite):
        pygame.sprite.Group.add_internal(self, sprite)

    def remove_internal(self, sprite):
        pygame.sprite.Group.remove_internal(self, sprite)

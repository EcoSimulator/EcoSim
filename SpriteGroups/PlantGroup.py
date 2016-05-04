# Matthew Severance, 4/18/2016


import pygame


class PlantGroup(pygame.sprite.Group):

    _spritegroup = "plant"
    reproduction_rate = 0.78

    def __init__(self):
        pygame.sprite.Group.__init__(self)

    def add_internal(self, sprite):
        pygame.sprite.Group.add_internal(self, sprite)

    def remove_internal(self, sprite):
        pygame.sprite.Group.remove_internal(self, sprite)

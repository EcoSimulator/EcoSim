import pygame

__author__ = "Matthew Severance"


class PlantGroup(pygame.sprite.Group):
    """
    Group for plant sprites
    Group Name = "plant"
    """
    _spritegroup = "plant"
    reproduction_rate = 0.78

    def __init__(self):
        pygame.sprite.Group.__init__(self)

    def add_internal(self, sprite):
        pygame.sprite.Group.add_internal(self, sprite)

    def remove_internal(self, sprite):
        pygame.sprite.Group.remove_internal(self, sprite)

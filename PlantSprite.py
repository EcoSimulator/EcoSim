# Matthew Severance, 4/25/2016


import pygame
import Utils


class PlantSprite(pygame.sprite.DirtySprite):

    def __init__(self, rect):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Resources/sprites/plant.png")
        self.rect = rect
        self.type = "plant"
        self.screen = Utils.screen

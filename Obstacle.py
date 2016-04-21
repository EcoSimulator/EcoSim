# Matthew Severance 4/19/2016

import pygame
from pygame.locals import *
import Utils
import WorldMap
import random


class Obstacle(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Resources/sprites/dickbutt.jpg")
        self.rect = Rect((150, 150), (50, 50))
        # self.rect.move_ip(random.randrange(50, 1110), random.randrange(50, 600))    # doesn't work right for some reason
        self.add_internal(WorldMap.obstacle_group)



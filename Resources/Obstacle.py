import pygame
from pygame.locals import *
import Utils

class Obstacle(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.rect = Rect((Utils.screen_size[0]/2, Utils.screen_size[1]/2), (50, 50))



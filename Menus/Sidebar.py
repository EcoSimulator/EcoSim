import pygame
from pygame.locals import *
import Utils

def make_sidebar():

    sidebar = []
    sidebar_img = pygame.image.load("Resources/sidebar/sidebar.png")
    sidebar_rect = Rect((0, 0), (154, 719))

    sidebar.append((sidebar_img, sidebar_rect))

    for tuple in sidebar:
        Utils.screen.blit(tuple[0], tuple[1])

    pygame.display.flip()
    return sidebar

import pygame
from pygame.locals import *
from Menus import Sidebar
import Utils

def make_monitor(itr, species):
    # We need a few different elements:
    # 1. White capsule to hold the sprite and population counter
    # 2. Population counter
    # 3. Sprite
    # 4. Appropriate warning symbol

    monitor = []
    start_x = 12
    start_y = 14 + (itr*36)

    #warning symbol
    warning = pygame.image.load("Resources/sidebar/warningoff.png")
    warning_rect = Rect((start_x+0, start_y+1), (27, 24))
    #button
    button = pygame.image.load("Resources/sidebar/popbutton.png")
    button_rect = Rect((start_x+36, start_y+0), (90, 27))
    #sprite
    getSprite = ("Resources/sprites/" +species+ ".png")
    sprite = pygame.image.load(getSprite)
    sprite_rect = Rect((start_x+97, start_y+2), (24, 24))

    # make a button out of the capsule and its rectangle
    monitor.append((button, button_rect))
    # put the sprite on top of it
    monitor.append((sprite, sprite_rect))
    # put the warning symbol next to it
    monitor.append((warning, warning_rect))

    for tuple in monitor:
        Utils.screen.blit(tuple[0], tuple[1])
    pygame.display.flip()

    return monitor
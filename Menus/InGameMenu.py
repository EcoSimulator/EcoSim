import pygame
from pygame.locals import *
import Utils

"""
Menu displayed during the running of the game
"""


# makes all the buttons
def make_buttons():
    """
    Creates and displays the list of buttons present while the game is running
    0: Deer
    1: Wolf
    2: Plant
    3: Bee
    :return: the list of buttons
    """
    buttons = []

    # make a deer button, Rect creates the rectangle to draw the button in
    deer_button = pygame.image.load("Resources/buttons/deernormal.png")
    deer_button_rect = Rect((0, 0), (40, 39))

    # make a wolf button, Rect creates the rectangle to draw the button in
    wolf_button = pygame.image.load("Resources/buttons/wolfnormal.png")
    wolf_button_rect = Rect((0, deer_button_rect.bottom), (40, 39))

    # make a plant button, Rect creates the rectangle to draw the button in
    plant_button = pygame.image.load("Resources/buttons/plantnormal.png")
    plant_button_rect = Rect((0, wolf_button_rect.bottom), (40, 39))

    bee_button = pygame.image.load("Resources/buttons/beesnormal.png")
    bee_button_rect = Rect((0, plant_button_rect.bottom), (40, 39))

    # add buttons to the list
    buttons.append((deer_button, deer_button_rect))
    buttons.append((wolf_button, wolf_button_rect))
    buttons.append((plant_button, plant_button_rect))
    buttons.append((bee_button, bee_button_rect))

    # blit- puts stuff on the screen
    # blit terrain and buttons
    # flip just refreshes screen to display blits since last flip
    for button in buttons:
        Utils.screen.blit(button[0], button[1])
    pygame.display.flip()

    return buttons

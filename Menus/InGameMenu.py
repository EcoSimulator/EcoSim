import pygame
from pygame.locals import *
from Menus import PopMonitor, Sidebar
import Utils

__author__ = "Matthew Severance, Justin Tribuna"


def make_buttons():
    """
    Creates and displays the list of buttons present while the game is running
    0: Deer
    1: Wolf
    2: Plant
    3: Bee
    :return: the list of buttons
    """

    Sidebar.make_sidebar()

    buttons = []

    # we'll want the game to have a list of available species that we can get
    all_species = {"wolf", "deer", "bees", "plant"}
    index = 0
    for item in all_species:
        monitor = PopMonitor.make_monitor(index, item)
        buttons.append(monitor)
        index += 1

    # population monitors are blitted in PopMonitor
    # flip just refreshes screen to display blits since last flip
    pygame.display.flip()

    return buttons

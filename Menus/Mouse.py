import pygame
from pygame.locals import *
import Utils
from Sprites import SpriteProduction

"""
Mouse related functions for while the game is running
"""

# monitors mouse activity, mostly used for selecting buttons and placing animals now
def mouse_monitor(buttons):
    """
    Watches the mouse to detect hovering over and selection of buttons
    :param buttons: the buttons to watch
    :return: option (which buttons selected)
    """
    mouse = pygame.mouse    # our mouse from now on
    mouse_pos = mouse.get_pos()     # the position of the mouse
    for button in buttons:
        # while the mouse is within the bounds of any button in the button list
        while (button[1].left < mouse_pos[0] < button[1].right and
                button[1].top < mouse_pos[1] < button[1].bottom):
            # button[0] = deer
            if buttons.index(button) == 0:
                # change to highlighted deer button
                deer_button = pygame.image.load("Resources/buttons/deerselected.png")
                Utils.screen.blit(deer_button, button[1])
                pygame.display.flip()
                # waits for click to select deer button
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        place_image(mouse, "Resources/sprites/deer.png", "deer")
            # button[1] = wolf
            elif buttons.index(button) == 1:
                # change to highlighted wolf button
                wolf_button = pygame.image.load("Resources/buttons/wolfselected.png")
                Utils.screen.blit(wolf_button, button[1])
                pygame.display.flip()
                # waits for click to select wolf button
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        place_image(mouse, "Resources/sprites/wolf.png", "wolf")
            # button[2] = plant
            elif buttons.index(button) == 2:
                # change to highlighted plant button
                plant_button = pygame.image.load("Resources/buttons/plantselected.png")
                Utils.screen.blit(plant_button, button[1])
                pygame.display.flip()
                # waits for click to select plant button
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        place_image(mouse, "Resources/sprites/plant.png", "plant")
            elif buttons.index(button) == 3:
                # change to highlighted plant button
                bee_button = pygame.image.load("Resources/buttons/beesselected.png")
                Utils.screen.blit(bee_button, button[1])
                pygame.display.flip()
                # waits for click to select plant button
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        place_image(mouse, "Resources/sprites/bees.png", "bees")
            # update position for while loop
            mouse_pos = mouse.get_pos()
    # return buttons to normal
    for button in buttons:
        Utils.screen.blit(button[0], button[1])
    pygame.display.flip()


def buffer_mouse_pos(mouse_pos):
    """
    Buffers the mouse to prevent the user from placing sprites off-screen
    :param mouse_pos: the position of the last mouse press
    :return: the offset mouse position
    """
    buffer = 50     # 5= pixel buffer
    if mouse_pos[0] <= buffer:  # left
        mouse_pos[0] += buffer
        if mouse_pos[1] <= buffer:  # left top
            mouse_pos[1] += buffer
        elif mouse_pos[1] >= Utils.screen.get_bounding_rect().bottom - 1.5 * buffer:    # bottom left
            mouse_pos[1] -= 2 * buffer
    elif mouse_pos[0] >= Utils.screen.get_bounding_rect().right - 1.5 * buffer:     # right
        mouse_pos[0] -= 2 * buffer
        if mouse_pos[1] <= buffer:  # right top
            mouse_pos[1] += buffer
        elif mouse_pos[1] >= Utils.screen.get_bounding_rect().bottom - 1.5 * buffer:  # bottom right
            mouse_pos[1] -= 2 * buffer
    elif mouse_pos[1] <= buffer:  # top
            mouse_pos[1] += buffer
    elif mouse_pos[1] >= Utils.screen.get_bounding_rect().bottom - 1.5 * buffer:  # bottom
        mouse_pos[1] -= 2 * buffer
    return mouse_pos


# puts an image of an animal on screen at a mouse click
def place_image(mouse, image_name, animal_name):
    """
    Actually places the sprite at the (possibly buffered) mouse position
    :param mouse: pygame mouse, used to get position
    :param image_name: name of animal image
    :param animal_name: actual animal name
    :return: void
    """
    while True:  # waits forever, until user places animal
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                # buffer_mouse_pos(list(mouse.get_pos()))
                location = buffer_mouse_pos(list(mouse.get_pos()))
                SpriteProduction.spawn_sprite(location, image_name, animal_name)
                return

# Matthew Severance, 4/18/2016

import sys
from Sprite import Sprite
import pygame
from pygame.locals import *
from DeerGroup import DeerGroup
from WolfGroup import WolfGroup


deer_group = DeerGroup()
wolf_group = WolfGroup()
screen_size = 1280, 720


# displays the map, initializes terrain and buttons
def display_map():
       # just a random size
    screen = pygame.display.set_mode(screen_size)  # creates the screen
    pygame.display.set_caption("Environment Simulator")     # write the caption

    # sets the terrain to an image
    terrain = pygame.image.load("Resources/randomterrain.jpg")
    terrain_rect = Rect((0, 0), screen_size)

    # blit the terrain image to the screen
    screen.blit(terrain, terrain_rect)

    buttons = make_buttons(screen)   # the list of buttons, its a list of tuples [(image, image_rectangle)]

    # loop to listen on the mouse, delayed cuz otherwise stuff flickers
    while True:
        mouse_monitor(screen, buttons)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        wolf_group.update()
        deer_group.update()
        pygame.time.delay(100)


# makes all the buttons
def make_buttons(screen):
    buttons = []

    # make a deer button, Rect creates the rectangle to draw the button in
    deer_button = pygame.image.load("Resources/buttons/deernormal.png")
    deer_button_rect = Rect((0, 0), (40, 39))

    # make a wolf button, Rect creates the rectangle to draw the button in
    wolf_button = pygame.image.load("Resources/buttons/wolfnormal.png")
    wolf_button_rect = Rect((0, deer_button_rect.bottom), (40, 39))

    # add buttons to the list
    buttons.append((deer_button, deer_button_rect))
    buttons.append((wolf_button, wolf_button_rect))

    # blit- puts stuff on the screen
    # blit terrain and buttons
    # flip just refreshes screen to display blits since last flip
    for button in buttons:
        screen.blit(button[0], button[1])
    pygame.display.flip()

    return buttons


# monitors mouse activity, mostly used for selecting buttons and placing animals now
def mouse_monitor(screen, buttons):
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
                screen.blit(deer_button, button[1])
                pygame.display.flip()
                # waits for click to select deer button
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        place_image(screen, mouse, "Resources/sprites/deer.png", "deer")
            # button[1] = wolf
            elif buttons.index(button) == 1:
                # change to highlighted wolf button
                deer_button = pygame.image.load("Resources/buttons/wolfselected.png")
                screen.blit(deer_button, button[1])
                pygame.display.flip()
                # waits for click to select wolf button
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        place_image(screen, mouse, "Resources/sprites/wolf.png", "wolf")
            # update position for while loop
            mouse_pos = mouse.get_pos()
    # return buttons to normal
    for button in buttons:
        screen.blit(button[0], button[1])
    pygame.display.flip()


# puts an image of an animal on screen at a mouse click
def place_image(screen, mouse, image_name, animal_name):
    image = pygame.image.load(image_name)
    while True:  # waits forever, until user places animal
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                image_rect = Rect((mouse.get_pos()), (24, 24))
                new_sprite = Sprite(image, image_rect, animal_name, screen)
                new_sprite.blit()
                add_to_correct_group(new_sprite)
                return


def add_to_correct_group(sprite):
    if sprite.type == "wolf":
        wolf_group.add_internal(sprite)
    elif sprite.type == "deer":
        deer_group.add_internal(sprite)


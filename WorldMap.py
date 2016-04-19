# Matthew Severance, 4/18/5016

import sys
from Sprite import Sprite
import pygame
from pygame.locals import *
from DeerGroup import DeerGroup
from WolfGroup import WolfGroup
from WolfSprite import WolfSprite
from DeerSprite import DeerSprite
import random
import Utils

deer_group = DeerGroup()
wolf_group = WolfGroup()

# displays the map, initializes terrain and buttons
def display_map():
       # just a random size
    pygame.display.set_caption("Environment Simulator")     # write the caption

    # sets the terrain to an image
    terrain = pygame.image.load("Resources/randomterrain.jpg")
    terrain_rect = Rect((0, 0), Utils.screen_size)

    # blit the terrain image to the screen
    Utils.screen.blit(terrain, terrain_rect)

    buttons = make_buttons()   # the list of buttons, its a list of tuples [(image, image_rectangle)]

    # loop to listen on the mouse, delayed cuz otherwise stuff flickers
    count = 0
    while True:
        mouse_monitor(buttons)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        wolf_group.update()
        deer_group.update()
        reproduce(count)
        pygame.time.delay(100)
        count += 1
        if count > 1000:
            count = 0


# makes all the buttons
def make_buttons():
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
        Utils.screen.blit(button[0], button[1])
    pygame.display.flip()

    return buttons


# monitors mouse activity, mostly used for selecting buttons and placing animals now
def mouse_monitor(buttons):
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
                        place_image(Utils.screen, mouse, "Resources/sprites/deer.png", "deer")
            # button[1] = wolf
            elif buttons.index(button) == 1:
                # change to highlighted wolf button
                deer_button = pygame.image.load("Resources/buttons/wolfselected.png")
                Utils.screen.blit(deer_button, button[1])
                pygame.display.flip()
                # waits for click to select wolf button
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        place_image(Utils.screen, mouse, "Resources/sprites/wolf.png", "wolf")
            # update position for while loop
            mouse_pos = mouse.get_pos()
    # return buttons to normal
    for button in buttons:
        Utils.screen.blit(button[0], button[1])
    pygame.display.flip()


# puts an image of an animal on screen at a mouse click
def place_image(screen, mouse, image_name, animal_name):
    while True:  # waits forever, until user places animal
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                location = buffer_mouse_pos(list(mouse.get_pos()))
                spawn_sprite(location, image_name, animal_name)
                return


def spawn_sprite(location, image_name, animal_name):
    image = pygame.image.load(image_name)
    image_rect = Rect(location, (24, 24))
    new_sprite = Sprite(image, image_rect, animal_name)
    new_sprite.blit()
    add_to_correct_group(new_sprite)


def create_sprite(screen, location, image_name, animal_name):
    image = pygame.image.load(image_name)
    image_rect = Rect(location, (24, 24))
    new_sprite = Sprite(image, image_rect, animal_name)
    return new_sprite


def reproduce(count):
    buffer = 50     # 50 pixel buffer
    if count % 10 == 0:
        rand_location = (random.randrange(buffer, Utils.screen_size[0] - buffer),
                         random.randrange(buffer, Utils.screen_size[1] - buffer))
        new_sprite = create_sprite(Utils.screen, rand_location, "Resources/sprites/wolf.png", "wolf")
        while not Sprite.move_is_within_surface(new_sprite, random.randrange(buffer, Utils.screen_size[0] - buffer),
                                                random.randrange(buffer, Utils.screen_size[1] - buffer)):
            rand_location = (random.randrange(buffer, Utils.screen_size[0] - buffer),
                             random.randrange(buffer, Utils.screen_size[1] - buffer))
            new_sprite = create_sprite(Utils.screen, rand_location, "Resources/sprites/wolf.png", "wolf")
        new_sprite.kill()
        spawn_sprite(rand_location, "Resources/sprites/wolf.png", "wolf")

        rand_location = (random.randrange(buffer, Utils.screen_size[0] - buffer),
                         random.randrange(buffer, Utils.screen_size[1] - buffer))
        new_sprite = create_sprite(Utils.screen, rand_location, "Resources/sprites/deer.png", "deer")
        while not Sprite.move_is_within_surface(new_sprite, random.randrange(buffer, Utils.screen_size[0] - buffer),
                                                random.randrange(buffer, Utils.screen_size[1] - buffer)):
            rand_location = (random.randrange(buffer, Utils.screen_size[0] - buffer),
                             random.randrange(buffer, Utils.screen_size[1] - buffer))
            new_sprite = create_sprite(Utils.screen, rand_location, "Resources/sprites/deer.png", "deer")
        new_sprite.kill()
        spawn_sprite(rand_location, "Resources/sprites/deer.png", "deer")


def add_to_correct_group(sprite):
    if sprite.type == "wolf":
        wolf_group.add_internal(WolfSprite(sprite.image, sprite.rect, sprite.type))
    elif sprite.type == "deer":
        deer_group.add_internal(DeerSprite(sprite.image, sprite.rect, sprite.type))


def buffer_mouse_pos(mouse_pos):
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

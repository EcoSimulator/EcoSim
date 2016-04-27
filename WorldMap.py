# Matthew Severance, 4/18/5016

import sys
from Sprite import Sprite
import pygame
from pygame.locals import *
from DeerGroup import DeerGroup
from WolfGroup import WolfGroup
from PlantGroup import PlantGroup
from WolfSprite import WolfSprite
from DeerSprite import DeerSprite
from PlantSprite import PlantSprite
import random
import Utils

deer_group = DeerGroup()
wolf_group = WolfGroup()
plant_group = PlantGroup()
buttons_global = []


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
    global buttons_global
    buttons_global = buttons

    # loop to listen on the mouse, delayed cuz otherwise stuff flickers
    count = 0
    while True:
        mouse_monitor(buttons)
        display_population_count(wolf_group, 1)
        display_population_count(deer_group, 0)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = True
                    pause(paused)
            if event.type == pygame.QUIT:
                sys.exit()
        if len(wolf_group) > 0:
            wolf_group.update()
        if len(deer_group) > 0:
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


def create_sprite(location, image_name, animal_name):
    image = pygame.image.load(image_name)
    image_rect = Rect(location, (24, 24))
    new_sprite = Sprite(image, image_rect, animal_name)
    return new_sprite


# display population count of a sprite group, near its button (given button index in buttons_global
def display_population_count(sprite_group, button_index):
    # initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
    font = pygame.font.SysFont("monospace", 28, True, False)

    # get count of group
    sprite_count = str(len(sprite_group))

    # generate coordinates and render text
    button_x = buttons_global[button_index][1].right + 10
    button_y = buttons_global[button_index][1].centery - 12
    label = font.render(sprite_count, 1, (255, 255, 255))

    # reset view
    dirty_rect = Utils.clean_screen.subsurface(Rect((button_x, button_y), (40, 39))).copy()
    Utils.screen.blit(dirty_rect, (button_x, button_y))

    # blit new text
    Utils.screen.blit(label, (button_x, button_y))
    pygame.display.flip()


def reproduce(count):
    buffer = 50     # 50 pixel buffer
    if count % 10 == 0:
        rand_location = (random.randrange(buffer, Utils.screen_size[0] - buffer),
                         random.randrange(buffer, Utils.screen_size[1] - buffer))
        # new_sprite = create_sprite(rand_location, "Resources/sprites/wolf.png", "wolf")
        # while not Sprite.move_is_within_surface(new_sprite, rand_location[0], rand_location[1]):
        #     rand_location = (random.randrange(buffer, Utils.screen_size[0] - buffer),
        #                      random.randrange(buffer, Utils.screen_size[1] - buffer))
        #     new_sprite = create_sprite(rand_location, "Resources/sprites/wolf.png", "wolf")
        # new_sprite.kill()
        spawn_sprite(rand_location, "Resources/sprites/wolf.png", "wolf")
        display_population_count(wolf_group, 1)     # display new wolf count

        rand_location = (random.randrange(buffer, Utils.screen_size[0] - buffer),
                         random.randrange(buffer, Utils.screen_size[1] - buffer))
        # new_sprite = create_sprite(rand_location, "Resources/sprites/deer.png", "deer")
        # while not Sprite.move_is_within_surface(new_sprite, rand_location[0], rand_location[1]):
        #     rand_location = (random.randrange(buffer, Utils.screen_size[0] - buffer),
        #                      random.randrange(buffer, Utils.screen_size[1] - buffer))
        #     new_sprite = create_sprite(rand_location, "Resources/sprites/deer.png", "deer")
        # new_sprite.kill()
        spawn_sprite(rand_location, "Resources/sprites/deer.png", "deer")
        display_population_count(deer_group, 0)     # display new deer count

        rand_location = (random.randrange(buffer, Utils.screen_size[0] - buffer),
                         random.randrange(buffer, Utils.screen_size[1] - buffer))
        # new_sprite = create_sprite(rand_location, "Resources/sprites/plant.png", "plant")
        # while not Sprite.move_is_within_surface(new_sprite, rand_location[0], rand_location[1]):
        #     rand_location = (random.randrange(buffer, Utils.screen_size[0] - buffer),
        #                      random.randrange(buffer, Utils.screen_size[1] - buffer))
        #     new_sprite = create_sprite(rand_location, "Resources/sprites/plant.png", "plant")
        # new_sprite.kill()
        spawn_sprite(rand_location, "Resources/sprites/plant.png", "plant")


def add_to_correct_group(sprite):
    if sprite.type == "wolf":
        wolf_group.add_internal(WolfSprite(sprite.rect))
    elif sprite.type == "deer":
        deer_group.add_internal(DeerSprite(sprite.rect))
    elif sprite.type == "plant":
        plant_group.add_internal(PlantSprite(sprite.rect))


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


# pause menu stuff, may want to put all of this in its own file
def pause(paused):
    buttons = make_pause_buttons()

    while paused:
        if (pause_menu_monitor(buttons)) == 0:
            paused = False
            terrain = pygame.image.load("Resources/randomterrain.jpg")
            terrain_rect = Rect((0, 0), Utils.screen_size)
            Utils.screen.blit(terrain, terrain_rect)
            pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False
                    terrain = pygame.image.load("Resources/randomterrain.jpg")
                    terrain_rect = Rect((0, 0), Utils.screen_size)
                    Utils.screen.blit(terrain, terrain_rect)
                    pygame.display.flip()
                    break


def make_pause_buttons():
    center_x = Utils.screen_size[0]/2
    center_y = Utils.screen_size[1]/2
    buttons = []

    paused_label = pygame.image.load("Resources/buttons/paused.png")
    paused_label_rect = Rect((center_x-116, center_y-115), (111, 21))
    resume_button = pygame.image.load("Resources/buttons/resumenormal.png")
    resume_button_rect = Rect((center_x-75, center_y-50), (129, 39))
    quit_button = pygame.image.load("Resources/buttons/quitnormal.png")
    quit_button_rect = Rect((center_x-75, center_y), (129, 39))

    buttons.append((resume_button, resume_button_rect))
    buttons.append((quit_button, quit_button_rect))

    Utils.screen.blit(paused_label, paused_label_rect)
    for button in buttons:
        Utils.screen.blit(button[0], button[1])
    pygame.display.flip()
    return buttons


def pause_menu_monitor(buttons):
    mouse = pygame.mouse    # our mouse from now on
    mouse_pos = mouse.get_pos()     # the position of the mouse
    resume = 0
    quit = 1
    for button in buttons:
        # while the mouse is within the bounds of any button in the button list
        while (button[1].left < mouse_pos[0] < button[1].right and
                button[1].top < mouse_pos[1] < button[1].bottom):
            # button[0] = resume
            if buttons.index(button) == 0:
                resume_button = pygame.image.load("Resources/buttons/resumeselected.png")
                Utils.screen.blit(resume_button, button[1])
                pygame.display.flip()
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        return resume
            # button[1] = quit
            elif buttons.index(button) == 1:
                quit_button = pygame.image.load("Resources/buttons/quitselected.png")
                Utils.screen.blit(quit_button, button[1])
                pygame.display.flip()
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        sys.exit()
            # update position for while loop
            mouse_pos = mouse.get_pos()
    # return buttons to normal
    for button in buttons:
        Utils.screen.blit(button[0], button[1])
    pygame.display.flip()



import random

import pygame
from pygame.locals import *

import Global
import Utils
from Sprites.BeeSprite import BeeSprite
from Sprites.DeerSprite import DeerSprite
from Sprites.PlantSprite import PlantSprite
from Sprites.Sprite import Sprite
from Sprites.WolfSprite import WolfSprite


def spawn_sprite(location, image_name, animal_name, should_be_pollinated=False):
    image = pygame.image.load(image_name)
    image_rect = Rect(location, (24, 24))
    if should_be_pollinated:
        new_sprite = PlantSprite(image_rect, True)
    else:
        if animal_name == "wolf":
            new_sprite = WolfSprite(image_rect)
        elif animal_name == "deer":
            new_sprite = DeerSprite(image_rect)
        elif animal_name == "plant":
            new_sprite = PlantSprite(image_rect)
        elif animal_name == "bees":
            new_sprite = BeeSprite(image_rect)
        else:
            new_sprite = Sprite(image, image_rect, animal_name)
    new_sprite.blit()


# display population count of a sprite group, near its button (given button index in buttons_global
def display_population_count(sprite_group, button_index):
    # initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
    font = pygame.font.SysFont("monospace", 28, True, False)

    # get count of group
    sprite_count = str(len(sprite_group))

    # generate coordinates and render text
    button_x = Global.buttons_global[button_index][1].right + 10
    button_y = Global.buttons_global[button_index][1].centery - 12
    label = font.render(sprite_count, 1, (255, 255, 255))

    # reset view
    dirty_rect = Utils.clean_screen.subsurface(Rect((button_x, button_y), (40, 39))).copy()
    Utils.screen.blit(dirty_rect, (button_x, button_y))

    # blit new text
    Utils.screen.blit(label, (button_x, button_y))
    pygame.display.flip()


def reproduce(count, first_generation=False):
    buffer = 150     # 50 pixel buffer
    if count % 10 == 0:
        if len(Global.wolf_group) > 0 or first_generation:
            rand_location = (random.randrange(buffer, Utils.screen.get_rect().right - buffer),
                             random.randrange(buffer, Utils.screen.get_rect().bottom - buffer))
            while not Utils.rect_within_screen(rand_location):
                rand_location = (random.randrange(buffer, Utils.screen.get_rect().right - buffer),
                                 random.randrange(buffer, Utils.screen.get_rect().bottom - buffer))
            spawn_sprite(rand_location, "Resources/sprites/wolf.png", "wolf")
            display_population_count(Global.wolf_group, 1)     # display new wolf count

        if len(Global.deer_group) > 0 or first_generation:
            for num in range(0, 2):
                rand_location = (random.randint(buffer, Utils.screen.get_rect().right - buffer),
                                 random.randint(buffer, Utils.screen.get_rect().bottom - buffer))
                while not Utils.rect_within_screen(rand_location):
                    rand_location = (random.randrange(buffer, Utils.screen.get_rect().right - buffer),
                                     random.randrange(buffer, Utils.screen.get_rect().bottom - buffer))
                spawn_sprite(rand_location, "Resources/sprites/deer.png", "deer")
                display_population_count(Global.deer_group, 0)     # display new deer count

        if len(Global.plant_group) > 0 or first_generation:
            for num in range(0, 2):
                rand_location = (random.randint(buffer, Utils.screen.get_rect().right - buffer),
                                 random.randint(buffer, Utils.screen.get_rect().bottom - buffer))
                while not Utils.rect_within_screen(rand_location):
                    rand_location = (random.randrange(buffer, Utils.screen.get_rect().right - buffer),
                                     random.randrange(buffer, Utils.screen.get_rect().bottom - buffer))
                spawn_sprite(rand_location, "Resources/sprites/plant.png", "plant")
                display_population_count(Global.plant_group, 2)

        if len(Global.bee_group) > 0 or first_generation:
            rand_location = (random.randint(buffer, Utils.screen.get_rect().right - buffer),
                             random.randint(buffer, Utils.screen.get_rect().bottom - buffer))
            while not Utils.rect_within_screen(rand_location):
                rand_location = (random.randrange(buffer, Utils.screen.get_rect().right - buffer),
                                 random.randrange(buffer, Utils.screen.get_rect().bottom - buffer))
            spawn_sprite(rand_location, "Resources/sprites/bees.png", "bees")
            display_population_count(Global.bee_group, 3)


def create_sprite(location, image_name, animal_name):
    image = pygame.image.load(image_name)
    image_rect = Rect(location, (24, 24))
    new_sprite = Sprite(image, image_rect, animal_name)
    return new_sprite


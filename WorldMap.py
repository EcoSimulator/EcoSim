# Matthew Severance, 4/18/5016

import sys

import pygame
from pygame.locals import *

import Global
import Utils
from Menus import Mouse, Pause, InGameMenu
from SpriteGroups.BeeGroup import BeeGroup
from SpriteGroups.DeerGroup import DeerGroup
from SpriteGroups.PlantGroup import PlantGroup
from SpriteGroups.WolfGroup import WolfGroup
from Sprites import SpriteProduction


# displays the map, initializes terrain and buttons
def display_map():
    # return to main menu
    Global.return_to_menu = False

    # just a random size
    pygame.display.set_caption("Environment Simulator")     # write the caption

    # sets the terrain to an image
    terrain = pygame.image.load(Utils.map)
    terrain_rect = Rect((0, 0), Utils.screen_size)

    # blit the terrain image to the screen
    Utils.screen.blit(terrain, terrain_rect)

    buttons = InGameMenu.make_buttons()   # the list of buttons, its a list of tuples [(image, image_rectangle)]
    Global.buttons_global = buttons

    # loop to listen on the mouse, delayed cuz otherwise stuff flickers
    count = 0
    SpriteProduction.reproduce(count, True)
    while True:

        if Global.return_to_menu:
            empty_all_groups()
            return
        
        Mouse.mouse_monitor(buttons)
        SpriteProduction.display_population_count(Global.deer_group, 0)
        SpriteProduction.display_population_count(Global.wolf_group, 1)
        SpriteProduction.display_population_count(Global.plant_group, 2)
        SpriteProduction.display_population_count(Global.bee_group, 3)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = True
                    Pause.pause(paused)
            if event.type == pygame.QUIT:
                sys.exit()
        if len(Global.wolf_group) > 0:
            Global.wolf_group.update()
        if len(Global.deer_group) > 0:
            Global.deer_group.update()
        if len(Global.bee_group) > 0:
            Global.bee_group.update()
        if len(Global.plant_group) > 0:
            Global.plant_group.update()
        SpriteProduction.reproduce(count)
        pygame.time.delay(100)
        count += 1
        if count > 1000:
            count = 0


def empty_all_groups():
    Global.deer_group = DeerGroup()
    Global.wolf_group = WolfGroup()
    Global.plant_group = PlantGroup()
    Global.bee_group = BeeGroup()

import random
import pygame
import Global
import SpriteProduction
import Utils
from Sprite import Sprite

__author__ = "Matthew Severance"
__date__ = "4/25/2016"


class PlantSprite(Sprite):
    """
    Plant sprite class
    """
    def __init__(self, rect, is_pollinated=False):
        """
        Calls Spite.init as super
        Sets speed, radius and is_pollinated (a boolean)
        Adds to global plant_group
        Loads pollinated image if is_pollinated
        """
        Sprite.__init__(self, pygame.image.load("Resources/sprites/plant.png"), rect, "plant")
        self.screen = Utils.screen
        self.is_pollinated = is_pollinated
        Global.plant_group.add_internal(self)
        if self.is_pollinated:
            self.image = pygame.image.load("Resources/sprites/plantpollinated.png")

    def pollinate(self):
        """
        Sets is_pollinated to True and loads pollinated image
        Randomly generates between 1 and 3 (pollinated) plants
            in a grid around the plant
        """
        self.is_pollinated = True
        self.image = pygame.image.load("Resources/sprites/plantpollinated.png")
        rand = random.randint(1, 3)
        master_location_list = [(self.rect.left, self.rect.top + 40),
                                (self.rect.left, self.rect.top - 40),
                                (self.rect.left + 40, self.rect.top),
                                (self.rect.left - 40, self.rect.top),
                                (self.rect.left - 40, self.rect.top + 40),
                                (self.rect.left + 40, self.rect.top + 40),
                                (self.rect.left - 40, self.rect.top - 40),
                                (self.rect.left + 40, self.rect.top - 40)
                                ]
        current_list = []
        for num in range(0, rand):
            rand_index = random.randint(0, len(master_location_list)-1)
            if Utils.rect_within_screen(master_location_list[rand_index]):
                current_list.append(master_location_list.pop(rand_index))

        for new_location in current_list:
            SpriteProduction.spawn_sprite(new_location, "Resources/sprites/plant.png", self.type, True)

    def update(self):
        """
        Updates the plant sprite
        Just decreases health until death
        """
        Sprite.button_ops(self)
        self.health_monitor()
        self.blit()

    def health_monitor(self):
        """
        Decreases the sprite's health each update
        Returns true and kills the sprite if health <= 0
        """
        self.health -= 1
        if self.health <= 0:
            dirtyrect = Utils.clean_screen.subsurface(self.rect).copy()
            self.screen.blit(dirtyrect, self.rect)
            pygame.display.flip()
            Global.plant_group.remove_internal(self)
            return True

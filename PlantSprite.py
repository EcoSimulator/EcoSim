# Matthew Severance, 4/25/2016


from Sprite import Sprite
import WorldMap
import pygame
import random
import Utils


class PlantSprite(Sprite):

    def __init__(self, rect, is_pollinated=False):
        Sprite.__init__(self, pygame.image.load("Resources/sprites/plant.png"), rect, "plant")
        self.screen = Utils.screen
        self.is_pollinated = is_pollinated
        WorldMap.plant_group.add_internal(self)

    def pollinate(self):
        self.is_pollinated = True
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
            WorldMap.spawn_sprite(new_location, "Resources/sprites/plant.png", self.type, True)

    def update(self):
        self.health -= 1
        self.blit()

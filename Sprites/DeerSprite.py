# Matthew Severance, 4/18/2016

import math
import random

import pygame

import Global
import Utils
from Sprite import Sprite


class DeerSprite(Sprite):

    def __init__(self, image_rect):
        Sprite.__init__(self, pygame.image.load("Resources/sprites/deer.png"), image_rect, "deer")
        self.speed = 24
        self.radius = 100
        self.runningAway = False
        Global.deer_group.add_internal(self)

    def update(self):
        Sprite.button_ops(self)
        if self.health_monitor():
            return
        # for all wolves in collide circle
        if not self.flee():
            self.runningAway = False
            if not Sprite.hunt(self, Global.plant_group):
                Sprite.update(self)

    def flee(self):
        sprite_list = pygame.sprite.spritecollide(self, Global.wolf_group, False, pygame.sprite.collide_circle)
        if len(sprite_list) > 0:
            wolf = Utils.find_closest_sprite(self, sprite_list)
            direction_x = wolf.rect.centerx
            direction_y = wolf.rect.centery
            distance = Utils.distance(self.rect.centerx, self.rect.centery, direction_x, direction_y)

            # If recognizes wolf, run opposite ( determined by wolf's steath )
            if self.runningAway or random.randrange(1, 100) - (distance / 10) > wolf.stealth:
                self.runningAway = True
                move_to_x = self.speed * (self.rect.centerx - direction_x) / distance
                move_to_y = self.speed * (self.rect.centery - direction_y) / distance

                theta = int(math.degrees(math.atan(move_to_y / (move_to_x + .00001))))

                if direction_x > self.rect.centerx:
                    direction = math.radians(random.randrange(theta + 135, theta + 225))
                else:
                    direction = math.radians(random.randrange(theta - 45, theta + 45))

                move_to_x = self.speed * math.sin(direction)
                move_to_y = self.speed * math.cos(direction)
                if self.move_is_within_surface(move_to_x, move_to_y):
                    dirtyrect = Utils.clean_screen.subsurface(self.rect).copy()
                    self.screen.blit(dirtyrect, self.rect)
                    self.rect.move_ip(move_to_x, move_to_y)
                    self.blit()
                    # direction = self.make_good_move(x_offset, y_offset)
                    # x_offset = self.speed * math.cos(direction)
                    # y_offset = self.speed * math.sin(direction)
                else:
                    Sprite.update(self)
                    # direction = self.make_good_move_flee(move_to_x, move_to_y, wolf)
                    # move_to_x = self.speed * math.sin(direction)
                    # move_to_y = self.speed * math.cos(direction)
                    # dirtyrect = Utils.clean_screen.subsurface(self.rect).copy()
                    # self.screen.blit(dirtyrect, self.rect)
                    # self.rect.move_ip(move_to_x, move_to_y)
                    # self.blit()
            pygame.display.flip()
            pygame.time.delay(100)
            return True
        else:
            return False

    def health_monitor(self):
        self.health -= 1
        if self.health <= 0:
            dirtyrect = Utils.clean_screen.subsurface(self.rect).copy()
            self.screen.blit(dirtyrect, self.rect)
            pygame.display.flip()
            Global.deer_group.remove_internal(self)
            return True

    # def make_good_move_flee(self, x_offset, y_offset, wolf):
    #         buffer = 50  # 50 pixel buffer from edge
    #         if self.rect.left + x_offset <= self.screen.get_rect().left + buffer:
    #             if self.rect.top + y_offset <= self.screen.get_rect().top + buffer:
    #                 if wolf.rect.centery >= wolf.rect.centerx:
    #                     return math.radians(random.randint(275, 305))  # top left, wolf above
    #                 else:
    #                     return math.radians(random.randint(325, 355))  # top left, wolf below
    #
    #             if self.rect.bottom + y_offset >= self.screen.get_rect().bottom - buffer:
    #                 if wolf.rect.centery >= wolf.rect.centerx:
    #                     return math.radians(random.randint(5, 35))  # bottom left, wolf above
    #                 else:
    #                     return math.radians(random.randint(55, 85))  # bottom left, wolf below
    #
    #             if wolf.rect.centery > self.rect.centery:
    #                 return math.radians(random.randint(25, 85))  # just left, wolf below
    #             else:
    #                 return math.radians(random.randint(275, 335))   # just left, wolf above
    #
    #         if self.rect.right + x_offset >= self.screen.get_rect().right - buffer:
    #             if self.rect.top + y_offset <= self.screen.get_rect().top + buffer:
    #                 if wolf.rect.centery >= wolf.rect.centerx:
    #                     return math.radians(random.randint(185, 215))  # top right, wolf above
    #                 else:
    #                     return math.radians(random.randint(235, 265))  # top right, wolf below
    #
    #             if self.rect.bottom + y_offset >= self.screen.get_rect().bottom - buffer:
    #                 if wolf.rect.centery >= wolf.rect.centerx:
    #                     return math.radians(random.randint(145, 175))  # bottom right, wolf above
    #                 else:
    #                     return math.radians(random.randint(95, 125))  # bottom right, wolf below
    #
    #             return math.radians(random.randint(95, 265))  # just right
    #
    #         if self.rect.top + y_offset <= self.screen.get_rect().top + buffer:
    #             if wolf.rect.centerx > self.rect.centerx:
    #                 return math.radians(random.randint(185, 245))  # just top, wolf on right
    #             else:
    #                 return math.radians(random.randint(295, 355))  # just top, wolf on left
    #
    #         if self.rect.bottom + y_offset >= self.screen.get_rect().bottom - buffer:
    #             if wolf.rect.centerx > self.rect.centerx:
    #                 return math.radians(random.randint(115, 175))  # just bottom, wolf on right
    #             else:
    #                 return math.radians(random.randint(5, 65))  # just bottom, wolf on left


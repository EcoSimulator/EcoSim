# Matthew Severance, 4/18/2016

from Sprite import Sprite
import WorldMap
import pygame
import random
import WolfSprite
import math
import Utils

class DeerSprite(Sprite):

    def __init__(self, image, image_rect, type, screen):
        Sprite.__init__(self, image, image_rect, type, screen)
        self.speed = 24
        self.radius = 100
        self.runningAway = False

    def update(self):
        #for all wolves in collide circle
        sprite_list = pygame.sprite.spritecollide(self, WorldMap.wolf_group, False, pygame.sprite.collide_circle)
        if len(sprite_list) > 0:
            wolf = Utils.find_closest_sprite(self, sprite_list)
            direction_x = wolf.rect.centerx
            direction_y = wolf.rect.centery
            distance = Utils.distance(self.rect.centerx, self.rect.centery, direction_x, direction_y)

            # If recognizes wolf, run opposite ( determined by wolf's steath )
            if self.runningAway or random.randrange(1, 100)-(distance/10) > wolf.stealth :
                self.runningAway = True
                move_to_x = int(self.speed * (self.rect.centerx - direction_x) / distance)
                move_to_y = int(self.speed * (self.rect.centery - direction_y) / distance)

                direction = random.randrange(90, 270)
                #move_to_x *= math.cos(direction)
                #move_to_y *= self.speed * math.sin(direction)
                if self.move_is_within_surface(move_to_x, move_to_y):
                    dirtyrect = Utils.clean_screen.subsurface(self.rect).copy()
                    self.screen.blit(dirtyrect, self.rect)
                    self.rect.move_ip(move_to_x, move_to_y)
                    self.blit()
                    #direction = self.make_good_move(x_offset, y_offset)
                    #x_offset = self.speed * math.cos(direction)
                    #y_offset = self.speed * math.sin(direction)
                else:
                    Sprite.update(self)
                #move_to_x = move_to_x + int(math.cos(theta))
                #move_to_y = move_to_y + int(math.sin(theta))

            pygame.display.flip()
            pygame.time.delay(100)
        else:
            Sprite.update(self)
            self.runningAway = False
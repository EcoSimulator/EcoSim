# Matthew Severance, 4/18/2016


from Sprite import Sprite
import WorldMap
import pygame
import math
import Utils


class WolfSprite(Sprite):

    def __init__(self, image, image_rect, type, screen):
        Sprite.__init__(self, image, image_rect, type, screen)
        self.speed = 15
        self.radius = 150

    def update(self):
        sprite_list = pygame.sprite.spritecollide(self, WorldMap.deer_group, False, pygame.sprite.collide_circle)
        if len(sprite_list) > 0:
            deer = Utils.find_closest_sprite(self, sprite_list)
            direction_x = deer.rect.centerx
            direction_y = deer.rect.centery
            distance = Utils.distance(self.rect.centerx, self.rect.centery, direction_x, direction_y)
            move_to_x = int(self.speed * (direction_x - self.rect.centerx)/distance)
            move_to_y = int(self.speed * (direction_y - self.rect.centery)/distance)
            dirtyrect = Utils.clean_screen.subsurface(self.rect).copy()
            self.screen.blit(dirtyrect, self.rect)
            self.rect.move_ip(move_to_x, move_to_y)
            self.blit()
            if pygame.sprite.collide_rect(self, deer):
                WorldMap.deer_group.remove_internal(deer)
                dirtyrect = Utils.clean_screen.subsurface(deer.rect).copy()
                self.screen.blit(dirtyrect, deer.rect)
                pygame.display.flip()
                # Utils.output_message(self.screen, "A wolf killed a deer.")
            pygame.display.flip()
            pygame.time.delay(100)
        else:
            Sprite.update(self)



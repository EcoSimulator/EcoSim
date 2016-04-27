# Matthew Severance, 4/18/2016


import pygame
import random
import math
import Utils


class Sprite(pygame.sprite.DirtySprite):

    def __init__(self, image, rect, type):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 10
        self.image = image
        self.rect = rect
        self.type = type
        self.screen = Utils.screen
        self.health = 100

    def add_internal(self, group):
        pygame.sprite.Sprite.add_internal(group)

    def remove_internal(self, group):
        pygame.sprite.Sprite.remove_internal(group)

    def blit(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        direction = math.radians(random.randint(0, 360))
        x_offset = self.speed * math.sin(direction)
        y_offset = self.speed * math.cos(direction)
        while not self.move_is_within_surface(x_offset, y_offset):
            direction = self.make_good_move(x_offset, y_offset)
            x_offset = self.speed * math.sin(direction)
            y_offset = self.speed * math.cos(direction)
        dirty_rect = Utils.clean_screen.subsurface(self.rect).copy()
        self.screen.blit(dirty_rect, self.rect)
        self.rect.move_ip(x_offset, y_offset)
        self.blit()
        pygame.display.flip()
        pygame.time.delay(100)
        # rect.clamp moves one rectangle inside another
        # good for wolf catching deer probably

    def make_good_move(self, x_offset, y_offset):
        buffer = 50     # 50 pixel buffer from edge
        if self.rect.left + x_offset <= self.screen.get_rect().left + buffer:
            if self.rect.top + y_offset <= self.screen.get_rect().top + buffer:
                return math.radians(random.randint(275, 355))   # top left
            if self.rect.bottom + y_offset >= self.screen.get_rect().bottom - buffer:
                return math.radians(random.randint(5, 85))      # bottom left
            return math.radians(random.randint(-85, 85))        # just left

        if self.rect.right + x_offset >= self.screen.get_rect().right - buffer:
            if self.rect.top + y_offset <= self.screen.get_rect().top + buffer:
                return math.radians(random.randint(185, 265))   # top right
            if self.rect.bottom + y_offset >= self.screen.get_rect().bottom - buffer:
                return math.radians(random.randint(95, 175))    # bottom right
            return math.radians(random.randint(95, 265))        # just right

        if self.rect.top + y_offset <= self.screen.get_rect().top + buffer:
            return math.radians(random.randint(185, 355))       # just top

        if self.rect.bottom + y_offset >= self.screen.get_rect().bottom - buffer:
            return math.radians(random.randint(5, 175))         # just bottom

    def move_is_within_surface(self, x_offset, y_offset):
        buffer = 50     # 50 pixel buffer from edge
        if self.rect.left + x_offset <= self.screen.get_rect().left + buffer:
            return False
        if self.rect.right + x_offset >= self.screen.get_rect().right - buffer:
            return False
        if self.rect.top + y_offset <= self.screen.get_rect().top + buffer:
            return False
        if self.rect.bottom + y_offset >= self.screen.get_rect().bottom - buffer:
            return False
        return True

    def hunt(self, group):
        sprite_list = pygame.sprite.spritecollide(self, group, False, pygame.sprite.collide_circle)
        if len(sprite_list) > 0:
            sprite = Utils.find_closest_sprite(self, sprite_list)
            direction_x = sprite.rect.centerx
            direction_y = sprite.rect.centery
            distance = Utils.distance(self.rect.centerx, self.rect.centery, direction_x, direction_y)
            move_to_x = int(self.speed * (direction_x - self.rect.centerx) / distance)
            move_to_y = int(self.speed * (direction_y - self.rect.centery) / distance)
            dirtyrect = Utils.clean_screen.subsurface(self.rect).copy()
            self.screen.blit(dirtyrect, self.rect)
            self.rect.move_ip(move_to_x, move_to_y)
            self.blit()
            if pygame.sprite.collide_rect(self, sprite):
                self.health += 20
                group.remove_internal(sprite)
                dirtyrect = Utils.clean_screen.subsurface(sprite.rect).copy()
                self.screen.blit(dirtyrect, sprite.rect)
                pygame.display.flip()
                # Utils.output_message(self.screen, "A wolf killed a deer.")
            pygame.display.flip()
            pygame.time.delay(100)
            return True
        else:
            return False
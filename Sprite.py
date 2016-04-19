# Matthew Severance, 4/18/2016


import pygame
import random
import math
import Utils


class Sprite(pygame.sprite.DirtySprite):

    def __init__(self, image, rect, type, screen):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = rect
        self.type = type
        self.screen = screen
        self.speed = 10

    def add_internal(self, group):
        pygame.sprite.Sprite.add_internal(self, group)

    def remove_internal(self, group):
        pygame.sprite.Sprite.remove_internal(self, group)

    def blit(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        direction = math.radians(random.randint(0, 360))
        x_offset = self.speed * math.cos(direction)
        y_offset = self.speed * math.sin(direction)
        while not self.move_is_within_surface(x_offset, y_offset):
            direction = self.make_good_move(x_offset, y_offset)
            x_offset = self.speed * math.cos(direction)
            y_offset = self.speed * math.sin(direction)
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
        if self.rect.left + x_offset <= self.screen.get_bounding_rect().left + buffer:
            if self.rect.top + y_offset <= self.screen.get_bounding_rect().top + buffer:
                return math.radians(random.randint(275, 355))   # top left
            if self.rect.bottom + y_offset >= self.screen.get_bounding_rect().bottom - buffer:
                return math.radians(random.randint(5, 85))      # bottom left
            return math.radians(random.randint(-85, 85))        # just left

        if self.rect.right + x_offset >= self.screen.get_bounding_rect().right - buffer:
            if self.rect.top + y_offset <= self.screen.get_bounding_rect().top + buffer:
                return math.radians(random.randint(185, 265))   # top right
            if self.rect.bottom + y_offset >= self.screen.get_bounding_rect().bottom - buffer:
                return math.radians(random.randint(95, 175))    # bottom right
            return math.radians(random.randint(95, 265))        # just right

        if self.rect.top + y_offset <= self.screen.get_bounding_rect().top + buffer:
            return math.radians(random.randint(185, 355))       # just top

        if self.rect.bottom + y_offset >= self.screen.get_bounding_rect().bottom - buffer:
            return math.radians(random.randint(5, 175))         # just bottom

    def move_is_within_surface(self, x_offset, y_offset):
        buffer = 50     # 50 pixel buffer from edge
        if self.rect.left + x_offset <= self.screen.get_bounding_rect().left + buffer:
            return False
        if self.rect.right + x_offset >= self.screen.get_bounding_rect().right - buffer:
            return False
        if self.rect.top + y_offset <= self.screen.get_bounding_rect().top + buffer:
            return False
        if self.rect.bottom + y_offset >= self.screen.get_bounding_rect().bottom - buffer:
            return False
        return True

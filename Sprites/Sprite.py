import math
import random
import sys
import pygame
import Utils
from Menus import Pause

__author__ = "Matthew Severance"
__date__ = "4/18/2016"


class Sprite(pygame.sprite.DirtySprite):
    """
    Default sprite class
    All (move-able) sprites should inherit from this
    """
    def __init__(self, image, rect, type):
        """
        Initializes a blank sprite
        Should not be called on its own
            only as super in another __init__
        Sets health = 100 (max-health, once implemented)
        """
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
        """
        Default sprite update
        Simply makes a random move, staying withing the screen
        """
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
        """
        Called after an attempt by a sprite to move off screen
        Returns an appropriate move depending on what edge
            the sprite is attempting to move off of
        """
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
        """
        Checks whether a sprite's move keeps it within the bounds of the screen
        """
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
        """
        Hunt function for sprites
        Distinguishes between different species and their appropriate prey
        Sprite travels in a straight line towards prey
            Until it catches it or the prey escapes
        """
        sprite_list = pygame.sprite.spritecollide(self, group, False, pygame.sprite.collide_circle)
        if len(sprite_list) > 0:
            sprite = Utils.find_closest_sprite(self, sprite_list)
            while self.type == "bees" and sprite.type == "plant" and sprite.is_pollinated:
                if len(sprite_list) - 1 >= 0:
                    return False
                sprite_list.remove(sprite)
                sprite = Utils.find_closest_sprite(self, sprite_list)
            direction_x = sprite.rect.centerx
            direction_y = sprite.rect.centery
            distance = Utils.distance(self.rect.centerx, self.rect.centery, direction_x, direction_y)
            if distance == 0:
                distance = .1
            move_to_x = int(self.speed * (direction_x - self.rect.centerx) / distance)
            move_to_y = int(self.speed * (direction_y - self.rect.centery) / distance)
            dirtyrect = Utils.clean_screen.subsurface(self.rect).copy()
            self.screen.blit(dirtyrect, self.rect)
            self.rect.move_ip(move_to_x, move_to_y)
            self.blit()
            if pygame.sprite.collide_rect(self, sprite):
                if self.type == "wolf":
                    self.health += 20
                    group.remove_internal(sprite)
                    dirtyrect = Utils.clean_screen.subsurface(sprite.rect).copy()
                    self.screen.blit(dirtyrect, sprite.rect)
                    pygame.display.flip()
                    # Utils.output_message(self.screen, "A wolf killed a deer.")
                elif self.type == "deer":
                    self.health += 20
                    group.remove_internal(sprite)
                    dirtyrect = Utils.clean_screen.subsurface(sprite.rect).copy()
                    self.screen.blit(dirtyrect, sprite.rect)
                    pygame.display.flip()
                elif self.type == "bees":
                    if sprite.type == "plant" and sprite.is_pollinated:
                        return False
                    else:
                        self.health += 20
                        sprite.pollinate()
            pygame.display.flip()
            pygame.time.delay(100)
            return True
        else:
            return False

    def button_ops(self):
        """
        Checks for pause menu call with ESC key
        """
        # Mouse.mouse_monitor(Global.buttons_global)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = True
                    Pause.pause(paused)
            if event.type == pygame.QUIT:
                sys.exit()

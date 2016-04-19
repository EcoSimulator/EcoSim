# Matthew Severance, 4/18/2016


import pygame
import math

clean_screen = pygame.image.load("Resources/randomterrain.jpg")


def output_message(screen, message):
    myfont = pygame.font.SysFont("monospace", 15)
    label = myfont.render(message, 1, (255, 255, 0))
    screen.blit(label, (100, 100))


def distance(x_1, y_1, x_2, y_2):
    return math.sqrt((x_2 - x_1)**2 + (y_2 - y_1)**2)


def find_closest_sprite(target, sprite_list):
    closest = sprite_list[0]
    dist = distance(target.rect.centerx, target.rect.centery, closest.rect.centerx, closest.rect.centery)
    for sprite in sprite_list:
        if dist > abs(distance(target.rect.centerx, target.rect.centery, sprite.rect.centerx, sprite.rect.centery)):
            closest = sprite
    return closest


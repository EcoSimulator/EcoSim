# Matthew Severance, 4/18/2016


import pygame
import math

map = "Resources/terrain/map1.png"

clean_screen = pygame.image.load(map)

screen_size = 1280, 720

screen = pygame.display.set_mode(screen_size)  # creates the screen, add in pygame.FULLSCREEN to fullscreen


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
            # if sprite.type == "plant" and not sprite.is_pollinated:
                closest = sprite
    return closest


def rect_within_screen(loc):
    rect = pygame.Rect(loc[0], loc[1], 24, 24)
    buffer = 50  # 50 pixel buffer from edge
    if rect.left <= screen.get_rect().left + buffer:
        return False
    if rect.right >= screen.get_rect().right - buffer:
        return False
    if rect.top <= screen.get_rect().top + buffer:
        return False
    if rect.bottom >= screen.get_rect().bottom - buffer:
        return False
    return True

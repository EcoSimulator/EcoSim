# Matthew Severance, 4/18/2016


import pygame

clean_screen = pygame.image.load("Resources/randomterrain.jpg")


def output_message(screen, message):
    myfont = pygame.font.SysFont("monospace", 15)
    label = myfont.render(message, 1, (255, 255, 0))
    screen.blit(label, (100, 100))

import pygame
from pygame.locals import *
import Utils
import sys
import Global

"""
The Pause menu
"""

# pause menu stuff, may want to put all of this in its own file
def pause(paused):
    """
    Entry point to pause menu
    Called with ESC key from the running game
    :param paused: boolean indicating paused state
    :return: void
    """
    buttons = make_pause_buttons()

    while paused:
        if (pause_menu_monitor(buttons)) == 0:
            paused = False
            terrain = pygame.image.load(Utils.map)
            terrain_rect = Rect((0, 0), Utils.screen_size)
            Utils.screen.blit(terrain, terrain_rect)
            pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False
                    terrain = pygame.image.load(Utils.map)
                    terrain_rect = Rect((0, 0), Utils.screen_size)
                    Utils.screen.blit(terrain, terrain_rect)
                    pygame.display.flip()
                    break


def make_pause_buttons():
    """
    Creates the list of buttons in the pause menu and blits them to the screen
    0: Resume
    1: Main Menu
    2: Full Screen (Toggle)
    3: Quit
    :param self: GameMenu
    :return: the list of buttons
    """
    center_x = Utils.screen.get_rect().width / 2
    center_y = Utils.screen.get_rect().height / 2
    buttons = []

    paused_label = pygame.image.load("Resources/buttons/paused.png")
    paused_label_rect = Rect((center_x-116, center_y-115), (216, 36))
    resume_button = pygame.image.load("Resources/buttons/resumenormal.png")
    resume_button_rect = Rect((center_x-75, center_y-50), (129, 39))
    mainmenu_button = pygame.image.load("Resources/buttons/mainmenunormal.png")
    mainmenu_button_rect = Rect((center_x - 116, center_y -10), (201, 39))
    fullscreen_botton = pygame.image.load("Resources/buttons/fullscreennormal.png")
    fullscreen_botton_rect = Rect((center_x - 147, center_y - 50), (201, 39))
    quit_button = pygame.image.load("Resources/buttons/quitnormal.png")
    quit_button_rect = Rect((center_x-75, center_y+32), (129, 39))

    paused_label_rect.centerx = center_x
    resume_button_rect.top = paused_label_rect.bottom + 10
    resume_button_rect.centerx = center_x
    mainmenu_button_rect.top = resume_button_rect.bottom + 10
    mainmenu_button_rect.centerx = center_x
    fullscreen_botton_rect.top = mainmenu_button_rect.bottom + 10
    fullscreen_botton_rect.centerx = center_x
    quit_button_rect.top = fullscreen_botton_rect.bottom + 10
    quit_button_rect.centerx = center_x

    buttons.append((resume_button, resume_button_rect))
    buttons.append((mainmenu_button, mainmenu_button_rect))
    buttons.append((fullscreen_botton, fullscreen_botton_rect))
    buttons.append((quit_button, quit_button_rect))

    Utils.screen.blit(paused_label, paused_label_rect)
    for button in buttons:
        Utils.screen.blit(button[0], button[1])
    pygame.display.flip()
    return buttons


def pause_menu_monitor(buttons):
    """
    Watches the mouse to detect hovering over and selection of buttons
    :param buttons: the buttons to watch
    :return: option (which buttons selected)
    """
    global return_to_menu
    mouse = pygame.mouse    # our mouse from now on
    mouse_pos = mouse.get_pos()     # the position of the mouse
    resume = 0
    for button in buttons:
        # while the mouse is within the bounds of any button in the button list
        while (button[1].left < mouse_pos[0] < button[1].right and
                button[1].top < mouse_pos[1] < button[1].bottom):
            # button[0] = resume
            if buttons.index(button) == 0:
                resume_button = pygame.image.load("Resources/buttons/resumeselected.png")
                Utils.screen.blit(resume_button, button[1])
                pygame.display.flip()
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        return resume
            # button[1] = menu
            elif buttons.index(button) == 1:
                mainmenu_button = pygame.image.load("Resources/buttons/mainmenuselected.png")
                Utils.screen.blit(mainmenu_button, button[1])
                pygame.display.flip()
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        Global.return_to_menu = True

                        return resume
            # button[2] = fullscreen
            elif buttons.index(button) == 2:
                fullscreen_button = pygame.image.load("Resources/buttons/fullscreenselected.png")
                Utils.screen.blit(fullscreen_button, button[1])
                pygame.display.flip()
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        if not Utils.screen.get_flags() == FULLSCREEN:
                            pygame.display.set_mode(Utils.screen_size, pygame.FULLSCREEN)
                        else:
                            pygame.display.set_mode(Utils.screen_size)
                        Utils.screen.blit(pygame.image.load(Utils.map), Utils.screen.get_rect())
                        pygame.display.flip()
            # button[3] = quit
            elif buttons.index(button) == 3:
                quit_button = pygame.image.load("Resources/buttons/quitselected.png")
                Utils.screen.blit(quit_button, button[1])
                pygame.display.flip()
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        sys.exit()
            # update position for while loop
            mouse_pos = mouse.get_pos()
    # return buttons to normal
    for button in buttons:
        Utils.screen.blit(button[0], button[1])
    pygame.display.flip()

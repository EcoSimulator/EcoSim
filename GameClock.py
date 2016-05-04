# Jasmine Oliveira
# 4/27/2016

import time
import threading
import pygame, sys
from pygame.locals import *
import Utils

#timer clock
global timerrun #I added this to show / hide the clock from my main screen


class GameClock (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        # clock_font = pygame.font.SysFont("monospace", 60)  # font to use for timer clock
        t0 = time.clock()
        count = 0
        display(count)
        while True:
            count+=1
            wait()
            display(count)

def wait():
    time.sleep(2.5)

def display(count):
    clock_font =  pygame.font.SysFont("monospace", 28, True, False);
    label = clock_font.render(str(count), 1, (255, 255, 255))

    # reset view
    dirty_rect = Utils.clean_screen.subsurface(Rect((100, 0), (40, 39))).copy()
    Utils.screen.blit(dirty_rect, (100, 0))

    # show counter
    #Utils.screen.unlock()
    Utils.screen.blit(label, (100, 0))
    #Utils.screen.lock()
    pygame.display.flip()

#sc = GameClock()
# c = CountDownExec(timeonclock,myAction)

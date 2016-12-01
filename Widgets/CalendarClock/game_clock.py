# -----------------------------------------------------------------------------
# Author: Jasmine Oliveira
# Date:   10/2016
# -----------------------------------------------------------------------------
# game_clock.py
# -----------------------------------------------------------------------------
# Module designed to represent and display a calendar game clock to a pygame
# surface.
#
#       Public Functions:
#
#

import pygame
from pygame.locals import *
from virtual_calendar import VirtualCalendar
import time


class GameClock:

    def __init__(self, GRID_LOCK, subsurface, coordinates, font=None):
        """

        :param GRID_LOCK:
        :param subsurface:
        :param coordinates:
        """

        ''' Threading Data '''
        self.GRID_LOCK = GRID_LOCK  # Thread Lock

        ''' Surface Display Data  '''
        self.subsurface = subsurface
        self.clean_subsurface = subsurface.copy()
        self.x = coordinates[0]
        self.y = coordinates[1]
        # need rect size

        ''' Surface Design Data'''
        self.clock_font = pygame.font.SysFont("arial", 28, True, False) if font is None else font

        ''' Calendar Info '''
        self.calendar = VirtualCalendar(30, 11, 2016) ## static date for testing

    def run(self):
        """
        Runs the game clock
        """

        while True:
            self.calendar.get_next_date()   # get the next date in the calendar
            self.display()
            time.sleep(0.5)
            self.calendar.get_next_date()   # get the next date in the calendar
            self.display()

    def display(self):
        """
        Displays the time string, from the current state of the
        VirtualCalendar widget.
        :return:
        """
        # create display string
        the_time = str(self.calendar.get_weekday_abbr()) + "  " + str(self.calendar.get_day()) \
                   + " " + str(self.calendar.get_month_abbr()) + " " + str(self.calendar.get_year())

        # render string to a surface
        time_text = self.clock_font.render(str(the_time), True, (255, 255, 255), (0, 0, 0))

        # Unlock (to be thread safe)
        self.GRID_LOCK.acquire()

        # blit surface to screen
        #self.subsurface.blit(self.clean_subsurface, (self.x, self.y))
        self.subsurface.blit(time_text, (self.x, self.y))

        pygame.display.flip()  # update pygame

        # Release Lock
        self.GRID_LOCK.release()


import pygame
from pygame.locals import *
from virtual_calendar import VirtualCalendar
import time


class GameClock:

    def __init__(self, GRID_LOCK, subsurface, clock, x, y):

        self.GRID_LOCK = GRID_LOCK
        self.calendar = VirtualCalendar(30, 11, 2016) ## for now test
        self.clock = clock
        self.wait = 2
        self.subsurface = subsurface
        self.clean_subsurface = subsurface.copy()
        self.clock_font =  pygame.font.SysFont("arial", 28, True, False);
        self.x = x
        self.y = y

    def run(self):

        while True:
            self.clock.tick(1)
            self.calendar.get_next_date()   # get the next date in the calendar
            self.display()
            time.sleep(0.5)
            self.calendar.get_next_date()   # get the next date in the calendar
            self.display()

    def display(self):

        # create display string
        the_time = str(self.calendar.get_weekday_abbr()) + "  " + str(self.calendar.get_day()) \
                   + " " + str(self.calendar.get_month_abbr()) + " " + str(self.calendar.get_year())

        # render string to a surface
        time_text = self.clock_font.render(str(the_time), True, (255, 255, 255), (0, 0, 0))

        self.GRID_LOCK.acquire()

        # blit surface to screen
        self.subsurface.blit(self.clean_subsurface, (self.x, self.y))
        self.subsurface.blit(time_text, (self.x, self.y))

        pygame.display.flip()  # update pygame
        self.GRID_LOCK.release()


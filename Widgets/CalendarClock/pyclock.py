# -----------------------------------------------------------------------------
# Author: Jasmine Oliveira
# Date:   10/2016
# -----------------------------------------------------------------------------
# virtual_calendar.py
# -----------------------------------------------------------------------------
# Module designed to test game_clock, and multithreading with a pygame display.
# Does test by creating, and running 3 clocks on a single screen.

import pygame
from game_clock import GameClock
import threading
import time
from threading import Thread

pygame.init()

# Get Pygame values
screen = pygame.display.set_mode((800, 600))
surface = pygame.Surface(screen.get_size())
clock = pygame.time.Clock()
GRID_LOCK = threading.Lock()

# Create Clock subsurface
minx = 10
miny = 10
maxx = 50
maxy = 50
r = pygame.Rect(minx,miny,maxx-minx,maxy-miny)
clock_subsurface = surface.subsurface(r)


## Create 3 Game Clocks
game_clock = GameClock(GRID_LOCK, screen, clock, 0, 0)
t = Thread(target=game_clock.run)
t.daemon = True

game_clock2 = GameClock(GRID_LOCK, screen, clock, 0, 50)
s = Thread(target=game_clock2.run)
s.daemon = True

game_clock3 = GameClock(GRID_LOCK, screen, clock, 0, 100)
u = Thread(target=game_clock3.run)
u.daemon = True


# Run the Threads
t.start()
s.start()
u.start()

pygame.init()

# Loop until Pygame exits
done = False
while not done:
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True
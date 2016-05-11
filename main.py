import pygame
import Utils
from Menus import GameMenu
"""
Main driver file
Call this to run program
Calls pygame init, then gamemenu
"""
# the main driver file, s
pygame.init()

# Start Menu (calls WorldMap.display_map)
gm = GameMenu.GameMenu(Utils.screen)
gm.run()

# Display Map
#WorldMap.display_map()

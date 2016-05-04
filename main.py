# Matthew Severance, 4/18/2016

import pygame
import Utils
from Menus import GameMenu

# the main driver file, s
pygame.init()

# Start Menu (calls WorldMap.display_map)
gm = GameMenu.GameMenu(Utils.screen)
gm.run()

# Display Map
#WorldMap.display_map()

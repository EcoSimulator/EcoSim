# Matthew Severance, 4/18/2016

import WorldMap
import GameMenu
import Utils
from DeerGroup import DeerGroup
from WolfGroup import WolfGroup
import pygame

# the main driver file, s
pygame.init()

# Start Menu (calls WorldMap.display_map)
gm = GameMenu.GameMenu(Utils.screen)
gm.run()

# Display Map
#WorldMap.display_map()

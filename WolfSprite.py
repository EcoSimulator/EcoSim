# Matthew Severance, 4/18/2016


from Sprite import Sprite
import WorldMap
import pygame
import math
import Utils

class WolfSprite(Sprite):

    def __init__(self, image, image_rect, type, screen):
        Sprite.__init__(self, image, image_rect, type, screen)

        self.radius = 50

    def update(self):
        Sprite.update(self)
        for deer in WorldMap.deer_group:
            if pygame.sprite.collide_circle(self, deer):
                direction_x = deer.rect.centerx
                direction_y = deer.rect.centery
                magnitude = 10  # change to incorporate speed
                dirtyrect = Utils.clean_screen.subsurface(self.rect).copy()
                self.screen.blit(dirtyrect, self.rect)
                self.rect.move_ip(magnitude * math.cos(direction_x), magnitude * math.sin(direction_y))
                self.blit()
                pygame.display.flip()
                if pygame.sprite.collide_rect(self, deer):
                    WorldMap.deer_group.remove_internal(deer)
                    dirtyrect = Utils.clean_screen.subsurface(deer.rect).copy()
                    self.screen.blit(dirtyrect, deer.rect)
                    pygame.display.flip()
                    # Utils.output_message(self.screen, "A wolf killed a deer.")

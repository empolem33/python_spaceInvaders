import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """a class to represent a single alien in a fleet"""

    def __init__(self, ai_game):
        """initalize alien and set its starting positon"""
        super().__init__()
        self.screen = ai_game.screen

        # load the alien image and set its rect
        self.image = pygame.image.load('assets/pixel_ship_red_small.png')
        self.rect = self.image.get_rect()

        # start each new alien near the top
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

import pygame


class Ship:
    """A class to manage the ship."""
    def __init__(self, ai_game):
        """Initalize the ship and set its starting postion."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # load ship image and get rect
        self.image = pygame.image.load('assets/pixel_ship_red_small.png')
        self.rect = self.image.get_rect()
        # start new ship at bottom center of screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw ship at its current location"""
        self.screen.blit(self.image, self.rect)


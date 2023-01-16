import pygame


class Ship:
    """A class to manage the ship."""
    def __init__(self, ai_game):
        """Initalize the ship and set its starting postion."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # load ship image and get rect
        self.image = pygame.image.load('assets/pixel_ship_yellow.png')
        self.rect = self.image.get_rect()
        # start new ship at bottom center of screen
        self.rect.midbottom = self.screen_rect.midbottom

        # store a decimal value for the ships position
        self.x = float(self.rect.x)

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        # update rect object
        self.rect.x = self.x

    def blitme(self):
        """Draw ship at its current location"""
        self.screen.blit(self.image, self.rect)


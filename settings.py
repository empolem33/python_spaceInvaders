import pygame
class Settings:
    """ A class to store all settings for Alien Invasion."""
    def __init__(self):
        """ initialize the game's settings."""
        # screen settings
        self.screen_width = 870
        self.screen_height = 700
        self.bg = pygame.transform.scale(pygame.image.load("assets/background-black.png"), (self.screen_width, self.screen_height))

        # ship settings
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (3, 248, 252)
        self.bullets_allowed = 3

        # alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1

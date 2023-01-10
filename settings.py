import pygame
class Settings:
    """ A class to store all settings for Alien Invasion."""
    def __init__(self):
        """ initialize the game's settings."""
        # screen settings
        self.screen_width = 800
        self.screen_height = 700
        self.bg = pygame.transform.scale(pygame.image.load("assets/background-black.png"), (self.screen_width, self.screen_height))


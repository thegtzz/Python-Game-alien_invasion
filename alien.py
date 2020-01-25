import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Class represents one alien ship"""
    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.ai_settings = ai_settings
        self.screen = screen

        # Uploading an alien image and rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Every new alien ship appears at position 0, 0
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Saving alien`s ship precise position
        self.x = float(self.rect.x)

    def blitme(self):
        """Shows an alien ship at its current position"""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """Return 'True' if alien ship achieved the end of the screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Moves a ship to the left or right side"""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

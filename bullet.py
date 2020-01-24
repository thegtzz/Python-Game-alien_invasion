import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Class for configuration of ship's bullets"""
    def __init__(self, ai_settings, screen, ship):
        """Creates a bullet at ship's position"""
        super().__init__()
        self.screen = screen

        """Creation of a bullet at (0,0) position"""
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        """Bullet's position is a float"""
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Moves a bullet from bottom to top"""
        self.y -= self.speed_factor
        """Refreshing of rect position"""
        self.rect.y = self.y

    def draw_bullet(self):
        """Drawing a bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)

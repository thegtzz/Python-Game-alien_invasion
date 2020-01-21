import pygame


class Ship:
    def __init__(self, ai_settings,screen):
        """Initialize the ship and its position"""
        self.screen = screen
        self.ai_settings = ai_settings

        """Load the ship image as a rectangular"""
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        """Each ship appears at the bottom center of the screen"""
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)

        """Flag of pushing a ship"""
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Updates ship's position according to flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        # refreshing 'rect' attribute based on 'self.center'
        self.rect.centerx = self.center

    def blitme(self):
        """Draw a ship at the current position"""
        self.screen.blit(self.image, self.rect)

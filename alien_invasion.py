import pygame
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # Initialize a game and creates display-object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Creation of the ship.
    ship = Ship(screen)

    # Background color of the main screen.
    bg_color = (230, 230, 230)

    # Initializing main game loop.
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)


run_game()

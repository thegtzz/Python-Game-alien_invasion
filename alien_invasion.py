import sys
import pygame


def run_game():
    # intialize a game and creates display-object
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")

    # intializing main game loop
    while True:
        # spying keyboard and mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # displaying the last-drawn screen
        pygame.display.flip()

run_game()
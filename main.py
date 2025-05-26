import pygame
from pygame.locals import *
from constants import *


pygame.init()


def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    # ruff: noqa
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.Surface.fill(screen, (0, 0, 0), None, 0)
        pygame.display.flip()


if __name__ == "__main__":
    main()

import pygame
from pygame.locals import *
from constants import *
from player import Player


def main():
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    player = Player(x, y)

    print("Starting Asteroids!")

    # ruff: noqa
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        updatable.update(dt)
        screen.fill("black")
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()

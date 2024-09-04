import pygame
from constants import *


def main():
    print("Starting asteroids!")
    if SCREEN_WIDTH is None:
        raise ValueError("SCREEN_WIDTH is None")
    if SCREEN_HEIGHT is None:
        raise ValueError("SCREEN_HEIGHT is None")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Pygame Window")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        black = (0, 0, 0)
        screen.fill(black)
        pygame.display.flip()


if __name__ == "__main__":
    main()

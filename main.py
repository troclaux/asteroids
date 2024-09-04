import pygame
from constants import *
from player import Player


def main():
    print("Starting asteroids!")
    if SCREEN_WIDTH is None:
        raise ValueError("SCREEN_WIDTH is None")
    if SCREEN_HEIGHT is None:
        raise ValueError("SCREEN_HEIGHT is None")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    x = SCREEN_WIDTH / 2
    y = SCREEN_WIDTH / 2
    player = Player(x, y, PLAYER_RADIUS)

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Pygame Window")

    clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        black = (0, 0, 0)
        screen.fill(black)
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()
        time_passed = clock.tick(60)
        dt = time_passed / 1000


if __name__ == "__main__":
    main()

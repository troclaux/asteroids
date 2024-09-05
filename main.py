import sys
import pygame
from player import *
from constants import *
from asteroidfield import *


def main():

    try:
        if SCREEN_WIDTH is None:
            raise ValueError("SCREEN_WIDTH is None")
        if SCREEN_HEIGHT is None:
            raise ValueError("SCREEN_HEIGHT is None")
        if PLAYER_RADIUS is None:
            raise ValueError("PLAYER_RADIUS is None")
    except ValueError as e:
        print(f"Error: {e}")

    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    x = SCREEN_WIDTH / 2
    y = SCREEN_WIDTH / 2

    player = Player(x, y, PLAYER_RADIUS)
    asteroid_field = AsteroidField()

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

        for object in updatable:
            object.update(dt)
        for object in drawable:
            object.draw(screen)

        for asteroid in asteroids:
            if player.collision(asteroid):
                print("Game over!")
                sys.exit()

        pygame.display.flip()
        time_passed = clock.tick(60)
        dt = time_passed / 1000


if __name__ == "__main__":
    main()

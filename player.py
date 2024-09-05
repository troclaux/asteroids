import pygame
from circleshape import *
from shot import *
from constants import *


class Player(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0
        self.timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        white = (255, 255, 255)
        pygame.draw.polygon(screen, white, self.triangle(), 2)

    def move(self, dt):
        if PLAYER_SPEED is None:
            raise ValueError("PLAYER_SPEED is None")
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def rotate(self, dt):
        if PLAYER_TURN_SPEED is None:
            raise ValueError("PLAYER_TURN_SPEED is None")
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):

        self.timer -= dt

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.move(dt)

        if keys[pygame.K_s]:
            self.move(-dt)

        if keys[pygame.K_a]:
            self.rotate(-dt)

        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_SPACE]:
            self.shoot()

    def shoot(self):
        try:
            if PLAYER_SHOOT_COOLDOWN is None:
                raise ValueError("PLAYER_SHOOT_COOLDOWN is None")
            if PLAYER_SHOOT_SPEED is None:
                raise ValueError("PLAYER_SHOOT_SPEED is None")
        except ValueError as e:
            print(f"Error: {e}")

        if self.timer > 0:
            return

        self.timer = PLAYER_SHOOT_COOLDOWN
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

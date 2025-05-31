import pygame
import random
from asteroid import Asteroid
from constants import (SCREEN_HEIGHT, SCREEN_WIDTH, ASTEROID_MAX_RADIUS, 
                        ASTEROID_MIN_RADIUS, ASTEROID_SPAWN_RATE, ASTEROID_KINDS)


class AsteroidField(pygame.sprite.Sprite):
    """
    AsteroidField is a sprite responsible for spawning and managing asteroids in the game.

    Attributes:
        edges (list): Defines the four edges of the screen where asteroids can spawn. Each edge is represented by a direction vector and a function that generates a spawn position along that edge.

    Methods:
        __init__():
            Initializes the AsteroidField sprite and its spawn timer.

        spawn(radius, position, velocity):
            Creates a new Asteroid instance at the given position, with the specified radius and velocity.

        update(dt):
            Updates the spawn timer. When the timer exceeds ASTEROID_SPAWN_RATE, spawns a new asteroid at a random edge with randomized velocity and size.
    """
    edges = [
        [
            pygame.Vector2(1, 0),
            lambda y: pygame.Vector2(-ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT),
        ],
        [
            pygame.Vector2(-1, 0),
            lambda y: pygame.Vector2(
                SCREEN_WIDTH + ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT
            ),
        ],
        [
            pygame.Vector2(0, 1),
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, -ASTEROID_MAX_RADIUS),
        ],
        [
            pygame.Vector2(0, -1),
            lambda x: pygame.Vector2(
                x * SCREEN_WIDTH, SCREEN_HEIGHT + ASTEROID_MAX_RADIUS
            ),
        ],
    ]

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0

    def spawn(self, radius, position, velocity):
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity

    def update(self, dt):
        self.spawn_timer += dt
        if self.spawn_timer > ASTEROID_SPAWN_RATE:
            self.spawn_timer = 0

            # spawn a new asteroid at a random edge
            edge = random.choice(self.edges)
            speed = random.randint(40, 100)
            velocity = edge[0] * speed
            velocity = velocity.rotate(random.randint(-30, 30))
            position = edge[1](random.uniform(0, 1))
            kind = random.randint(1, ASTEROID_KINDS)
            self.spawn(ASTEROID_MIN_RADIUS * kind, position, velocity)
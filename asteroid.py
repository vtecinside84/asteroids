import pygame
import random
from constants import ASTEROID_MIN_RADIUS
from circleshape import CircleShape

class Asteroid(CircleShape):
    """
    Asteroid class representing an asteroid object in the game.
    Inherits from:
        CircleShape
    Attributes:
        radius (float): The radius of the asteroid.
        position (pygame.Vector2): The current position of the asteroid.
        velocity (pygame.Vector2): The current velocity vector of the asteroid.
    Methods:
        __init__(x, y, radius):
            Initializes an Asteroid instance at position (x, y) with the given radius.
        draw(screen):
            Draws the asteroid as a white circle outline on the provided screen surface.
        update(dt):
            Updates the asteroid's position based on its velocity and the elapsed time (dt).
        split():
            Splits the asteroid into two smaller asteroids if its radius is above the minimum threshold.
            Removes (kills) the current asteroid and spawns two new ones with adjusted velocities and radii.
    """
    def __init__ (self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = radius
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)

    def draw(self, screen):
        return pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
            
    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        avelocity = self.velocity.rotate(angle)
        bvelocity = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        a = Asteroid(
            self.position.x, self.position.y, new_radius
        )
        a.velocity = avelocity*1.2
        b = Asteroid(
            self.position.x, self.position.y, new_radius
        )
        b.velocity = bvelocity*1.2
import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    """
    A base class for circular sprite shapes in a Pygame environment.

    Inherits from:
        pygame.sprite.Sprite

    Attributes:
        position (pygame.Vector2): The position of the circle's center.
        velocity (pygame.Vector2): The velocity vector of the circle.
        radius (float): The radius of the circle.

    Methods:
        draw(screen):
            Draws the circle on the given screen surface.
            This method should be overridden by subclasses.

        update(dt):
            Updates the state of the circle.
            This method should be overridden by subclasses.

        collide(other):
            Determines if this circle collides with another circle-shaped object.
            Args:
                other (CircleShape): Another circle-shaped object.
            Returns:
                bool: True if the circles overlap, False otherwise.
    """
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collide(self, other):
        distance = pygame.Vector2.distance_to(self.position, other.position)
        return distance < (self.radius + other.radius)
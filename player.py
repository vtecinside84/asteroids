import pygame
from circleshape import CircleShape
from constants import (PLAYER_RADIUS, PLAYER_SPEED, PLAYER_TURN_SPEED, 
                        PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN)
from shot import Shot

class Player(CircleShape):
    """
    Player class representing the user-controlled ship in the Asteroids game.
    Inherits from:
        CircleShape
    Attributes:
        rotation (float): The current rotation angle of the player in degrees.
        timer (float): Timer used to control shooting cooldown.
    Methods:
        __init__(x, y):
            Initializes the player at position (x, y) with a predefined radius.
        triangle():
            Calculates and returns the vertices of the player's triangular shape based on its position and rotation.
        draw(screen):
            Draws the player's triangle on the given Pygame screen surface.
        rotate(dt):
            Rotates the player by updating its rotation angle based on the turn speed and delta time.
        shoot():
            Creates a new Shot object at the player's position and sets its velocity in the direction the player is facing.
        update(dt):
            Handles player input for rotation, movement, and shooting. Updates the shooting cooldown timer.
        move(dt):
            Moves the player forward or backward in the direction it is currently facing, based on the speed and delta time.
    """
    def __init__(self,x,y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        return pygame.draw.polygon(screen,"white",self.triangle(),2)

    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)
    
    def shoot(self):
        # create a new shot
        shot = Shot(self.position.x, self.position.y)
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        shot.velocity = forward * PLAYER_SHOOT_SPEED
        

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            # rotate left
            self.rotate(-dt)
        if keys[pygame.K_d]:
            # rotate right
            self.rotate(dt)
        if keys[pygame.K_w]:
            # move forward
            self.move(dt)
        if keys[pygame.K_s]:
            # move backward
            self.move(-dt)
        if keys[pygame.K_SPACE]:
               # shoot
            if self.timer > 0:
                self.timer -= dt    
            else:
                self.shoot()
                self.timer = PLAYER_SHOOT_COOLDOWN
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
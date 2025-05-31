import sys
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from shot import Shot
from asteroidfield import AsteroidField

def main():
    """
    Initializes the Asteroids game, sets up the display, sprite groups, and main game loop.
    - Initializes pygame and creates the main game window.
    - Sets up sprite groups for updateable, drawable, asteroids, and shots.
    - Assigns sprite containers for Player, Asteroid, AsteroidField, and Shot classes.
    - Instantiates the player and asteroid field.
    - Runs the main game loop:
        - Handles quit events.
        - Updates all updateable sprites.
        - Checks for collisions between the player and asteroids (ends game on collision).
        - Checks for collisions between shots and asteroids (splits asteroids and removes shots).
        - Draws all drawable sprites to the screen.
        - Updates the display and manages frame timing.
    """
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    clk = pygame.time.Clock()

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updateable, drawable)
    Asteroid.containers = (updateable, drawable, asteroids)
    AsteroidField.containers = (updateable)
    Shot.containers = (updateable, drawable, shots)
    
    p1 = Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2)
    field = AsteroidField()
    dt = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updateable.update(dt)
        for asteroid in asteroids:
            if asteroid.collide(p1):
                print("Game Over!")
                sys.exit()
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collide(shot):
                    asteroid.split()
                    shot.kill()    
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()
        dt = clk.tick(60) / 1000

if __name__ == "__main__":
    main()

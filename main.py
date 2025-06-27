# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

x = SCREEN_WIDTH / 2
y = SCREEN_HEIGHT / 2

def main():
    print("Starting Asteroids!\n")
    pygame.init()
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    
    player1 = Player(x, y)
    asteroidfield1 = AsteroidField()

    dt = 0

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)

        screen.fill(color="black")                

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        
        for obj in asteroids:
            if obj.collision(player1):
                print("Game Over!")
                sys.exit()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000
         
if __name__ == "__main__":
    main()
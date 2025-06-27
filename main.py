# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
import player

x = SCREEN_WIDTH / 2
y = SCREEN_HEIGHT / 2

def main():
    print("Starting Asteroids!\n")
    pygame.init()
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    player1 = player.Player(x, y)
    clock = pygame.time.Clock()
    dt = 0

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill(color="black")                
        player1.draw(screen)
        player1.update(dt)
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000
         
if __name__ == "__main__":
    main()
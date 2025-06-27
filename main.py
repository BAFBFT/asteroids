# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    pygame.init()
    print("Starting Asteroids!\n")
    print(f"Screen width: {SCREEN_WIDTH}\n")
    print(f"Screen height: {SCREEN_HEIGHT}\n")

if __name__ == "__main__":
    main()
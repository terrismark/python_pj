import pygame  # importing pygame
from pygame.draw import *  # importing all from draw module in pygame

FPS = 60  # FPS of the window with the game
SCREEN_HEIGHT = 400
SCREEN_WIDTH = 400
WHITE = (255, 255, 255)

pygame.init()  # initialising the program

# Screen settings
screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))  # window size
pygame.display.set_caption("Test Game")  # window title
screen.fill(WHITE)  # window background color

clock = pygame.time.Clock()
pygame.display.update()


def main():  # the main function of the game
    run = True
    while run:  # the main loop
        clock.tick(FPS)  # FPS counter
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # checking for quiting
                run = False
                pygame.quit()


if __name__ == "__main__":
    main()

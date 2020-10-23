import pygame  # importing pygame
from pygame.draw import *  # importing all from draw module in pygame

clock = pygame.time.Clock()
FPS = 240  # FPS of the window with the game
SCREEN_HEIGHT = 400
SCREEN_WIDTH = 400
WHITE = [255, 255, 255]

pygame.init()  # initialising the program

# Screen settings
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # window size
pygame.display.set_caption("Test Game 2")  # window title
icon = pygame.image.load('assets/icon.png')  # icon loading
pygame.display.set_icon(icon)  # setting the icon


def draw_objects():
    """
    TODO: make this function
    :return:
    """
    pass


def main():  # the main function of the game
    screen.fill(WHITE)  # window background color
    run = True
    while run:  # the main loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # checking for quiting
                run = False

        pygame.display.flip()  # updating the game window
        clock.tick(FPS)  # FPS counter


if __name__ == "__main__":
    main()

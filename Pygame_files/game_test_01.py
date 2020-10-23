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
pygame.display.set_caption("Test Game")  # window title
icon = pygame.image.load('assets/icon.png')  # icon loading
pygame.display.set_icon(icon)  # setting the icon


# Objects
class Point:
    flag = pygame.image.load('assets/flag.png')  # sizes = 32px * 32px
    flag_x = SCREEN_WIDTH//2
    flag_y = SCREEN_HEIGHT//2

    def __init__(self, x=flag_x, y=flag_y):
        screen.blit(self.flag, (x - 16, y - 16))


def draw_objects():
    """
    TODO: make this function
    :return:
    """
    pass


def main():  # the main function of the game
    x, y = 184, 184
    run = True
    while run:  # the main loop
        screen.fill(WHITE)  # window background color
        Point(x, y)  # creating an object
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                y -= 10
                Point(x, y)

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                y += 10
                Point(x, y)

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                x -= 10
                Point(x, y)

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                x += 10
                Point(x, y)
            if event.type == pygame.QUIT:  # checking for quiting
                run = False

        pygame.display.flip()  # updating the game window
        clock.tick(FPS)  # FPS counter


if __name__ == "__main__":
    main()

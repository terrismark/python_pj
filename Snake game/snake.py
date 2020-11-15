import pygame as pg
import sys
import random as rnd


# snake objects
class Snake:
    def __init__(self):
        self.color = (80, 118, 249)
        self.x = 2
        self.y = (GRID_HEIGHT - 1) // 2
        self.poses = [(self.x * GRID_SIZE, self.y * GRID_SIZE),
                      ((self.x + 1) * GRID_SIZE, self.y * GRID_SIZE)]
        self.direction = (0, 0)
        self.upgrade = False

    def draw(self, surface):
        for i in self.poses:
            snake_body_sell = (i, (GRID_SIZE, GRID_SIZE))
            pg.draw.rect(surface, self.color, snake_body_sell)

    def move(self):
        if not self.upgrade:
            tail = self.poses[:-1]
        else:
            tail = self.poses.copy()
            self.upgrade = False
        moved_body = (tail[0][0] + self.direction[0] * GRID_SIZE, tail[0][1] + self.direction[1] * GRID_SIZE)
        tail.insert(0, moved_body)
        self.poses = tail.copy()

    def size_up(self):
        self.upgrade = True


# apple objects
class Apple:
    def __init__(self):
        self.color = (244, 55, 6)
        self.randomize_pos()

    def draw(self, surface):
        apple_square = (self.pos, (GRID_SIZE, GRID_SIZE))
        pg.draw.rect(surface, self.color, apple_square)

    def randomize_pos(self):
        self.x = rnd.randint(0, GRID_WIDTH-1)
        self.y = rnd.randint(0, GRID_HEIGHT-1)
        self.pos = (self.x * GRID_SIZE, self.y * GRID_SIZE)


# function that draws a grid layout
def draw_grid(surface):
    for i in range(GRID_WIDTH):
        for j in range(GRID_HEIGHT):
            square = pg.Rect((i * GRID_SIZE, j * GRID_SIZE), (GRID_SIZE, GRID_SIZE))
            if (i + j) % 2 == 0:
                pg.draw.rect(surface, (167, 217, 72), square)
            else:
                pg.draw.rect(surface, (132, 189, 53), square)


# screen and grid params
GRID_SIZE = 30
SCREEN_HEIGHT = 420
SCREEN_WIDTH = 420
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# user event
SCREEN_UPDATE = pg.USEREVENT
pg.time.set_timer(SCREEN_UPDATE, 120)


# main function
def main():
    # initializing the game
    pg.init()

    clock = pg.time.Clock()
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
    # making the surface
    surface = pg.Surface(screen.get_size()).convert()

    # initializing game objects
    apple = Apple()
    snake = Snake()
    # game loop
    while True:
        for event in pg.event.get():
            # if quiting
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            # move every (repeating time) milliseconds
            if event.type == SCREEN_UPDATE:
                snake.move()
            if event.type == pg.KEYDOWN:
                # move up if key up is down
                if event.key == pg.K_UP and snake.direction != (0, 1):
                    snake.direction = (0, -1)
                # move down if key down is down
                if event.key == pg.K_DOWN and snake.direction != (0, -1):
                    snake.direction = (0, 1)
                # move right if key right is down
                if event.key == pg.K_RIGHT and snake.direction != (-1, 0):
                    snake.direction = (1, 0)
                # move left if key left is down
                if event.key == pg.K_LEFT and snake.direction != (1, 0):
                    snake.direction = (-1, 0)

        if snake.poses[0] == apple.pos:
            apple.randomize_pos()
            snake.size_up()
        # drawing surface, apple and a snake
        draw_grid(surface)
        apple.draw(surface)
        snake.draw(surface)
        screen.blit(surface, (0, 0))
        pg.display.update()
        clock.tick(60)


main()








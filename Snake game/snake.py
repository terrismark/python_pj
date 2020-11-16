import pygame as pg
import sys
import random as rnd


# snake object
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
        moved_body = (tail[0][0] + self.direction[0] * GRID_SIZE,
                      tail[0][1] + self.direction[1] * GRID_SIZE)
        tail.insert(0, moved_body)
        self.poses = tail.copy()

    def size_up(self):
        self.upgrade = True

    def reset_snake(self):
        self.x = 2
        self.y = (GRID_HEIGHT - 1) // 2
        self.poses = [(self.x * GRID_SIZE, self.y * GRID_SIZE),
                      ((self.x + 1) * GRID_SIZE, self.y * GRID_SIZE)]
        self.direction = (0, 0)


# apple object
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


# main game object
class Game:
    def __init__(self):
        # initializing game objects
        self.apple = Apple()
        self.snake = Snake()

    def draw_objects(self, surface):
        # drawing surface, apple and a snake
        draw_grid(surface)
        self.apple.draw(surface)
        self.snake.draw(surface)

    def update(self):
        # move snake
        self.snake.move()
        # check if snake eats apple
        self.check_collision()
        # check if game over
        self.game_over()

    def event_handler(self):
        for event in pg.event.get():
            # if quiting
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            # move every (repeating time) milliseconds
            if event.type == SCREEN_UPDATE:
                self.update()
            if event.type == pg.KEYDOWN:
                # move up if key up is down
                if event.key == pg.K_UP and self.snake.direction != (0, 1):
                    self.snake.direction = (0, -1)
                # move down if key down is down
                elif event.key == pg.K_DOWN and self.snake.direction != (0, -1):
                    self.snake.direction = (0, 1)
                # move right if key right is down
                elif event.key == pg.K_RIGHT and self.snake.direction != (-1, 0):
                    self.snake.direction = (1, 0)
                # move left if key left is down
                elif event.key == pg.K_LEFT and self.snake.direction != (1, 0):
                    self.snake.direction = (-1, 0)

    # snake functions
    def check_collision(self):
        # if snake eats apple
        if self.snake.poses[0] == self.apple.pos:
            # generating a new apple
            self.apple.randomize_pos()
            # snake size up
            self.snake.size_up()

        for i in self.snake.poses:
            if i == self.apple.pos:
                self.apple.randomize_pos()

    # game over states
    def game_over(self):
        # if snake hits walls
        state_1 = 0 <= self.snake.poses[0][0] < SCREEN_WIDTH
        state_2 = 0 <= self.snake.poses[0][1] < SCREEN_HEIGHT
        if not (state_1 and state_2):
            self.snake.reset_snake()

        # if snake hits itself
        for i in self.snake.poses[1:]:
            if i == self.snake.poses[0]:
                self.snake.reset_snake()


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
SCREEN_HEIGHT = 480
SCREEN_WIDTH = 480
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# moving each (repeat time) milliseconds
repeat_time = 120
SCREEN_UPDATE = pg.USEREVENT
pg.time.set_timer(SCREEN_UPDATE, repeat_time)


# main function
def main():
    # initializing the game
    pg.init()
    clock = pg.time.Clock()

    # making the surface
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
    surface = pg.Surface(screen.get_size()).convert()

    # initializing main Game object
    game = Game()

    # game loop
    while True:
        # event handling
        game.event_handler()

        # drawing surface, apple and a snake
        game.draw_objects(surface)

        # screen update
        screen.blit(surface, (0, 0))
        pg.display.update()
        clock.tick(60)


main()

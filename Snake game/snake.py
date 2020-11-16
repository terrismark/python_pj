import pygame as pg
import sys
import random as rnd


# snake object
class Snake:
    def __init__(self):
        self.color = (80, 118, 249)
        self.x = 2
        self.y = GRID_HEIGHT // 2
        self.poses = [(self.x * GRID_SIZE, self.y * GRID_SIZE),
                      ((self.x + 1) * GRID_SIZE, self.y * GRID_SIZE)]
        self.direction = (0, 0)
        self.upgrade = False
        self.high_score = 0

    def draw(self):
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
        self.y = GRID_HEIGHT // 2
        self.poses = [(self.x * GRID_SIZE, self.y * GRID_SIZE),
                      ((self.x + 1) * GRID_SIZE, self.y * GRID_SIZE)]
        self.direction = (0, 0)


# apple object
class Apple:
    def __init__(self):
        self.color = (244, 55, 6)
        self.randomize_pos()

    def draw(self):
        apple_square = (self.pos, (GRID_SIZE, GRID_SIZE))
        pg.draw.rect(surface, self.color, apple_square)

    def randomize_pos(self):
        self.x = rnd.randint(1, GRID_WIDTH)
        self.y = rnd.randint(1, GRID_HEIGHT)
        self.pos = (self.x * GRID_SIZE, self.y * GRID_SIZE)


# main game object
class Game:
    def __init__(self):
        # initializing game objects
        self.apple = Apple()
        self.snake = Snake()

    def draw_objects(self):
        # drawing surface, apple and a snake
        draw_grid()
        self.apple.draw()
        self.snake.draw()

    # updating the grid snake and apples
    def update(self):
        # move snake
        self.snake.move()
        # check if snake eats apple
        self.check_collision()
        # check if game over
        self.game_over()

    # user event handler
    def event_handler(self):
        for event in pg.event.get():
            # if quiting
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            # move every 120 milliseconds
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
        state_1 = GRID_SIZE <= self.snake.poses[0][0] < SCREEN_WIDTH - 4 * GRID_SIZE
        state_2 = GRID_SIZE <= self.snake.poses[0][1] < SCREEN_HEIGHT - GRID_SIZE
        if not (state_1 and state_2):
            self.snake.reset_snake()

        # if snake hits itself
        for i in self.snake.poses[1:]:
            if i == self.snake.poses[0]:
                self.snake.reset_snake()

        # if snake is overflows all the field
        if len(self.snake.poses) == GRID_WIDTH*GRID_HEIGHT - 1:
            self.snake.reset_snake()


# function that draws score
def draw_score():
    # displaying current score
    score = len(game.snake.poses) - 2
    score_text = score_font.render(str(score), True, (255, 255, 255))

    # text should be on the at the intersection of grid cells
    score_rect = score_text.get_rect(center=(SCREEN_WIDTH - GRID_SIZE, 4*GRID_SIZE))
    screen.blit(score_text, score_rect)

    # high score counting
    if score != 0 and game.snake.high_score < score:
        game.snake.high_score = score

    # displaying high score
    high_score_text = score_font.render(str(game.snake.high_score), True, (255, 255, 255))

    # text should be on the at the intersection of grid cells
    high_score_rect = high_score_text.get_rect(center=(SCREEN_WIDTH - GRID_SIZE, 6*GRID_SIZE))
    screen.blit(high_score_text, high_score_rect)


# function that draws a grid layout
def draw_grid():
    for i in range(SCREEN_WIDTH // GRID_SIZE):
        for j in range(SCREEN_HEIGHT // GRID_SIZE):
            # the grid consists os squares
            square = pg.Rect((i * GRID_SIZE, j * GRID_SIZE), (GRID_SIZE, GRID_SIZE))

            # the black line
            if i == SCREEN_WIDTH // GRID_SIZE - 3:
                pg.draw.rect(surface, (0, 0, 0), square)

            # the edges in width are filled with dark green color
            elif i == 0 or i == SCREEN_WIDTH // GRID_SIZE - 4 or i >= SCREEN_WIDTH // GRID_SIZE - 2:
                if i >= SCREEN_WIDTH // GRID_SIZE - 2:
                    # red where current score displays
                    if j == 3 or j == 4:
                        pg.draw.rect(surface, (244, 55, 6), square)
                    else:
                        pg.draw.rect(surface, (74, 117, 44), square)
                else:
                    pg.draw.rect(surface, (74, 117, 44), square)

            # the edges in width are filled with dark green color
            elif j == 0 or j >= SCREEN_HEIGHT // GRID_SIZE - 1:
                pg.draw.rect(surface, (74, 117, 44), square)
            else:
                # the field is like a chess board (green and light green)
                if (i + j) % 2 == 0:
                    pg.draw.rect(surface, (167, 217, 72), square)
                else:
                    pg.draw.rect(surface, (132, 189, 53), square)


# initializing the game
pg.init()
clock = pg.time.Clock()

# screen and grid params
GRID_SIZE = 30
SCREEN_HEIGHT = 540
SCREEN_WIDTH = 630
# How many cells of the screen are for the snake and apples
GRID_WIDTH = (SCREEN_WIDTH - 5 * GRID_SIZE) // GRID_SIZE
GRID_HEIGHT = (SCREEN_HEIGHT - 2 * GRID_SIZE) // GRID_SIZE

# font
pg.font.init()
score_font = pg.font.SysFont('Comic Sans MS', 26)

# moving each (repeat time) milliseconds
repeat_time = 150
SCREEN_UPDATE = pg.USEREVENT
pg.time.set_timer(SCREEN_UPDATE, repeat_time)

# screen
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# making the surface
surface = pg.Surface(screen.get_size()).convert()

# initializing main Game object
game = Game()

# game loop
while True:
    # event handling
    game.event_handler()

    # drawing surface, apple and a snake
    game.draw_objects()
    # screen update
    screen.blit(surface, (0, 0))

    # draw score
    draw_score()

    # display update
    pg.display.update()
    clock.tick(10)


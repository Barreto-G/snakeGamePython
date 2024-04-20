import pygame
import random


class SnakeGame:
    colors = {
        'black': (0, 0, 0),
        'white': (255, 255, 255),
        'red': (255, 0, 0),
        'green': (0, 255, 0)
    }

    def __init__(self, width: int = 1200, height: int = 800):
        pygame.init()
        pygame.display.set_caption('Snake Game by Barreto')
        self.__screenWidth = width
        self.__screenHeight = height
        self.__screen = pygame.display.set_mode((width, height))
        self.__clock = pygame.time.Clock()
        self.__blockSize = (width/height)*15.0
        self.__gameSpeed = 15
        self.__score = 0

    # Generates a random position inside the screen for the food that will be put
    def random_position(self):
        x_position = round(random.randrange(0, self.__screenWidth - int(self.__blockSize))/self.__blockSize)*self.__blockSize
        y_position = round(random.randrange(0, self.__screenHeight - int(self.__blockSize))/self.__blockSize)*self.__blockSize
        return x_position, y_position

    # Draw a rectangle with the position and color given
    def draw(self, x_position, y_position, color):
        rect = [x_position, y_position, self.__blockSize, self.__blockSize]
        pygame.draw.rect(self.__screen, color, rect)

    # Draws the snake body
    def draw_snake(self, snake_pixels):
        for pixel in snake_pixels:
            self.draw(pixel[0], pixel[1], self.colors['green'])
        pass

    # Shows the player score on the screen
    def draw_score(self):
        font = pygame.font.SysFont('Helvetica', 25)
        text = font.render(f"Score: {self.__score}", False, self.colors['white'])
        self.__screen.blit(text, [1,1])

    # Handles the movement of the snake using the key pressed by the player
    def movement(self, key, former_x_speed, former_y_speed):
        x_speed = 0
        y_speed = 0

        if key == pygame.K_DOWN and former_y_speed == 0:
            y_speed = self.__blockSize
        elif key == pygame.K_UP and former_y_speed ==0:
            y_speed = -self.__blockSize
        elif key == pygame.K_LEFT and former_x_speed == 0:
            x_speed = -self.__blockSize
        elif key == pygame.K_RIGHT and former_x_speed == 0:
            x_speed = self.__blockSize
        else:
            x_speed = former_x_speed
            y_speed = former_y_speed

        return x_speed, y_speed

    def check_borders(self, x_snake, y_snake):
        if x_snake < 0:
            x_snake = self.__screenWidth
        elif x_snake > self.__screenWidth:
            x_snake = 0

        if y_snake < 0:
            y_snake = self.__screenHeight
        elif y_snake > self.__screenHeight:
            y_snake = 0

        return x_snake, y_snake

    def play(self):
        game_ended = False

        # Snake always starts in the middle of the screen
        x_snake = self.__screenWidth/2
        y_snake = self.__screenHeight/2

        # The position of each pixel of the snake`s body is stored in pixels
        # and it`s full size in snake_size
        snake_size = 1
        pixels = []

        # Indicates wich direction the snake is moving
        x_speed = 0
        y_speed = 0

        # Generate the first food element
        x_food, y_food = self.random_position()

        while not game_ended:
            self.__screen.fill(SnakeGame.colors['black'])
            self.draw(x_food, y_food, self.colors['red'])   # Draw the current food

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_ended = True
                elif event.type == pygame.KEYDOWN:
                    x_speed, y_speed = self.movement(event.key, x_speed, y_speed)

            # Stores the current position of the snake`s head
            pixels.append([x_snake, y_snake])

            # The position of the snake is changed by it`s movement speed
            x_snake += x_speed
            y_snake += y_speed

            # The movement of the snake is simply remove its last pixel
            if len(pixels) > snake_size:
                del pixels[0]

            x_snake, y_snake = self.check_borders(x_snake, y_snake)

            # Verifies if the snake hit its own body
            for pixel in pixels[:-1]:
                if pixel == [x_snake, y_snake]:
                    game_ended = True

            self.draw_snake(pixels)
            self.__score = snake_size-1
            self.draw_score()

            pygame.display.update()

            if x_snake == x_food and y_snake == y_food:
                snake_size += 1
                x_food, y_food = self.random_position()

            self.__clock.tick(self.__gameSpeed)
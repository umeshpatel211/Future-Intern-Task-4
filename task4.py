'''To develop a snake game:
Create a program where the player controls a snake that moves around the screen. Initially,
the snake starts with a single segment and grows in length each time it eats food randomly 
placed on the screen. The player uses arrow keys to navigate the snake. The game ends if the 
snake collides with itself or the boundaries of the screen.'''

import pygame
import time
import random

# Initialize pygame
pygame.init()

# Set display dimensions
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))

# Set colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)

# Set clock speed
clock = pygame.time.Clock()
snake_speed = 15

# Set snake properties
snake_block = 10

# Define font for displaying score
font_style = pygame.font.SysFont("bahnschrift", 25)

# Function to display score
def display_score(score):
    value = font_style.render(f"Your Score: {score}", True, green)
    screen.blit(value, [0, 0])

# Function to draw the snake on the screen
def draw_snake(snake_block, snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, green, [block[0], block[1], snake_block, snake_block])

# Function for the main game loop
def game_loop():
    game_over = False
    game_close = False

    # Starting position of the snake
    x = screen_width / 2
    y = screen_height / 2
    x_change = 0
    y_change = 0

    # Snake body list and initial length
    snake_list = []
    length_of_snake = 1

    # Position of the first food
    food_x = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close:
            screen.fill(black)
            message = font_style.render("Game Over! Press C to play again or Q to quit.", True, red)
            screen.blit(message, [screen_width / 6, screen_height / 3])
            display_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_block
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_block
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -snake_block
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = snake_block
                    x_change = 0

        # If the snake hits the screen boundary, the game ends
        if x >= screen_width or x < 0 or y >= screen_height or y < 0:
            game_close = True

        # Update the position of the snake
        x += x_change
        y += y_change
        screen.fill(black)

        # Draw the food
        pygame.draw.rect(screen, white, [food_x, food_y, snake_block, snake_block])

        # Update the snake's position
        snake_head = [x, y]
        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # If the snake collides with itself, the game ends
        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        # Draw the snake
        draw_snake(snake_block, snake_list)

        # Display the score
        display_score(length_of_snake - 1)

        pygame.display.update()

        # If the snake eats the food, generate a new food item and grow the snake
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        # Set the game speed
        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Start the game
game_loop()

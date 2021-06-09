import pygame
import random
import math
from pygame.constants import KEYDOWN, K_ESCAPE, K_RETURN

pygame.init()

# Game console
screen = pygame.display.set_mode((900, 600))

# Title
pygame.display.set_caption("Snakes")

# Icon
Icon = pygame.image.load('C:\\Users\\Admin\\Desktop\\dragonx\\Projects\\Snakes\\snake.png')
pygame.display.set_icon(Icon)


# Snake
class Snake:
    snakeX = 45
    snakeY = 55
    velocityX = 0
    velocityY = 0
    snakeSize = 10
    snakeList = []
    snakeLength = 1

# Food
class Food:
    foodX = random.randint(0, 830)
    foodY = random.randint(0, 540)
    foodSize = 12

# Game specific variables
running = True
game_over = False
clock = pygame.time.Clock()
FPS = 60
score = 0
font = pygame.font.Font('freesansbold.ttf', 15)
over_font = pygame.font.Font('freesansbold.ttf', 30)
welcomefont = pygame.font.Font('freesansbold.ttf', 25)

with open("Highscore.txt", "r") as Hs:
    highscore = Hs.read()

def textScreen(font, text, colour, x, y):
    screen_text = font.render(text, True, colour)
    screen.blit(screen_text, (x, y))

# def welcome():
#     running_welcome = True
#     while not running_welcome:
#         screen.fill((255, 255, 255))
#         textScreen(welcomefont, "Welcome to Snakes", (0, 0, 0), 360, 290)
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running_welcome = False

#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_RETURN:
#                     running = True
#                     return

#                 elif event.key == pygame.K_ESCAPE:
#                     running_welcome = False

#         pygame.display.update()
#         clock.tick(FPS)

# Snake Plotting
def plot_snake(gameWindow, colour, snakeList, snakeSize):
    for x,y in snakeList:
        pygame.draw.rect(screen, colour, [x, y, snakeSize, snakeSize])

# Plot Food
def plot_food(gameWindow, colour, foodX, foodY, foodSize):
    pygame.draw.circle(screen, colour, (foodX, foodY), foodSize, width=0)

# Checks for food eaten by snake
def isEaten(X1, Y1, X2, Y2, min_dist):
    Distance = math.sqrt(math.pow((X1 - X2), 2) + math.pow((Y1 - Y2), 2))

    if Distance < min_dist:
        return True

    else:
        return False

# Prints score on window
def show_score(score, font):
    textScreen(font, "Score :" + str(score), (0, 0, 0), 15, 15)
    textScreen(font, "High Score :" + str(highscore), (0, 0, 0), 15, 30)

def Game_Over(over_font):
    textScreen(over_font, "Game Over", (0, 0, 0), 360, 290)

# Greetings
# welcome()

# Game Loop
while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                Snake.velocityX = 5
                Snake.velocityY = 0

            if event.key == pygame.K_LEFT:
                Snake.velocityX = -5
                Snake.velocityY = 0

            if event.key == pygame.K_DOWN:
                Snake.velocityY = 5
                Snake.velocityX = 0

            if event.key == pygame.K_UP:              
                Snake.velocityY = -5
                Snake.velocityX = 0

            # Cheat Code
            if event.key == pygame.K_q:
                score += 100
                Snake.snakeLength += 10

    Snake.snakeX += Snake.velocityX
    Snake.snakeY += Snake.velocityY

    if isEaten(Snake.snakeX, Snake.snakeY, Food.foodX, Food.foodY, 10):
        score += 10
        Food.foodX = random.randint(0, 850)
        Food.foodY = random.randint(0, 550)
        Snake.snakeLength += 5
        if score > int(highscore):
            highscore = score
            with open ("Highscore.txt", "w") as Hs:
                Hs.write(str(highscore))

    # Check if the snake has hit the walls
    if Snake.snakeX <= 0 or Snake.snakeY <=0:
        game_over = True
        Snake.velocityX = 0
        Snake.velocityY = 0

    elif Snake.snakeX == 890 or Snake.snakeY == 590:
        game_over = True
        Snake.velocityX = 0
        Snake.velocityY = 0

    Head = []
    Head.append(Snake.snakeX)
    Head.append(Snake.snakeY)
    Snake.snakeList.append(Head)
    
    if len(Snake.snakeList) > Snake.snakeLength:
        del Snake.snakeList[0]

    if Head in Snake.snakeList[1:-1]:
        game_over = True

    plot_snake(screen, (0, 0, 0), Snake.snakeList, Snake.snakeSize)
    plot_food(screen, (255, 0, 0), Food.foodX, Food.foodY, Food.foodSize)
    clock.tick(FPS)

    show_score(score, font)
    if game_over:
        screen.fill((255, 255, 255))
        Game_Over(over_font)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

    pygame.display.update()

pygame.quit()
quit()
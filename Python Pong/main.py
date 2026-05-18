import pygame
import sys
from paddle import Paddle
from ball import Ball

pygame.init
screen_size = (1000, 600)
screen = pygame.display.set_mode(screen_size)
display = pygame.Surface(screen_size)
pygame.display.set_caption("Pong Project")

ball_width = 30
ball_height = 30

balls = []

player1 = Paddle(7, 10, 300, 10, 100, (0, 170, 200), 10, screen_size[1]-110, pygame.K_w, pygame.K_s)
player2 = Paddle(7, 980, 300, 10, 100, (255, 190, 200), 10, screen_size[1]-110, pygame.K_UP, pygame.K_DOWN)
balls.append(Ball(5, 500, 300, ball_width, ball_height, (255, 255, 100), 0, screen_size[0], ball_height/2, screen_size[1]-(ball_height/2), player1, player2))
print('initial theta =', balls[0].theta)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for ball in balls:
        ball.find_axis_val()

    screen.fill((50, 50, 50))

    player1.move()
    player2.move()
    for ball in balls:
        ball.move()

    player1.draw(screen)
    player2.draw(screen)
    for ball in balls:
        ball.draw(screen)

    for ball in balls:
        if ball.check_goal():
            balls.remove(ball)
            balls.append(Ball(5, 500, 300, ball_width, ball_height, (255, 255, 100), 0, screen_size[0], ball_height/2, screen_size[1]-(ball_height/2), player1, player2))
            balls.append(Ball(5, 500, 300, ball_width, ball_height, (255, 255, 100), 0, screen_size[0], ball_height/2, screen_size[1]-(ball_height/2), player1, player2))

    if player1.points >= 50:
        print('PLAYER 1 WINS')
        running = False
    if player2.points >= 50:
        print('PLAYER 2 WINS')
        running = False

    print('----------------------------')
    pygame.time.Clock().tick(60)
    pygame.display.update()

pygame.quit()
sys.exit
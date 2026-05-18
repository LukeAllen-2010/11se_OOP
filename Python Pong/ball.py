import random
from math import *
from entity import Entity
import pygame

class Ball(Entity):
    def __init__(self, start_speed, x, y, width, height, colour, left_bound, right_bound, top_bound, bottom_bound, paddle_left, paddle_right):
        super().__init__(start_speed, x, y, width, height, colour)
        self.y_bound = (top_bound, bottom_bound)
        self.x_bound = (left_bound, right_bound)
        self.theta = random.randint(1, 360) 
        self.paddle_left = paddle_left
        self.paddle_right = paddle_right
        self.lock_to_side_left = paddle_left.rect.right
        self.true_center = [x, y]
        print('init_theta =', self.theta)


    def find_axis_val(self):
        # if self.a != self.theta: # Debug, print when change in theta
        #     print(self.theta)
        #     self.a = self.theta

        h = self.speed
        self.movement[0] = h * cos(radians(self.theta))
        self.movement[1] = h * sin(radians(self.theta))

        print('MOVEMENT =', self.movement)
        # print('theta =', self.theta)

        if round(self.movement[0]) <= 1 or round(self.movement[1]) <= 1:
            self.find_axis_val

    
    def find_rect_side(self, paddle_left, paddle_right):
        if self.rect.colliderect(paddle_left):
            return paddle_left.rect
        if self.rect.colliderect(paddle_right):
            return paddle_right.rect

    def paddle_collision(self, paddle_left, paddle_right, lock_to_side):
        if self.rect.colliderect(paddle_left.rect):
            print(f"collision with {paddle_left}")
            self.rect.left = paddle_left.rect.right
            self.theta = 180 - self.theta
            self.theta += random.randint(-10,10)

            # print('theta:', self.theta)
            self.speed += 1

            self.true_center = [self.rect.center[0], self.rect.center[1]]
            self.movement[0] = 0
            self.movement[1] = 0
            # print('CENTER_INT_X =', self.rect.centerx)
            # print('CENTER_TRUE_X =', self.true_center[0])

        elif self.rect.colliderect(paddle_right.rect):
            print(f"collision with {paddle_left}")

            self.rect.right = paddle_right.rect.left
            self.theta = 180 - self.theta
            self.theta += random.randint(-10,10)
            # print('theta:', self.theta)

            self.true_center = [self.rect.center[0], self.rect.center[1]]
            # print('CENTER_INT_X =', self.rect.centerx)
            # print('CENTER_TRUE_X =', self.true_center[0])

            self.movement[0] = 0
            self.movement[1] = 0
        print(f"{paddle_left.points} vs {paddle_right.points}")

    def collision_check_y(self):
        if self.y_bound[0] > self.rect.centery + self.movement[1]:
            self.rect.top = self.y_bound[0]
            self.movement[1] *= -1
            self.theta *= -1
        elif self.y_bound[1] < self.rect.centery + self.movement[1]:
            self.rect.bottom = self.y_bound[1]
            self.movement[1] *= -1 # If it isn't, swap movement around
            self.theta *= -1    


    def move(self):
        self.paddle_collision(self.paddle_left, self.paddle_right, self.paddle_left.rect.right)
        # self.paddle_collision(self.paddle_right, self.rect.right, self.paddle_right.rect.left)
        self.collision_check_y()

        self.true_center[0] += self.movement[0]
        self.true_center[1] += self.movement[1]
        self.rect.center = (self.true_center[0], self.true_center[1])
        print('rect center =',self.rect.center)
        
    def check_goal(self):
        if self.rect.x < self.x_bound[0] - self.rect.width:
            self.paddle_right.points += 1
            return True
        elif self.rect.x > self.x_bound[1] + self.rect.width:
            self.paddle_right.points += 1
            return True
        return False


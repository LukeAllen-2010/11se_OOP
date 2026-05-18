import pygame
from entity import Entity

class Paddle(Entity):
    def __init__(self, speed, x, y, width, height, colour, top_bound, bottom_bound, up_key, down_key):
        super().__init__(speed, x, y, width, height, colour)
        self.y_bound = (top_bound, bottom_bound)
        self.points = 0
        self.down_key = down_key
        self.up_key = up_key

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[self.down_key]:
            self.movement[1] += self.speed
        if keys[self.up_key]:
            self.movement[1] -= self.speed
        
        if self.y_bound[0] < self.rect.y + self.movement[1] < self.y_bound[1]:
            self.rect.y += self.movement[1]
        self.movement = [0, 0]
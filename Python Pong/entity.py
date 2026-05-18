import pygame

class Entity:
    def __init__(self, speed, x, y, width, height, colour):
        self.speed = speed
        self.rect = pygame.Rect(x, y, width, height)
        self.rect_colour = colour
        self.movement = [0, 0]

    def draw(self, screen):
        pygame.draw.rect(screen, self.rect_colour, self.rect)
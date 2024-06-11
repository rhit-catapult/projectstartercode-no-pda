import pygame
import sys


cube_size = 40

class Wall:
    def __init__(self, screen, x, y, width, height):
        self.screen = screen
        self.color = (0, 0, 0)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def draw(self):
        self.rect = pygame.draw.rect(self.screen, self.color, (self.x,self.y, self.width, self.height))

    def collide_with(self, player):
        self.rect.colliderect(player)

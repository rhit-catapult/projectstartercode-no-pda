import pygame
import sys

class Ending:
    def __init__(self, screen):
        self.screen = screen

    def main_loop(self):
        self.screen.fill((0, 0, 0))
        font2 = pygame.font.SysFont("geneva", 100)
        caption2 = font2.render("Congrass", True, pygame.Color("Red"))
        self.screen.blit(caption2, (300, 300))
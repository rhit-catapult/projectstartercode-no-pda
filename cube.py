import pygame
import sys
import time
import random




class Cube:
    def __init__(self, screen, x, y):
        self.x = x
        self.y = y
        self.screen = screen
        self.side = 20
        self.color = (0,0,0)

    def move(self):
        pass






    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.side,self.side))





def main():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("World's Hardest Game")
    screen = pygame.display.set_mode((640, 650))

    c = Cube(screen, 50,50)

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill((255, 255, 255))
        #c.move
        c.draw()




        pygame.display.update()


main()

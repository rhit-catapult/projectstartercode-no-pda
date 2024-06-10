import pygame
import sys
import random
import time

class Player:
    def __init__(self, screen, x, y):
        self.x = x
        self.y = y
        self.screen = screen

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        # if self.x > self.screen.get_width - 25:
        #     self.x = self.screen.get_width - 25
        # if self.x < 25:
        #     self.x = 25
        # if self.y > self.screen.get_height - 25:
        #     self.y = self.screen.get_height - 25
        # if self.y < 25:
        #     self.y = 25

        pass
    def draw(self):
        pygame.draw.rect(self.screen, (0, 0, 0), (self.x, self.y, 25, 25))
        pass

def main():
    # turn on pygame
    pygame.init()

    # create a screen
    pygame.display.set_caption("Cool Project")

    # TODO: Change the size of the screen as you see fit!
    screen = pygame.display.set_mode((1000, 700))

    p1 = Player(screen, 50, 50)

    # let's set the framerate
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_a] or pressed_keys[pygame.K_LEFT]:
            p1.move(-5, 0)
        if pressed_keys[pygame.K_d] or pressed_keys[pygame.K_RIGHT]:
            p1.move(5, 0)
        if pressed_keys[pygame.K_w] or pressed_keys[pygame.K_UP]:
            p1.move(0, -5)
        if pressed_keys[pygame.K_s] or pressed_keys[pygame.K_DOWN]:
            p1.move(0, 5)

            # TODO: Add you events code

        # TODO: Fill the screen with whatever background color you like!
        screen.fill((255, 255, 255))

        p1.draw()

        # TODO: Add your project code

        # don't forget the update, otherwise nothing will show up!
        pygame.display.update()

main()

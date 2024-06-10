import pygame
import sys
import random
import time
import math

class Player:
    def __init__(self, screen, x, y):
        self.x = x
        self.y = y
        self.screen = screen
        self.size = 40

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        if self.x > self.screen.get_width() - self.size:
            self.x = self.screen.get_width() - self.size
        if self.x < 0:
            self.x = 0
        if self.y > self.screen.get_height() - self.size:
            self.y = self.screen.get_height() - self.size
        if self.y < 0:
            self.y = 0

        pass
    def draw(self):
        pygame.draw.rect(self.screen, (0, 0, 0), (self.x, self.y, 25, 25))
        pass

def main():
    # turn on pygame
    pygame.init()

    # create a screen
    pygame.display.set_caption("No PDA!")
    # TODO: Change the size of the screen as you see fit!
    screen = pygame.display.set_mode((1000, 700))

    delta = 10
    gs = 50
    # let's set the frame rate
    p1 = Player(screen, 55, 55)

    # let's set the framerate
    clock = pygame.time.Clock()
    while True:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_a] or pressed_keys[pygame.K_LEFT]:
            p1.move(-delta, 0)
        if pressed_keys[pygame.K_d] or pressed_keys[pygame.K_RIGHT]:
            p1.move(delta, 0)
        if pressed_keys[pygame.K_w] or pressed_keys[pygame.K_UP]:
            p1.move(0, -delta)
        if pressed_keys[pygame.K_s] or pressed_keys[pygame.K_DOWN]:
            p1.move(0, delta)

            # TODO: Add you events code

        # TODO: Fill the screen with whatever background color you like!
        screen.fill((255, 255, 255))
        pygame.draw.rect(screen, (98, 226, 108), (0, 0, 150, 150))
        pygame.draw.rect(screen, (98, 226, 108), (screen.get_width()-150, screen.get_height()-150, 150, 150))
        pygame.draw.rect(screen, (0, 0, 0), (150,0, 50, 550))
        pygame.draw.rect(screen, (0, 0, 0), (screen.get_width()-200, screen.get_height()-550, 50, 550))
        pygame.draw.circle(screen, (0, 0, 255), (275, 16), 15)
        pygame.draw.circle(screen, (0, 0, 255), (375, 16), 15)
        pygame.draw.circle(screen, (0, 0, 255), (475, 16), 15)
        pygame.draw.circle(screen, (0, 0, 255), (575, 16), 15)
        pygame.draw.circle(screen, (0, 0, 255), (675, 16), 15)
        pygame.draw.circle(screen, (0, 0, 255), (775, 16), 15)

        pygame.draw.circle(screen, (0, 0, 255), (225, screen.get_height() - 15), 15)
        pygame.draw.circle(screen, (0, 0, 255), (325, screen.get_height() - 15), 15)
        pygame.draw.circle(screen, (0, 0, 255), (425, screen.get_height() - 15), 15)
        pygame.draw.circle(screen, (0, 0, 255), (525, screen.get_height() - 15), 15)
        pygame.draw.circle(screen, (0, 0, 255), (625, screen.get_height() - 15), 15)
        pygame.draw.circle(screen, (0, 0, 255), (725, screen.get_height() - 15), 15)

        p1.draw()

        # TODO: Add your project code

        # don't forget the update, otherwise nothing will show up!
        pygame.display.update()

main()

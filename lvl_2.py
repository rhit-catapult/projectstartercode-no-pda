import pygame
import sys
import wall_class
import math
import wall_class

import enemy
class Player:
    def __init__(self, screen, x, y):
        self.x = x
        self.y = y
        self.screen = screen
        self.size = 40
        self.rect = None
        self.orig_x = x
        self.orig_y = y
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

    def draw(self):
        pygame.draw.rect(self.screen, (255, 255, 0), (self.x, self.y, self.size, self.size))
        self.rect = pygame.draw.rect(self.screen, (152, 144, 2), (self.x, self.y, self.size, self.size), 4)
    def collision(self):
        self.x = self.orig_x
        self.y = self.orig_y


def main():
    # turn on pygame
    pygame.init()

    # create a screen
    pygame.display.set_caption("No PDA!")
    # Done: Change the size of the screen as you see fit!
    screen = pygame.display.set_mode((1000, 700))

    p1 = Player(screen, 55, 55)

    # let's set the framerate
    clock = pygame.time.Clock()
    walls = []
    walls.append(pygame.draw.rect(screen, (30, 180, 80), (150, 0, 850, 50)))
    walls.append(pygame.draw.rect(screen, (30, 180, 80), (0, 650, 850, 50)))
    walls.append(pygame.draw.rect(screen, (30, 180, 80), (850, 0, 150, 550)))
    walls.append(pygame.draw.rect(screen, (30, 180, 80), (0, 150, 150, 550)))
    walls.append(pygame.draw.rect(screen, (30, 180, 80), (150, 150, 150, 150)))
    walls.append(pygame.draw.rect(screen, (30, 180, 80), (150, 400, 150, 150)))
    walls.append(pygame.draw.rect(screen, (30, 180, 80), (700, 150, 150, 150)))
    walls.append(pygame.draw.rect(screen, (30, 180, 80), (700, 400, 150, 150)))
    walls.append(pygame.draw.rect(screen, (30, 180, 80), (400, 300, 200, 100)))

    while True:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pressed_keys = pygame.key.get_pressed()
        dx = 0
        dy = 0
        if pressed_keys[pygame.K_a] or pressed_keys[pygame.K_LEFT]:
            dx = - 5

        if pressed_keys[pygame.K_d] or pressed_keys[pygame.K_RIGHT]:
            dx = 5

        if pressed_keys[pygame.K_w] or pressed_keys[pygame.K_UP]:

            dy = - 5
        if pressed_keys[pygame.K_s] or pressed_keys[pygame.K_DOWN]:
            dy = 5
        new_x = p1.x + dx
        new_y = p1.y + dy
        hit_any = False
        for wall in walls:
            if wall.colliderect(new_x, new_y, p1.size, p1.size):
                hit_any = True
        if not hit_any:
            p1.move(dx, dy)

            # TODO: Add you events code

        # TODO: Fill the screen with whatever background color you like!
        screen.fill((255, 255, 255))
        pygame.draw.rect(screen, (98, 226, 108), (0, 0, 150, 150))
        pygame.draw.rect(screen, (98, 226, 108), (screen.get_width()-150, screen.get_height()-150, 150, 150))
        pygame.draw.rect(screen, (30, 180, 80), (150, 0, 850, 50))
        pygame.draw.rect(screen, (30, 180, 80), (0, 650, 850, 50))
        pygame.draw.rect(screen, (30, 180, 80), (850, 0, 150, 550))
        pygame.draw.rect(screen, (30, 180, 80), (0, 150, 150, 550))
        pygame.draw.rect(screen, (30, 180, 80), (150, 150, 150, 150))
        pygame.draw.rect(screen, (30, 180, 80), (150, 400, 150, 150))
        pygame.draw.rect(screen, (30, 180, 80), (700, 150, 150, 150))
        pygame.draw.rect(screen, (30, 180, 80), (700, 400, 150, 150))
        pygame.draw.rect(screen, (30, 180, 80), (400, 300, 200, 100))

        p1.draw()

        # for wall in walls:
        #     if wall.colliderect(p1.x, p1.y, p1.size, p1.size):
        #         print("Collision!")


        pygame.display.update()

main()


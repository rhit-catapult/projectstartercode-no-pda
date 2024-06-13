import pygame
import sys
import enemy_2
import math
import wall_class
import new_enemy

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

class Level3:
    def __init__(self, screen):
        self.screen = screen
        self.walls = []
        self.has_won = False
        # create all walls
        self.p1 = Player(screen, 55, 55)
        self.has_died = False
        self.has_touched_grass = False
        self.walls.append(pygame.draw.rect(screen, (30, 180, 80), (150, 0, 50, 600)))
        self.walls.append(pygame.draw.rect(screen, (30, 180, 80), (300, 150, 50, 550)))
        self.walls.append(pygame.draw.rect(screen, (30, 180, 80), (450, 0, 50, 550)))
        self.walls.append(pygame.draw.rect(screen, (30, 180, 80), (600, 100, 50, 600)))
        self.walls.append(pygame.draw.rect(screen, (30, 180, 80), (650, 150, 250, 50)))
        self.walls.append(pygame.draw.rect(screen, (30, 180, 80), (650, 400, 250, 50)))
        self.walls.append(pygame.draw.rect(screen, (30, 180, 80), (750, 300, 250, 50)))
        self.walls.append(pygame.draw.rect(screen, (30, 180, 80), (750, 500, 250, 50)))
        self.walls.append(pygame.draw.rect(screen, (30, 180, 80), (750, 500, 50, 150)))
        # sped = 8
        self.balls = []
        # b = new_enemy.New_Ball(screen, 165, 75, sped, 0, 15, (0, 0, 255),835,165)
        # self.balls.append(b)






    def main_loop(self):
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
        new_x = self.p1.x + dx
        new_y = self.p1.y + dy
        hit_any = False
        for wall in self.walls:
            if wall.colliderect(new_x, new_y, self.p1.size, self.p1.size):
                hit_any = True
                self.p1.collision()
                self.has_touched_grass = True
        if not hit_any:
            self.p1.move(dx, dy)

            # TODO: Add you events code

        # TODO: Fill the screen with whatever background color you like!
        self.screen.fill((255, 255, 255))
        pygame.draw.rect(self.screen, (98, 226, 108), (0, 0, 150, 150))
        pygame.draw.rect(self.screen, (98, 226, 108), (self.screen.get_width() - 150, self.screen.get_height() - 150, 150, 150))
        pygame.draw.rect(self.screen, (30, 180, 80), (150, 0, 50, 600))
        pygame.draw.rect(self.screen, (30, 180, 80), (300, 150, 50, 550))
        pygame.draw.rect(self.screen, (30, 180, 80), (450, 0, 50, 550))
        pygame.draw.rect(self.screen, (30, 180, 80), (600, 100, 50, 600))
        pygame.draw.rect(self.screen, (30, 180, 80), (650, 150, 250, 50))
        pygame.draw.rect(self.screen, (30, 180, 80), (650, 400, 250, 50))
        pygame.draw.rect(self.screen, (30, 180, 80), (750, 300, 250, 50))
        pygame.draw.rect(self.screen, (30, 180, 80), (750, 500, 250, 50))
        pygame.draw.rect(self.screen, (30, 180, 80), (750, 500, 50, 150))

        for ball in self.balls:
            ball.move()
            ball.draw()
            if ball.shape.colliderect(self.p1.x, self.p1.y, self.p1.size, self.p1.size):
                self.p1.collision()
                self.has_died = True

        # if 0 <= self.p1.x <= 1000 and 200 <= self.p1.y <= 700:
        if 850 <= self.p1.x <= 1000 and 530 <= self.p1.y <= 700:
            self.has_won = True

        self.p1.draw()

        # for wall in walls:
        #     if wall.colliderect(p1.x, p1.y, p1.size, p1.size):
        #         print("Collision!")




def main():
    # turn on pygame
    pygame.init()

    # create a screen
    pygame.display.set_caption("No PDA!")
    # Done: Change the size of the screen as you see fit!
    screen = pygame.display.set_mode((1000, 700))







main()


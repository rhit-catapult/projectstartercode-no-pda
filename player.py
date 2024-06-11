import pygame
import sys






class Player:
    def __init__(self, screen, x, y):
        self.x = x
        self.y = y
        self.screen = screen
        self.size = 40
        self.rect = None

        #gg
        self.orig_x = x
        self.orig_y = y
     #gg
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






        if 110 <= self.x <= 116 and 0 <= self.y <= 551:
            self.x = 110
        if 111 <= self.x <= 200 and 540 <= self.y <=550:
            self.y = 550
        if 200 >= self.x >= 190 and 0 <= self.y <= 550:
            self.x = 200
        if 800 <= self.x <= 850 and 150 <= self.y <= 700:
            self.x = 850
        if 760 <= self.x <= 850 and 110 <= self.y <= 150:
            self.y = 110
        if 760 <= self.x <= 800 and 150 <= self.y <= 700:
            self.x = 760


    def draw(self):
        pygame.draw.rect(self.screen, (255, 255, 0), (self.x, self.y, self.size, self.size))
        self.rect = pygame.draw.rect(self.screen, (152, 144, 2), (self.x, self.y, self.size, self.size), 4)
    def collision(self):
        self.x = self.orig_x
        self.y = self.orig_y

    def main():
        pygame.init()
        screen = pygame.display.set_mode((500, 500))
        pygame.display.set_caption('Bouncing Ball')
        screen.fill(pygame.Color('gray'))
        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            clock.tick(60)
            screen.fill(pygame.Color('gray'))

            pygame.display.update()
        draw.Player()

    if __name__ == "__main__":
        main()
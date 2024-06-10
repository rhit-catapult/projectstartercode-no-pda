import pygame
import sys

balls = []

class Ball:
    def __init__(self, screen, x, y, x_speed, y_speed, ball_size, color):
        self.radius = ball_size
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.screen = screen
        self.ball_color = color
        self.x = x
        self.y = y
    def move(self):
        self.y = self.y + self.y_speed
        self.x = self.x + 0
        if self.x >= self.screen.get_width() or self.x <= 0:
            self.x_speed = -self.x_speed
        if self.y >= self.screen.get_height() or self.y <= 0:
            self.y_speed = -self.y_speed
# dTODO: Possible member variables: screen, color, x, y, radius, speed_x, speed_y
    def draw(self):
        pygame.draw.circle(self.screen, self.ball_color, (self.x, self.y), radius = self.radius)



def main():
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption('Bouncing Ball')
    screen.fill(pygame.Color('gray'))
    clock = pygame.time.Clock()



    balls = []
    for ball_number in range(1):
        ball_x_speed = 5
        ball_y_speed = 5
        ball_size = 5
        ball_color1 = (0)
        ball_color2 = (0)
        ball_color3 =(255)
        b = Ball(screen, 50,250, ball_x_speed, ball_y_speed, ball_size,(ball_color1, ball_color2, ball_color3))
        balls.append(b)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        clock.tick(60)
        screen.fill(pygame.Color('gray'))
        # dTODO: Move the ball

        # dTODO: Draw the ball
        for ball in balls:
            ball.move()
            ball.draw()
        pygame.display.update()


main()
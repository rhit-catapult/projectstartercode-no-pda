import pygame
import sys
import math
import wall_class
import lvl_1
import lvl_2
import enemy

def main():
    pygame.init()
    pygame.mixer_music.load("music.mp3")
    pygame.mixer_music.play(-1)
    # create a screen
    pygame.display.set_caption("No PDA!")
    # Done: Change the size of the screen as you see fit!
    screen = pygame.display.set_mode((1000, 700))


    # let's set the framerate
    clock = pygame.time.Clock()
    level = 1
    lvl1 = lvl_1.Level1(screen)
    lvl2 = None

    while True:
        clock.tick(45)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        if level == 1:
            lvl1.main_loop()
            if lvl1.has_won:
                level += 1
                lvl2 = lvl_2.Level2(screen)
        if level == 2:
            lvl2.main_loop()


        pygame.display.update()

main()
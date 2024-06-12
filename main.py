import pygame
import sys
import random
import wall_class
import lvl_1
import lvl_2
import enemy
import enemy_2

def main():
    pygame.init()
    pygame.mixer_music.load("music.mp3")
    pygame.mixer_music.play(-1)
    # create a screen
    pygame.display.set_caption("No PDA!")
    # Done: Change the size of the screen as you see fit!
    window = pygame.display.set_mode((1000, 700))
    screen = pygame.Surface(window.get_size())


    # let's set the framerate
    clock = pygame.time.Clock()
    level = 1
    lvl1 = lvl_1.Level1(screen)
    lvl2 = None
    jumpscare = False
    counselor_images = ["aaron.png", "anahita.png", "anthony.png", "brayden.png", "claire.png", "eathan.png", "eli.png", "elley.png", "emmet.png", "eric.png", "fox.png", "kali.png", "michael.png", "reid.png", "ruby.png", "tyler.png", "coon.png"]
    loaded_images = []
    for c in counselor_images:
        image = pygame.image.load("Counselor_Images/" + c)
        image = pygame.transform.scale(image, (1500, 1500))
        loaded_images.append(image)
    alpha = 255
    image_index = 0
    boom_sound = pygame.mixer.Sound("samples/vine-boom.mp3")

    while True:
        clock.tick(45)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        if level == 1:
            lvl1.main_loop()
            if lvl1.has_died:
                lvl1.has_died = False
                alpha = 255
                jumpscare = True
                image_index = random.randint(0, len(loaded_images)-1)
                boom_sound.play()

            if lvl1.has_won:
                level += 1
                lvl2 = lvl_2.Level2(screen)
        if level == 2:
            lvl2.main_loop()
            if lvl2.has_died:
                lvl2.has_died = False
                alpha = 255
                jumpscare = True
                image_index = random.randint(0, len(loaded_images)-1)
                boom_sound.play()

        window.blit(screen, (0, 0))
        if jumpscare:
            pos = (0, 0, screen.get_width(), screen.get_height())
            image_surf = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
            if image_index == 16:
                image_surf.blit(loaded_images[image_index], (-325, 100))
            else:
                image_surf.blit(loaded_images[image_index], (-230, -245))
            image_surf.set_alpha(alpha)
            window.blit(image_surf, pos)

            alpha -= 5
            if alpha <= 0:
                jumpscare = False




        pygame.display.update()

main()
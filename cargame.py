import pygame
pygame.init()
gray = (119, 118, 110)
display_h = 600
display_w = 800
gamedisplay = pygame.display.set_mode((display_w, display_h))
pygame.display.set_caption("car game")
clock = pygame.time.Clock()


def game_loop():
    bumped = False
    while not bumped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                bumped = True

        gamedisplay.fill(gray)
        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
quit()

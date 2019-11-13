import pygame
pygame.init()
gray = (119, 118, 110)
display_h = 600
display_w = 1050
gamedisplay = pygame.display.set_mode((display_w, display_h))
pygame.display.set_caption("car game")
clock = pygame.time.Clock()
car_img = pygame.image.load('car9.png')
backgroundpic = pygame.image.load('trees.png')


def backgroundTrees():
    gamedisplay.blit(backgroundpic, (0, 0))
    gamedisplay.blit(backgroundpic, (0, 100))
    gamedisplay.blit(backgroundpic, (0, 200))
    gamedisplay.blit(backgroundpic, (0, 300))
    gamedisplay.blit(backgroundpic, (0, 400))
    gamedisplay.blit(backgroundpic, (800, 0))
    gamedisplay.blit(backgroundpic, (800, 100))
    gamedisplay.blit(backgroundpic, (800, 200))
    gamedisplay.blit(backgroundpic, (800, 300))
    gamedisplay.blit(backgroundpic, (800, 400))


def car(x, y):
    gamedisplay.blit(car_img, (x, y))


def game_loop():
    x = (display_w*0.45)
    y = (display_h*0.8)
    x_change = 0

    bumped = False
    while not bumped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                bumped = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            if event.key == pygame.K_RIGHT:
                x_change = 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
        x += x_change
        gamedisplay.fill(gray)
        backgroundTrees()
        car(x, y)
        pygame.display.update()

        clock.tick(60)


game_loop()
pygame.quit()
quit()

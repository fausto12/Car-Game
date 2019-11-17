import pygame
import time

pygame.init()
gray = (119, 118, 110)
display_h = 600
display_w = 1050
gamedisplay = pygame.display.set_mode((display_w, display_h))
pygame.display.set_caption("car game")
clock = pygame.time.Clock()
# images to load
car_img = pygame.image.load('car9.png')
backgroundpic = pygame.image.load('trees.png')
yellow_strip = pygame.image.load('yellow_strip.png')
white_strip = pygame.image.load('white_strip.png')
# width of the car
car_width = 128


def text_objects(text, font):
    textsurface = font.render(text, True, (0, 98, 255))
    return textsurface, textsurface.get_rect()


def message_display(text):
    largetext = pygame.font.Font("freesansbold.ttf", 80)
    textsurf, textrect = text_objects(text, largetext)
    textrect.center = ((display_w/2), (display_h/2))
    gamedisplay.blit(textsurf, textrect)
    pygame.display.update()
    time.sleep(3)
    game_loop()


def crash():
    message_display("YOU CRASHED")


def background():
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
    gamedisplay.blit(yellow_strip, (510, 0))
    gamedisplay.blit(yellow_strip, (510, 150))
    gamedisplay.blit(yellow_strip, (510, 300))
    gamedisplay.blit(yellow_strip, (510, 450))
    gamedisplay.blit(white_strip, (250, 0))
    gamedisplay.blit(white_strip, (250, 300))
    gamedisplay.blit(white_strip, (800, 0))
    gamedisplay.blit(white_strip, (800, 300))


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
        background()
        car(x, y)

        # boundary set up
        if(x > 833 - car_width or x < 227):
            crash()
        pygame.display.update()

        clock.tick(60)


game_loop()
pygame.quit()
quit()

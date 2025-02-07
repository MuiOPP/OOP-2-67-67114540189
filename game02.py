import pygame
from pygame.locals import (
 K_UP, K_DOWN, K_LEFT, K_RIGHT, QUIT, KEYDOWN, K_a, K_d, K_w, K_s,
)

x,y = 100, 100
pygame.init()
size = (600, 400)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("game02")
clock = pygame.time.Clock()
sheet = pygame.image.load('spritesheet.png')
frame = 0
running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        keys = pygame.key.get_pressed()
        if e.type == KEYDOWN:
            if e.key in [K_a, K_LEFT]:   x-=2
            elif e.key in [K_d, K_RIGHT]:  x+=2
            elif e.key in [K_s, K_DOWN]:  y+=2
            elif e.key in [K_w, K_UP]:    y-=2

    magentar = (255, 0, 255)
    black = (0, 0, 0)
    rect = pygame.Rect(20, 50, 200, 300)
    screen.fill(black)
    screen.blit(sheet, (10, 10))

    clock.tick(30)

    pygame.display.flip()

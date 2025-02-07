from pygame.locals import *

pygame.init()
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("game02")
clock = pygame.time.Clock()
frame = 0
running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
            break
        elif e.type == pygame.KEYDOWN:
            if e.key in [K_LEFT,K_DOWN ]
    pygame.display.flip()

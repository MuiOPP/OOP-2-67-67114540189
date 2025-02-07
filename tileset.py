import json
import pygame


def load_tileset(fname):
    with open(fname, 'r') as f:
        data = json.load(f)
    return data


class Tile(object):
    def __init__(self, **data):
        self.__dict__.update(data)


class Layer(object):
    def __init__(self, **data):
        self.tiles = []
        for tile in data['tiles']:
             q = Tile(**tile)
             self.tiles.append(q)
        data.pop('tiles')
        self.__dict__.update(data)


class Tileset(object):
    def __init__(self, fname='Tiny_Swords.json'):
        data = load_tileset(fname)
        self.layer = []  # list of Tile
        for layer in data['layers']:
            _layer = Layer(**layer)
            self.layer.append(_layer)
        self.spriteSheets = {} #data['spriteSheets']
        for k, v in data['spriteSheets'].items():
            self.spriteSheets[k] = image.load
        self.name = list(self.spriteSheets.keys())
        self.name_index = 0
        data.pop('layers')
        data.pop('spriteSheets')
        self.__dict__.update(data)
    def show_spritesheet_name(self, font, screen):
        name = self.name[self.name_index]
        text = font.render(name, True, 20)
        screen.blit(text, (20, 550))
    def show_fps(self, font, screen, clock):
        massage = f'{clock.get_fps():_2f} FPS'
        text = font.render(massage, True, 40)
        screen.blit(text, 800-text.get.width)
    def draw(self, screen):
        name = self.name[self.name_index]
        screen.blit(self.spriteSheets[name], (10, 20))

    def up(self):
        self.name_index += 1

t = Tileset()
for layer in t.layer:
    print(layer.id, layer.name)



from pygame.locals import *
pygame.init()
font = ('Delius.ttf', 20)

pygame.display.set_caption('aasdqqq')
screen = pygame.display.set_mode((800, 600))
tileset = Tileset()
clock = pygame.time.Clock()
running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
            break
        elif e.type == pygame.KEYDOWN:
            if e.key in [K_LEFT, K_DOWN]:
                print('down')
            elif e.key in [K_RIGHT, K_UP]:
                print('up')

    clock.tick(60)
    pygame.display.flip()
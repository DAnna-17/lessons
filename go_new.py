import pygame
import os


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30

    def render(self, screen):
        t = {'*' : 'box.png', '#': 'grass.png'}
        all_sprites = pygame.sprite.Group()
        with open('data\карта.txt') as f:
            map = f.read().split('\n')
            for i in range(10):
                for k in range(10):
                    image = t[map[k][i]]
                    sprite = pygame.sprite.Sprite()
                    sprite.image = load_image(image)
                    sprite.rect = sprite.image.get_rect()
                    x, y = i * 50 + 50, k * 50 + 50
                    print(x, y)
                    sprite.rect.x, sprite.rect.y = x, y
                    all_sprites.add(sprite)
            print(all_sprites)
        all_sprites.draw(screen)

class Hero:
    def __init__(self, x, y):
        self.all_sprites = pygame.sprite.Group()
        sprite = pygame.sprite.Sprite()
        self.sprite = sprite
        sprite.image = load_image('mar.png')
        sprite.rect = sprite.image.get_rect()
        self.x, self.y = x, y
        sprite.rect.x, sprite.rect.y = self.x, self.y
        self.all_sprites.add(sprite)
        self.all_sprites.draw(screen)

    def go(self, x, y):
        self.sprite.rect.x, self.sprite.rect.y = x, y
        self.all_sprites.draw(screen)

    def render(self):
        self.all_sprites.draw(screen)


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image



pygame.init()
board = Board(7, 7)
screen = pygame.display.set_mode((700, 600))
board.render(screen)
pygame.display.flip()
x, y = 62, 57
h = Hero(x, y)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= 50
            elif event.key == pygame.K_RIGHT:
                x += 50
            elif event.key == pygame.K_DOWN:
                y += 50
            elif event.key == pygame.K_UP:
                y -= 50
            h.go(x, y)
    board.render(screen)
    h.render()
    pygame.display.flip()
    screen.fill((0, 0, 0))
import pygame
import os


class Board:
    # создание поля
    def __init__(self, map):
        self.map = "data\\" + map + '.txt'

    def render(self, screen):
        t = {'#': 'box.png', '*': 'grass.png'}
        all_sprites = pygame.sprite.Group()
        with open(self.map) as f:
            map = f.read().split('\n')
            for i in range(10):
                for k in range(10):
                    image = t[map[k][i]]
                    sprite = pygame.sprite.Sprite()
                    sprite.image = load_image(image)
                    sprite.rect = sprite.image.get_rect()
                    x, y = i * 50, k * 50
                    sprite.rect.x, sprite.rect.y = x, y
                    all_sprites.add(sprite)
        self.all_sprites = all_sprites
        all_sprites.draw(screen)

    def apply(self, x, y, screen):
        for sprite in self.all_sprites:
            print(sprite.rect.x, sprite.rect.y)
            sprite.rect.x -= x
            sprite.rect.y -= y
            print(sprite.rect.x, sprite.rect.y, '\n-----')
            if sprite.rect.x < 12 or sprite.rect.x > 312 or sprite.rect.y < 7 or sprite.rect.y > 307:
                sprite.rect.x= 1000
                sprite.rect.y = 1000
        self.all_sprites.draw(screen)


    def draw(self, screen):
        self.all_sprites.draw(screen)


class Camera:
    # зададим начальный сдвиг камеры
    def __init__(self):
        self.dx = 0
        self.dy = 0

    # сдвинуть объект obj на смещение камеры
    def apply(self, obj):
        obj.rect.x += 100#self.dx
        obj.rect.y += 100#self.dy

    # позиционировать камеру на объекте target
    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - 50 // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - 50 // 2)

class Hero:
    def __init__(self, x, y):
        self.all_sprites = pygame.sprite.Group()
        sprite = pygame.sprite.Sprite()
        self.sprite = sprite
        self.image = load_image('mar.png')
        sprite.image = self.image
        sprite.rect = sprite.image.get_rect()
        self.x, self.y = x, y
        sprite.rect.x, sprite.rect.y = self.x, self.y
        self.rect = self.image.get_rect()
        self.all_sprites.add(sprite)
        self.all_sprites.draw(screen)

    def render(self):
        self.all_sprites.draw(screen)

    def go(self, x, y):
        self.sprite.rect.x += x
        self.sprite.rect.y += y
        print(111111111111111111, self.sprite.rect.x, self.sprite.rect.y, x, y)
        self.all_sprites.draw(screen)


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


map = 'карта'#input('Введите название карты без указания типа файла\n')
pygame.init()
board = Board(map)
cam = Camera()
screen = pygame.display.set_mode((350, 350))
board.render(screen)
pygame.display.flip()
h = Hero(162, 157)
cam.update(h.sprite)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            x, y = 0, 0
            if event.key == pygame.K_LEFT:
                x -= 50
            elif event.key == pygame.K_RIGHT:
                x += 50
            elif event.key == pygame.K_DOWN:
                y += 50
            elif event.key == pygame.K_UP:
                y -= 50
            #h.go(x, y)
            cam.update(h)
            screen.fill((0, 0, 0))
            board.apply(x, y, screen)
            # board.render(screen)
            pygame.display.flip()
            print(11111111111111)
    # board.render(screen)
    h.render()
    pygame.display.flip()
    #screen.fill((0, 0, 0))
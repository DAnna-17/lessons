import os
import sys

import pygame


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image



pygame.init()
screen = pygame.display.set_mode((700, 600))
running = True

all_sprites = pygame.sprite.Group()
sprite = pygame.sprite.Sprite()
sprite.image = load_image("cursor.png")
sprite.rect = sprite.image.get_rect()
sprite.rect.x, sprite.rect.y = pygame.mouse.get_pos()
all_sprites.add(sprite)
x, y = 0, 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= 10
            elif event.key == pygame.K_RIGHT:
                x += 10
            elif event.key == pygame.K_DOWN:
                y += 10
            elif event.key == pygame.K_UP:
                y -= 10
    sprite.rect.x, sprite.rect.y = x, y
    all_sprites.draw(screen)
    pygame.display.flip()
    screen.fill((0, 0, 0))
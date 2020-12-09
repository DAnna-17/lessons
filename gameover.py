import os
import sys

import pygame


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image



pygame.init()
screen = pygame.display.set_mode((1280, 720))
running = True

all_sprites = pygame.sprite.Group()
sprite = pygame.sprite.Sprite()
sprite.image = load_image("gameover.jpg")
sprite.rect = sprite.image.get_rect()
x, y = -1280, 0
sprite.rect.x, sprite.rect.y = x, y
all_sprites.add(sprite)

MYEVENTTYPE = pygame.USEREVENT + 1
pygame.time.set_timer(MYEVENTTYPE, 60)

while running:
    for event in pygame.event.get():
        if event.type == MYEVENTTYPE and x < 200:
            x += 200
        if event.type == pygame.QUIT:
            running = False
    if x > 0:
        x = 0
    sprite.rect.x, sprite.rect.y = x, y
    all_sprites.draw(screen)
    pygame.display.flip()
    screen.fill((0, 0, 0))
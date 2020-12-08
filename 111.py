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
screen = pygame.display.set_mode((700, 600))
running = True

all_sprites = pygame.sprite.Group()
sprite = pygame.sprite.Sprite()
sprite.image = load_image("cursor.png")
sprite.rect = sprite.image.get_rect()
sprite.rect.x, sprite.rect.y = pygame.mouse.get_pos()
all_sprites.add(sprite)
pygame.mouse.set_visible(False)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    sprite.rect.x, sprite.rect.y = pygame.mouse.get_pos()
    all_sprites.draw(screen)
    pygame.display.flip()
    screen.fill((0, 0, 0))
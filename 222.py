import pygame


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

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def set_view(self, a, b, n):
        for x in range(self.n):
            for y in range(self.m):
                coor = ((a + x * n, b + y * n),
                        (a + (x + 1) * n, b + (y + 1) * n))
                pygame.draw.rect(screen, (255, 255, 255), coor, width=2)


board = Board(5, 7)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    board.set_view(100, 100, 50)
    pygame.display.flip()
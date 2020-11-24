import pygame

n = input()
if n.isdigit():
    n = int(n)
    pygame.init()
    x, y = 600, 600
    size = width, height = x, y
    screen = pygame.display.set_mode(size)
    screen.fill((200, 200, 150))
    for i in range(x // n):
        for k in range(y // n):
            coor = ((n * k + n // 2, n * i),
                    (n * k + n, n // 2 + n * i),
                    (n * k + n // 2, n + n * i),
                    (n * k, n * i + n // 2))
            pygame.draw.polygon(screen, (240, 150, 100), coor, width=0)
    pygame.display.flip()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
else:
    print('Неправильный формат ввода')

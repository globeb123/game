import pygame 
 
score1 = 0
score2 = 0

score11 = str(score1)
score12 = str(score2)
 
pygame.init()

win_width = 900
win_height = 600
bg = pygame.image.load("game/images/background.png")

bg = pygame.transform.scale(bg, (win_width, win_height))

clock = pygame.time.Clock()

window = pygame.display.set_mode((win_width, win_height))
window_rect = window.get_rect()

pygame.display.set_caption("PIRATES")
exit = False

width = 50
height = 50

margin = 10

block = pygame.image.load("game/images/grass.png")
block1 = pygame.transform.scale(block, (width, height))

ship = pygame.image.load("game/images/ship.png")
ship1 = pygame.transform.scale(ship, (width, height))

font = pygame.font.Font(None, 36)

mas = [[0]*10 for i in range(10)]

while not exit:
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            exit = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            print (f'x = {x_mouse} y = {y_mouse}')
            column = x_mouse//(margin + width)
            row = y_mouse//(margin+height)
            mas [row] [column] = 1

    window.blit(bg, (0, 0))
    for row in range (10):
        for col in range(10):
            if mas [row][col] == 1:
                block = ship1
            else:
                block = block1
            x = col * width + (col + 1)*margin
            y = row * height + (row + 1)*margin
        
            window.blit(block, (x, y))
    window.blit(font.render('Score ' + score11 + " : " + score12, True, (0, 0, 0)), (700, 100))
    clock.tick(60)
    pygame.display.update()
import pygame
import pygame.font
 
 
 
pygame.init()

win_width = 1100
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

window.blit(bg, (0, 0))

mas = [[0]*10 for i in range(10)]

while not exit:
    pygame.display.update()
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            exit = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            print (f'x = {x_mouse} y = {y_mouse}')
            column = x_mouse//(margin + width)
            row = y_mouse//(margin+height)
            mas [row] [column] = 1

for row in range (10):
    for col in range(10):
        if mas [row] [column] == 1:
            block = pygame.image.load("game/images/grass.png")
        else:
            block = pygame.image.load("game/images/ship.png")
        x = col * width + (col + 1)*margin
        y = row * height + (row + 1)*margin
    
        window.blit(block1, (x, y))
import pygame
from random import randint
 

score2 = 0

score12 = str(score2)
 
pygame.init()

win_width = 900
win_height = 600
bg = pygame.image.load("images/background.png")

bg = pygame.transform.scale(bg, (win_width, win_height))

clock = pygame.time.Clock()

window = pygame.display.set_mode((win_width, win_height))
window_rect = window.get_rect()

pygame.display.set_caption("PIRATES")
exit = False

width = 50
height = 50

margin = 10

# block = pygame.image.load("game/images/grass.png")
# block = pygame.transform.scale(block, (width, height))

class Ship(pygame.sprite.Sprite):
    def __init__(self, img, x, y) -> None:
        super().__init__()
        self.image_open = pygame.image.load(img)
        self.image_open = pygame.transform.scale(self.image_open, (width, height))
        self.image_closed = pygame.image.load("images/grass.png")
        self.image_closed = pygame.transform.scale(self.image_closed, (width, height))
        self.image = self.image_closed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.enemy = False
        self.isOpen = False
    
    def open(self):
        self.isOpen = True
        self.image = self.image_open
        return self.enemy

    def show(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


ship_enemy = pygame.image.load("images/ship2.png")
ship_enemy = pygame.transform.scale(ship_enemy, (width, height))

font = pygame.font.Font(None, 36)

mas: list[list[Ship]] = []
for row in range(10):
    temp = []
    for col in range(10):
        x = col * width + (col + 1)*margin
        y = row * height + (row + 1)*margin
        temp.append(Ship("images/ship.png", x, y))
    mas.append(temp)

enemy = mas[randint(0, 9)][randint(0, 9)]
enemy.image_open = ship_enemy
enemy.enemy = True

finish = False

while not exit:
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            exit = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if finish:
                break
            x_mouse, y_mouse = pygame.mouse.get_pos()
            print (f'x = {x_mouse} y = {y_mouse}')
            column = x_mouse//(margin + width)
            row = y_mouse//(margin+height)
            if mas [row] [column].open():
                finish = True
    

    window.blit(bg, (0, 0))
    for row in mas:
        for ship in row:
            ship.show()
    if finish:
        window.blit(font.render('Ти програв!', True, (0, 0, 0)), (win_width/2, win_height/2))
    elif event.type == pygame.MOUSEBUTTONDOWN:
        score2 = score2 + 1
        score12 = str(score2)
    window.blit(font.render('Score ' + " : " + score12, True, (0, 0, 0)), (700, 100))
    clock.tick(60)
    pygame.display.update()
import pygame
import pygame.font
 
 
 
pygame.init()

win_width = 1200
win_height = 900
bg = pygame.image.load("game/images/background.png")

bg = pygame.transform.scale(bg, (win_width, win_height))

clock = pygame.time.Clock()

window = pygame.display.set_mode((win_width, win_height))
window_rect = window.get_rect()

pygame.display.set_caption("PIRATES")
exit = False
    
while not exit:
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            exit = True
    window.blit(bg, (0, 0))
    pygame.display.update()

class block(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height) -> None:
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill('red')
        self.rect = self.image.get_rect()
        self.init_x = x
        self.init_y = y
        self.rect.x = x
        self.rect.y = y
        self.width = width
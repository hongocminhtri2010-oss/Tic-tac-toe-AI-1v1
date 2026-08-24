import pygame
pygame.init()

pygame.display.set_caption("Tic Tac Toe")
screen=pygame.display.set_mode((801,801))
clock=pygame.time.Clock()

running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT: running=False
        
        
        
    clock.tick(60)

pygame.quit()

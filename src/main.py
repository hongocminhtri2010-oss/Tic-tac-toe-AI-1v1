import pygame
import sys
pygame.init()

pygame.display.set_caption("Tic Tac Toe")
screen=pygame.display.set_mode((801,801))
clock=pygame.time.Clock()
font=pygame.font.Font(None,96)

white=(255,255,255)
setboard=801//3

def drawline(start_x,start_y,end_x,end_y): pygame.draw.line(screen,white,(start_x,start_y),(end_x,end_y),5)
def drawboard():
    drawline(0,setboard,801,setboard)
    drawline(0,setboard*2,801,setboard*2)
    drawline(setboard,0,setboard,801)
    drawline(setboard*2,0,setboard*2,801)

turn=1
who=-1
step=0
res=""
board=[0]*9
#Draw=0; Human=1; AI=2

def check_winner():
    global who
    for i in range(0,7,3):
        if board[i]==board[i+1]==board[i+2]==1: who=1
        if board[i]==board[i+1]==board[i+2]==2: who=2
    for i in range(3):
        if board[i]==board[i+3]==board[i+6]==1: who=1
        if board[i]==board[i+3]==board[i+6]==2: who=2
    if board[0]==board[4]==board[8]==1: who=1
    if board[0]==board[4]==board[8]==2: who=2
    if board[2]==board[4]==board[6]==1: who=1
    if board[2]==board[4]==board[6]==2: who=2
    if step==9 and who==-1:who=0

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

        if who==-1:
            if event.type==pygame.MOUSEBUTTONDOWN and turn:
                x,y=event.pos
                play_Human(x,y)

    if who==-1:
        check_winner()
        if not turn: play_AI()
    
    drawboard() #Get 3x3 board
    if who!=-1:
        if who==0: res="Draw!"
        elif who==1: res="You won!"
        else: res="AI won!"
        
        text=font.render(res,True,white)
        screen.blit(text,(setboard,setboard))
        
    pygame.display.flip()
    clock.tick(60)

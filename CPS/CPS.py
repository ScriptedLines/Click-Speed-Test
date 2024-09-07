import pygame
from sys import exit

import time
pygame.init()

clock=pygame.time.Clock()



window=pygame.display.set_mode((800,800))
pygame.display.set_caption("Click Speed Test")
font1=pygame.font.Font("Cakewalk.ttf",50)
font2=pygame.font.Font("Cakewalk.ttf",25)


nonclick=pygame.image.load("unclick.png")
nrect=nonclick.get_rect(center=(400,450))

click=pygame.image.load("clicked.png")
crect=nonclick.get_rect(center=(400,450))

text1=font1.render("Welcome top CLick Speed Test!",True,"black")




back=pygame.image.load("background.jpg")


n=0

t=30
fcount=0
times=1





while True:
    clock.tick(60)
    fcount+=1
    window.blit(back,(0,0))

    window.blit(nonclick,nrect)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            if t!=0:
                
                n=n+1

    if fcount%60==0 and fcount<1801:
        t-=1

    if fcount%60==0 and fcount<1801:
        times+=1


    cps=n/times
    result=font2.render(f"Your CPS is {cps}",True,"red")
    resrect=result.get_rect(center=(400,750))
    window.blit(result,resrect)







    
    text2=font2.render(f"Score:{n}",False,"red")
    trect=text2.get_rect(center=(400,210))

    text3=font2.render(f"Timer:{t}s",False,"red")
    t2rect=text3.get_rect(center=(400,700))

    
    
    window.blit(text1,(50,50))
    
    window.blit(text2,trect)
    window.blit(text3,t2rect)

    mousepos=pygame.mouse.get_pos()
    if nrect.collidepoint(mousepos):
        if pygame.mouse.get_pressed()[0]==True:
            window.blit(click,crect)



    pygame.display.update()





import random
import pygame


screen = pygame.display.set_mode((600,450))


def menu_inicial():
    menu=pygame.image.load("tabuleiro.png")
    screen.blit(menu,(0,0))
    pygame.display.update()
  
            
def preencherRicardo():
    telapreta=pygame.image.load("telapreta.png")
    telapreta=pygame.transform.scale(telapreta,(190,190))
    screen.blit(telapreta,(350,25))
    ricardo=pygame.image.load("ricardo3.png")
    ricardo=pygame.transform.scale(ricardo,(190,190))
    screen.blit(ricardo,(350,25))
    
def preencherRicardo2():
    telapreta=pygame.image.load("telapreta.png")
    telapreta=pygame.transform.scale(telapreta,(190,190))
    screen.blit(telapreta,(350,240))
    ricardo=pygame.image.load("ricardo3.png")
    ricardo=pygame.transform.scale(ricardo,(190,190))
    screen.blit(ricardo,(350,240))
    
   
def dancemilos():
        time=pygame.time.Clock()
        ricardo1=pygame.image.load("ricardo1.png")
        ricardo2=pygame.image.load("ricardo2.png")
        ricardo3=pygame.image.load("ricardo3.png")
        ricardo4=pygame.image.load("ricardo4.png")
        ricardo5=pygame.image.load("ricardo5.png")
        ricardo6=pygame.image.load("ricardo6.png")
        ricardo7=pygame.image.load("ricardo7.png")
        ricardo8=pygame.image.load("ricardo8.png")
        ricardo9=pygame.image.load("ricardo9.png")
        ricardo10=pygame.image.load("ricardo10.png")
        ricardo11=pygame.image.load("ricardo11.png")
        ricardo12=pygame.image.load("ricardo0.png")
        ricardo1=pygame.transform.scale(ricardo1,(220,220))
        ricardo2=pygame.transform.scale(ricardo2,(220,220))
        ricardo3=pygame.transform.scale(ricardo3,(220,220))
        ricardo4=pygame.transform.scale(ricardo4,(220,220))
        ricardo5=pygame.transform.scale(ricardo5,(220,220))
        ricardo6=pygame.transform.scale(ricardo6,(220,220))
        ricardo7=pygame.transform.scale(ricardo7,(220,220))
        ricardo8=pygame.transform.scale(ricardo8,(220,220))
        ricardo9=pygame.transform.scale(ricardo9,(220,220))
        ricardo10=pygame.transform.scale(ricardo10,(220,220))
        ricardo11=pygame.transform.scale(ricardo11,(220,220))
        ricardo12=pygame.transform.scale(ricardo12,(220,220))
        telapreta=pygame.image.load("telapreta.png")
        telapreta=pygame.transform.scale(telapreta,(220,220))
        milosfinal=0
        pygame.display.update()
        time.tick(8)   
        if(milosfinal==0):
            screen.blit(ricardo1,(200,230))
            pygame.display.update()
            time.tick(8)
            milosfinal+=1
            screen.blit(telapreta,(200,230))
        if(milosfinal==1):
            screen.blit(ricardo2,(200,230))
            pygame.display.update()
            time.tick(8)
            milosfinal+=1
            screen.blit(telapreta,(200,230))
        if(milosfinal==2):
            screen.blit(ricardo9,(200,230))
            pygame.display.update()
            time.tick(8)
            milosfinal+=1
            screen.blit(telapreta,(200,230))
        if(milosfinal==3):
            screen.blit(ricardo3,(200,230))
            pygame.display.update()
            time.tick(8)
            milosfinal+=1
            screen.blit(telapreta,(200,230))
        if(milosfinal==4):
            screen.blit(ricardo4,(200,230))
            pygame.display.update()
            time.tick(8)
            milosfinal+=1
            screen.blit(telapreta,(200,230))
        if(milosfinal==5):
            screen.blit(ricardo6,(200,230))
            pygame.display.update()
            time.tick(8)
            milosfinal+=1
            screen.blit(telapreta,(200,230))
        if(milosfinal==6):
            screen.blit(ricardo12,(200,230))
            pygame.display.update()
            time.tick(8)
            milosfinal+=1
            screen.blit(telapreta,(200,230))
        if(milosfinal==7):
            screen.blit(ricardo7,(200,230))
            pygame.display.update()
            time.tick(8)
            milosfinal+=1
            screen.blit(telapreta,(200,230))
        if(milosfinal==8):
            screen.blit(ricardo8,(200,230))
            pygame.display.update()
            time.tick(8)
            milosfinal+=1
            screen.blit(telapreta,(200,230))
        if(milosfinal==9):
            screen.blit(ricardo11,(200,230))
            pygame.display.update()
            time.tick(8)
            milosfinal+=1
            screen.blit(telapreta,(200,230))
        if(milosfinal==10):
            screen.blit(ricardo10,(200,230))
            pygame.display.update()
            time.tick(8)
            milosfinal+=1
            screen.blit(telapreta,(200,230))
        if(milosfinal==11):
            screen.blit(ricardo5,(200,230))
            pygame.display.update()
            time.tick(8)
            milosfinal=0
            screen.blit(telapreta,(200,230))
        time.tick(2)

    

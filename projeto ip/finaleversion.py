from funcoes import menu_inicial
from funcoes import preencherRicardo
from funcoes import preencherRicardo2
from funcoes import dancemilos


import random
matriz=[[0]*4 for i in range(4)]
matriz2 = [[False for i in range(4)] for j in range(4)]
numerot=0
#preencheTabuleiro("T", 6)
#preencheBuraco("B", 3)
#preencherContagem()



import pygame
white=(255,255,255)
black=(0,0,0)
grenn=(0,255,0)
red=(255,0,0)
blue=(0,0,255)


pygame.init()


cont=0
while (cont < 6):
  na = random.randint(0,15)
  pos = 0
  na2= random.randint(0,100)
  for i in range(4):
     for j in range(4):
        if (pos == na and matriz[i][j] == 0):
           if(na2>37):
              matriz[i][j] = "T"
              cont += 1    
        pos += 1



cont=0
while (cont < 3):
  na = random.randint(0,15)
  pos = 0
  na2= random.randint(0,100)
  for i in range(4):
     for j in range(4):
        if (pos == na and matriz[i][j] == 0):
           if(na2 > 18):
              matriz[i][j] = "B"
              cont += 1    
        pos += 1





for i in range(0,4):
   for j in range(0,4):
      if (matriz[i][j] != "T" and matriz[i][j]!="B"):
         numerot = 0

     # Acima
         if (i - 1 >= 0 and matriz[i - 1][j]) == "T" :
            numerot += 1

     # Esquerda   
         if (j - 1 >= 0 and matriz[i][j - 1]) == "T" :
            numerot += 1

     # Direita   
         if (j + 1 < 4 and matriz[i][j + 1]) == "T" :
            numerot+= 1

     # Abaixo   
         if (i + 1 < 4 and matriz[i + 1][j]) == "T":
            numerot += 1
        
         matriz[i][j] = str(numerot)
        
for j in range(4): #So pra printar a matriz
   for i in range(4):
        print(matriz[i][j], end = " ")
   print()











screen = pygame.display.set_mode((600,450))
pygame.display.set_caption("Caça ao Tesouro")

menu_inicial()
baudetesouros1=0
baudetesouros2=0
contador1=0
lado_celula_x=80
lado_celula_y=110
jogadordavez=1
jogador1=pygame.image.load("ricardo1.png")
jogador1=pygame.transform.scale(jogador1,(190,190))
screen.blit(jogador1,(350,25))
jogador2=pygame.image.load("ricardo1.png")
jogador2=pygame.transform.scale(jogador2,(200,200))
screen.blit(jogador2,(350,230))
jogador12=False
jogador21=False
jogador33=False
pygame.font.init()

font=pygame.font.get_default_font()
pontos1=pygame.font.SysFont(font,30)
            
jogo=True
func = True
jogador1 = True
jogador2 = False

pygame.mixer.music.load("musica2.ogg")
pygame.mixer.music.play(1)
while jogo and contador1!=16:
    cair1=pygame.mixer.Sound("cair1.ogg")
    tesouro1=pygame.mixer.Sound("tesouro.ogg")
    pygame.mixer.Channel(0).set_volume(0.3)
    buraco=pygame.image.load("buraco.png")
    buraco=pygame.transform.scale(buraco,(120,80))
    
    while (func):
        telapreta=pygame.image.load("telapreta.png")
        telapreta=pygame.transform.scale(telapreta,(50,30))
        screen.blit(telapreta,(497,5))
        screen.blit(telapreta,(497,220))
        baudetesouros11 = pontos1.render("Jogador1:"+str(baudetesouros1),True,white)
        baudetesouros22 = pontos1.render("Jogador2:"+str(baudetesouros2),True,white)
        screen.blit(baudetesouros22,(400,220))
        screen.blit(baudetesouros11,(400,5))
        pygame.display.update()

        while jogador1 and contador1!=16:
            for evento in pygame.event.get():
                if(evento.type==pygame.QUIT):
                    jogo=False
                    func =False
                    jogador2 = False
                    jogador1 = False

                if(evento.type==pygame.MOUSEBUTTONDOWN and evento.button==1):
                    mouse_x,mouse_y = evento.pos
                    celula_x = mouse_x // lado_celula_x
                    celula_y = mouse_y // lado_celula_y
                    if(celula_x >= 0 and celula_x < 4 and matriz2[celula_x][celula_y] != True ):
                        if(matriz[celula_x][celula_y]=="B"):
                            pygame.mixer.Channel(0).play(cair1)
                            buraco=pygame.image.load("buraco.png")
                            buraco=pygame.transform.scale(buraco,(50,80))
                            telapreta=pygame.image.load("telapreta.png")
                            telapreta=pygame.transform.scale(telapreta,(190,190))
                            screen.blit(telapreta,(350,25))
                            screen.blit(buraco,(lado_celula_x*celula_x+2,lado_celula_y*celula_y+10))
                            ricardo=pygame.image.load("ricardo2.png")
                            ricardo=pygame.transform.scale(ricardo,(190,190))
                            screen.blit(ricardo,(350,25))
                            pygame.display.update()
                            matriz2[celula_x][celula_y]=True
                            contador1+=1
                            jogador2 = True
                            jogador1 = False
                            if(baudetesouros1>0):
                                baudetesouros1=baudetesouros1-50
                            pygame.display.update()
                        elif(matriz[celula_x][celula_y]=="T"):
                            pygame.mixer.Channel(0).play(tesouro1)
                            tesouro=pygame.image.load("tesouro1.png")
                            telapreta=pygame.image.load("telapreta.png")
                            telapreta=pygame.transform.scale(telapreta,(190,190))
                            screen.blit(telapreta,(350,25))
                            ricardo=pygame.image.load("ricardo4.png")
                            ricardo=pygame.transform.scale(ricardo,(190,190))
                            screen.blit(ricardo,(350,25))
                            tesouro=pygame.transform.scale(tesouro,(50,80))
                            screen.blit(tesouro,(lado_celula_x*celula_x+2,lado_celula_y*celula_y+10))
                            baudetesouros1+=100
                            matriz2[celula_x][celula_y]=True
                            pygame.display.update()
                            contador1+=1
                            jogador2 = True
                            jogador1 = False
                        else:
                            if(matriz[celula_x][celula_y]=="0"):
                                numero0=pygame.image.load("numero0.png")
                                numero0=pygame.transform.scale(numero0,(50,80))
                                preencherRicardo()
                                screen.blit(numero0,(lado_celula_x*celula_x+1,lado_celula_y*celula_y+10))
                                matriz2[celula_x][celula_y]=True
                                pygame.display.update()
                                contador1+=1
                                jogador2 = True
                                jogador1 = False
                            elif(matriz[celula_x][celula_y]=="1"):
                                numero1=pygame.image.load("numero1.png")
                                numero1=pygame.transform.scale(numero1,(50,80))
                                preencherRicardo()
                                screen.blit(numero1,(lado_celula_x*celula_x+1,lado_celula_y*celula_y+10))
                                matriz2[celula_x][celula_y]=True
                                pygame.display.update()
                                contador1+=1
                                jogador2 = True
                                jogador1 = False
                            elif(matriz[celula_x][celula_y]=="2"):
                                numero2=pygame.image.load("numero2.png")
                                numero2=pygame.transform.scale(numero2,(50,80))
                                preencherRicardo()
                                screen.blit(numero2,(lado_celula_x*celula_x+1,lado_celula_y*celula_y+10))
                                matriz2[celula_x][celula_y]=True
                                pygame.display.update()
                                contador1+=1
                                jogador2 = True
                                jogador1 = False
                            elif(matriz[celula_x][celula_y]=="3"):
                                numero3=pygame.image.load("numero3.png")
                                numero3=pygame.transform.scale(numero3,(50,80))
                                preencherRicardo()
                                screen.blit(numero3,(lado_celula_x*celula_x+1,lado_celula_y*celula_y+10))
                                matriz2[celula_x][celula_y]=True
                                pygame.display.update()
                                contador1+=1
                                jogador2 = True
                                jogador1 = False
                            elif(matriz[celula_x][celula_y]=="4"):
                                numero4=pygame.image.load("numero4.png")
                                numero4=pygame.transform.scale(numero4,(50,80))
                                preencherRicardo()
                                screen.blit(numero4,(lado_celula_x*celula_x+1,lado_celula_y*celula_y+10))
                                matriz2[celula_x][celula_y]=True
                                pygame.display.update()
                                contador1+=1
                                jogador2 = True
                                jogador1 = False

                        print(contador1)
                        print("dinheiro 1 bau:{}".format(baudetesouros1))
                        if contador1 == 16:
                            jogador1 = False
                            jogador2 = False
                            func = False
                            break;
        telapreta=pygame.image.load("telapreta.png")
        telapreta=pygame.transform.scale(telapreta,(50,30))
        screen.blit(telapreta,(497,5))
        screen.blit(telapreta,(497,220))
        baudetesouros11 = pontos1.render("Jogador1:"+str(baudetesouros1),True,white)
        baudetesouros22 = pontos1.render("Jogador2:"+str(baudetesouros2),True,white)
        screen.blit(baudetesouros22,(400,220))
        screen.blit(baudetesouros11,(400,5))
        pygame.display.update()

        while jogador2 and contador1!=16:
            for evento in pygame.event.get():
                if(evento.type==pygame.QUIT):
                    jogo=False
                    func =False
                    jogador2 = False
                    jogador1 = False

                if(evento.type==pygame.MOUSEBUTTONDOWN and evento.button==1):
                    mouse_x,mouse_y = evento.pos
                    celula_x = mouse_x // lado_celula_x
                    celula_y = mouse_y // lado_celula_y
                if(celula_x >= 0 and celula_x < 4 and matriz2[celula_x][celula_y] != True):
                    if(matriz[celula_x][celula_y]=="B"):
                        pygame.mixer.Channel(0).play(cair1)
                        buraco=pygame.image.load("buraco.png")
                        buraco=pygame.transform.scale(buraco,(50,80))
                        telapreta=pygame.image.load("telapreta.png")
                        telapreta=pygame.transform.scale(telapreta,(190,190))
                        screen.blit(telapreta,(350,240))
                        screen.blit(buraco,(lado_celula_x*celula_x+2,lado_celula_y*celula_y+10))
                        ricardo=pygame.image.load("ricardo2.png")
                        ricardo=pygame.transform.scale(ricardo,(190,190))
                        screen.blit(ricardo,(350,240))
                        matriz2[celula_x][celula_y]=True
                        pygame.display.update()
                        contador1+=1
                        jogador2 = False
                        jogador1 = True
                        if(baudetesouros2>0):
                            baudetesouros2=baudetesouros2-50
                        pygame.display.update()
                    elif(matriz[celula_x][celula_y]=="T"):
                        pygame.mixer.Channel(0).play(tesouro1)
                        tesouro=pygame.image.load("tesouro1.png")
                        telapreta=pygame.image.load("telapreta.png")
                        telapreta=pygame.transform.scale(telapreta,(190,190))
                        screen.blit(telapreta,(350,240))
                        ricardo=pygame.image.load("ricardo4.png")
                        ricardo=pygame.transform.scale(ricardo,(190,190))
                        screen.blit(ricardo,(350,240))
                        tesouro=pygame.transform.scale(tesouro,(50,80))
                        screen.blit(tesouro,(lado_celula_x*celula_x+2,lado_celula_y*celula_y+10))
                        baudetesouros2=baudetesouros2+100
                        matriz2[celula_x][celula_y]=True
                        pygame.display.update()
                        contador1+=1
                        jogador2 = False
                        jogador1 = True
                    else:
                        if(matriz[celula_x][celula_y]=="0"):
                            numero0=pygame.image.load("numero0.png")
                            numero0=pygame.transform.scale(numero0,(50,80))
                            preencherRicardo2()
                            screen.blit(numero0,(lado_celula_x*celula_x+1,lado_celula_y*celula_y+10))
                            matriz2[celula_x][celula_y]=True
                            pygame.display.update()
                            contador1+=1
                            jogador2 = False
                            jogador1 = True
                        elif(matriz[celula_x][celula_y]=="1"):
                            numero1=pygame.image.load("numero1.png")
                            numero1=pygame.transform.scale(numero1,(50,80))
                            preencherRicardo2()
                            screen.blit(numero1,(lado_celula_x*celula_x+1,lado_celula_y*celula_y+10))
                            matriz2[celula_x][celula_y]=True
                            pygame.display.update()
                            contador1+=1
                            jogador2 = False
                            jogador1 = True
                        elif(matriz[celula_x][celula_y]=="2"):
                            numero2=pygame.image.load("numero2.png")
                            numero2=pygame.transform.scale(numero2,(50,80))
                            preencherRicardo2()
                            screen.blit(numero2,(lado_celula_x*celula_x+1,lado_celula_y*celula_y+10))
                            matriz2[celula_x][celula_y]=True
                            pygame.display.update()
                            contador1+=1
                            jogador2 = False
                            jogador1 = True
                        elif(matriz[celula_x][celula_y]=="3"):
                            numero3=pygame.image.load("numero3.png")
                            numero3=pygame.transform.scale(numero3,(50,80))
                            preencherRicardo2()
                            screen.blit(numero3,(lado_celula_x*celula_x+1,lado_celula_y*celula_y+10))
                            matriz2[celula_x][celula_y]=True
                            pygame.display.update()
                            contador1+=1
                            jogador2 = False
                            jogador1 = True
                        elif(matriz[celula_x][celula_y]=="4"):
                            numero4=pygame.image.load("numero4.png")
                            numero4=pygame.transform.scale(numero4,(50,80))
                            preencherRicardo2()
                            screen.blit(numero4,(lado_celula_x*celula_x+1,lado_celula_y*celula_y+10))
                            matriz2[celula_x][celula_y]=True
                            pygame.display.update()
                            contador1+=1
                            jogador2 = False
                            jogador1 = True
                        else:
                            pass
                    print(contador1)
                    print("dinheiro do 2 bau:{}".format(baudetesouros2))
                    if contador1 == 16:
                            jogador1 = False
                            jogador2 = False
                            func = False
                            break;
    

    if(baudetesouros1>baudetesouros2):
        jogador12=True
        print(jogador12)
    elif(baudetesouros2>baudetesouros1):
        jogador21=True
        print(jogador21)
    elif(baudetesouros1==baudetesouros2):
        jogador33=True
        print(jogador33)
        
    pygame.display.update()
    
    if(jogador12==True):
      if(evento.type==pygame.QUIT):
        jogo=False
        jogador12==False 
      pygame.font.init()
      font=pygame.font.get_default_font()
      pontos1=pygame.font.SysFont(font,30)
      vencedor = pontos1.render("Jogador1 Venceu",True,white)
      screen.fill(black)
      screen.blit(vencedor,(200,100))
      dancemilos()
    elif(jogador21==True):
      if(evento.type==pygame.QUIT):
        jogo=False
        jogador21==False 
      pygame.font.init()
      font=pygame.font.get_default_font()
      pontos1=pygame.font.SysFont(font,30)
      vencedor = pontos1.render("Jogador2 Venceu",True,white)
      screen.fill(black)
      screen.blit(vencedor,(200,100))
      dancemilos()
    elif(jogador33==True):
      if(evento.type==pygame.QUIT):
        jogo=False
        jogador33==False 
      pygame.font.init()
      font=pygame.font.get_default_font()
      pontos1=pygame.font.SysFont(font,30)
      vencedor = pontos1.render("Empatou ",True,white)
      screen.fill(black)
      screen.blit(vencedor,(200,100))
      dancemilos()
pygame.quit()


import pygame
from random import randint

pygame.init()
Inicio=True
pygame.display.set_caption("Snake")
ventana=pygame.display.set_mode((1000,1000))
fps=pygame.time.Clock()


#Clase serpiente
class Serpiente:
    def __init__(self):
        self.Cuerpo=[]
        self.rect=pygame.Rect(500,500,20,20)
        self.direccion_x=0
        self.direccion_y=0
        self.velocidad=5
        self.Puntaje=0
        

    def Dibujar(self):
        self.Cabeza=pygame.draw.rect(ventana,(4, 92, 29),self.rect)
        for segmento in self.Cuerpo:
            pygame.draw.rect(ventana,(4, 150, 60),(self.rect.x - (len(self.Cuerpo)*20),self.rect.y,20,20))
    

    def Movimiento(self):
        for pulsado in pygame.event.get():
            if pulsado.type== pygame.KEYDOWN:

                #Arriba
                if pulsado.key== pygame.K_w:
                        if self.direccion_y==0:
                            self.direccion_y= -self.velocidad
                            self.direccion_x=0
                          
                #Abajo
                elif pulsado.key== pygame.K_s:
                    if self.direccion_y==0:
                        self.direccion_y= self.velocidad
                        self.direccion_x=0

                #izquierda
                elif pulsado.key== pygame.K_a:
                    if self.direccion_x==0:
                        self.direccion_x= -self.velocidad
                        self.direccion_y=0
                       
                #derecha
                elif pulsado.key== pygame.K_d:
                    if self.direccion_x==0:
                        self.direccion_x= self.velocidad
                        self.direccion_y=0

        self.rect.y+=self.direccion_y
        self.rect.x+=self.direccion_x

                

#Clase Fruta
class Fruta:
    def __init__(self):
        self.PosX=randint(10,800)
        self.PosY=randint(10,800)

    def Dibujar(self):
        self.Dibujo_Fruta=pygame.draw.circle(ventana,"red",(self.PosX,self.PosY),15,0)
    
    def Colision(self):
        if self.Dibujo_Fruta.colliderect(serpiente.Cabeza):
            serpiente.Puntaje+=1
            self.PosX=randint(10,800)
            self.PosY=randint(10,800)
            serpiente.Cuerpo.append(1)

    


        
fruta=Fruta()
serpiente=Serpiente()

while Inicio:
    ventana.fill((233, 247, 164))
    fps.tick(60)
    fruta.Dibujar()
    serpiente.Dibujar()
    serpiente.Movimiento()
    txtPuntos=pygame.font.SysFont("TimesNewRoman",40).render(f"Puntos: {serpiente.Puntaje}",True,(0,0,0))
    rectPuntos=txtPuntos.get_rect()
    rectPuntos.top=(100)
    rectPuntos.left=(400)
    ventana.blit(txtPuntos,rectPuntos)
    fruta.Colision()
    



    pygame.display.flip()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()
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
        

    def Dibujar(self):
        self.Cabeza=pygame.draw.rect(ventana,(4, 92, 29),self.rect)
    

    def Movimiento(self):
        for pulsado in pygame.event.get():
            if pulsado.type== pygame.KEYDOWN:
                #Arriba
                if pulsado.key== pygame.K_w:
                        self.direccion_y= -self.velocidad
                        self.direccion_x=0
                        print(f"{self.direccion_y}")
                #Abajo
                elif pulsado.key== pygame.K_s:
                    if self.direccion_y==0:
                        self.direccion_y= self.velocidad
                        self.direccion_x=0

                #izquierda
                elif pulsado.key== pygame.K_a:
                    self.direccion_x= -self.velocidad
                    self.direccion_y=0
                    print(f"{self.direccion_y}")
                #derecha
                elif pulsado.key== pygame.K_d:
                    self.direccion_x= self.velocidad
                    self.direccion_y=0

        self.rect.y+=self.direccion_y
        self.rect.x+=self.direccion_x

                

                
              








#Clase Fruta
class Fruta:
    def __init__(self):
        self.PosX=randint(10,900)
        self.PosY=randint(10,900)

    def Dibujar(self):
        self.Dibujo_Fruta=pygame.draw.circle(ventana,"red",(self.PosX,self.PosY),15,0)

        
fruta=Fruta()
serpiente=Serpiente()

while Inicio:
    ventana.fill((233, 247, 164))
    fps.tick(60)
    fruta.Dibujar()
    serpiente.Dibujar()
    serpiente.Movimiento()
    
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()
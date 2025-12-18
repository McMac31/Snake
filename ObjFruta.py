import pygame
from Interfaz import ventana
from JuegoSnake import serpiente
from random import randint

#Clase Fruta
class Fruta:
    def __init__(self):
        self.PosX=randint(15,685)
        self.PosY=randint(15,685)

    def Dibujar(self):
        self.Dibujo_Fruta=pygame.draw.circle(ventana,"red",(self.PosX,self.PosY),15,0)
    
    def Colision(self):
        if self.Dibujo_Fruta.colliderect(serpiente.rect): # Usamos .rect para detectar mejor el choque
            serpiente.Puntaje += 1
            self.PosX = randint(15,685)
            self.PosY = randint(15,685)     
import pygame
from Interfaz import ventana


#Clase serpiente
class Serpiente:
    def __init__(self):
        self.Cuerpo=[]
        self.rect=pygame.Rect(350,350,20,20)
        self.direccion_x=0
        self.direccion_y=0
        self.velocidad=20
        self.Puntaje=0
        

    def Dibujar(self):
        self.Cabeza=pygame.draw.rect(ventana,(4, 92, 29),self.rect)
        for segmento in self.Cuerpo:
            pygame.draw.rect(ventana,(4, 92, 29),segmento)
    

    def Movimiento(self,eventos):
        
        for pulsado in eventos:
            if pulsado.type == pygame.KEYDOWN:
                # Arriba 
                if pulsado.key == pygame.K_w and self.direccion_y == 0: # Evitar que se mueva en la dirección opuesta
                    self.direccion_y = -self.velocidad
                    self.direccion_x = 0
                # Abajo
                elif pulsado.key == pygame.K_s and self.direccion_y == 0: # Evitar que se mueva en la dirección opuesta
                    self.direccion_y = self.velocidad
                    self.direccion_x = 0
                # Izquierda
                elif pulsado.key == pygame.K_a and self.direccion_x == 0: # Evitar que se mueva en la dirección opuesta
                    self.direccion_x = -self.velocidad
                    self.direccion_y = 0
                # Derecha
                elif pulsado.key == pygame.K_d and self.direccion_x == 0: # Evitar que se mueva en la dirección opuesta
                    self.direccion_x = self.velocidad 
                    self.direccion_y = 0

     
        
        # Antes de movernos, hacemos una copia de donde estamos y la guardamos
        posicion_actual = self.rect.copy()
        self.Cuerpo.append(posicion_actual)

        # Movimiento perpetuo de la serpiente
        self.rect.y += self.direccion_y
        self.rect.x += self.direccion_x

        if len(self.Cuerpo) > self.Puntaje:
            self.Cuerpo.pop(0)
    

    def Muerte(self):
        # Colisión con los bordes
        if (self.rect.left < 0 or self.rect.right > 700 or
            self.rect.top < 0 or self.rect.bottom > 700):
            return True
        # Colisión con el cuerpo
        for segmento in self.Cuerpo[:-1]:  # Excluir la cabeza
            if self.rect.colliderect(segmento):
                return True
            
        return False
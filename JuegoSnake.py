import pygame
from random import randint
from ObjSerpiente import Serpiente
from Interfaz import ventana,Inicio,fps
from ObjFruta import Fruta

fruta=Fruta()
serpiente=Serpiente()
GameOver=False
while Inicio:
    eventos=pygame.event.get()
    ventana.fill((233, 247, 164))
    fps.tick(18)
    fruta.Dibujar()
    serpiente.Dibujar()
    if not GameOver:
        serpiente.Movimiento(eventos)
        fruta.Colision()
  
    txtPuntos=pygame.font.SysFont("TimesNewRoman",40).render(f"Puntos: {serpiente.Puntaje}",True,(0,0,0))
    rectPuntos=txtPuntos.get_rect()
    rectPuntos.top=(10)
    rectPuntos.left=(300)
    if serpiente.Muerte():
        GameOver=True


    if GameOver:
        txtGameOver=pygame.font.SysFont("TimesNewRoman",80).render("PERDISTE",True,(255,0,0))
        rectGameOver=txtGameOver.get_rect()
        rectGameOver.center=(350,350)
        ventana.blit(txtGameOver,rectGameOver)
    ventana.blit(txtPuntos,rectPuntos)
    
    pygame.display.flip()
    for evento in eventos:
        if evento.type==pygame.QUIT:
            pygame.quit()
            quit()
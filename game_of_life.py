import time
from turtle import update 
import pygame
import numpy as np

fondo = (50, 50, 50)
grid = (30, 30, 30)
muerte = (100, 100, 100)
vida = (150, 150, 150)

#Función para actualizar el estado de la matriz de células.
def actualizar(pantalla, celda, tamano, progreso=False):
    celda_actualizada = np.empty((celda.shape[0], celda.shape[1])) #Array vacío para almacenar el estado de las células.

    for row, col in np.ndindex(celda.shape): #Recorremos la matriz de células para ver su estado.
        vid = celda[row-1:row+2, col-1:col+2] #Obtenemos los vecinos de la célula actual.
        vecinos = np.sum(vid) - celda[row, col] #Sumamos los vecinos y restamos la célula actual.
        color = fondo if celda[row, col] == 0 else vida

        if celda[row, col] == 1: # Si la célula está viva.
            if vecinos < 2 or vecinos > 3: # Si tiene menos de 2 o más de 3 vecinos, muere.
                if progreso: # Si se está mostrando el progreso, se dibuja la célula muerta.
                    color = muerte
                    celda_actualizada[row, col] = 0
            elif 2 <= vecinos <= 3: # Si tiene 2 o 3 vecinos, sobrevive.
                celda_actualizada[row, col] = 1
                if progreso: # Si se está mostrando el progreso, se dibuja la célula viva.
                    color = vida
        else: # Si la célula está muerta.
            if vecinos == 3:
                celda_actualizada[row, col] = 1
                if progreso: # Si se está mostrando el progreso, se dibuja la célula viva.
                    color = vida
        
        pygame.draw.rect(pantalla, color, (col*tamano, row*tamano, tamano - 1, tamano - 1)) #Dibujamos la célula.
        
        return celda_actualizada

def main():
    pygame.init()
    pygame.display.set_caption("Game of Life")
    pantalla = pygame.display.set_mode((800, 600))
    
    cells = np.zeros((600//10, 800//10)) #Matriz de células.
    pantalla.fill(fondo)
    actualizar(pantalla, cells, 10)
    
    pygame.display.flip()
    pygame.display.update()

    r = False #Variable para saber si se está mostrando el progreso.
    
    while not r: #Bucle principal.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # = True
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN: #Si se pulsa una tecla se muestra el progreso.
                if event.key == pygame.K_SPACE: #Si se pulsa la barra espaciadora, se muestra el progreso.
                    r = True
                    actualizar(pantalla, cells, 10) #Actualizamos el estado de las células.
                    pygame.display.update()

            if pygame.mouse.get_pressed()[0]: #Si se pulsa el ratón, se cambia el estado de la célula.
                x, y = pygame.mouse.get_pos()
                cells[y//10, x//10] = 1
                pygame.draw.rect(pantalla, vida, (x//10*10, y//10*10, 10 - 1, 10 - 1))
                pygame.display.update()

        pantalla.fill(grid) #Dibujamos la cuadrícula.
        if r: #Si se está mostrando el progreso, se actualiza el estado de las células.
            cells = actualizar(pantalla, cells, 10, progreso = True)
            pygame.display.update()
        
        time.sleep(0.001)

if __name__ == "__main__":
    main()
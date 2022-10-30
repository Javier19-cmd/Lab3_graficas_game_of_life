"""
Nombre: Javier Sebastián Valle Balsells
Carnet: 20159
Referencia: https://www.youtube.com/watch?v=cRWg2SWuXtM
"""

import time
#from turtle import update 
import pygame
import numpy as np

fondo = (50, 50, 50)
grid = (30, 30, 30)
muerte = (100, 100, 100)
vida = (150, 150, 150)

#Función para actualizar el estado de la matriz de células.
def actualizar(pantalla, celda, tamano, progreso=False):
    celda_actualizada = np.zeros((celda.shape[0], celda.shape[1])) #Array vacío para almacenar el estado de las células.

    for row, col in np.ndindex(celda.shape): #Recorremos la matriz de células para ver su estado.
        vid = np.sum(celda[row-1:row+2, col-1:col+2]) - celda[row, col] #Obtenemos los vecinos de la célula actual.
        #vecinos = np.sum(vid) - celda[row, col] #Sumamos los vecinos y restamos la célula actual.
        color = fondo if celda[row, col] == 0 else vida

        if celda[row, col] == 1: # Si la célula está viva.
            if vid < 2 or vid > 3: # Si tiene menos de 2 o más de 3 vecinos, muere.
                if progreso: # Si se está mostrando el progreso, se dibuja la célula muerta.
                    color = muerte
                    #celda_actualizada[row, col] = 0
            elif 2 <= vid <= 3: # Si tiene 2 o 3 vecinos, sobrevive.
                celda_actualizada[row, col] = 1
                if progreso: # Si se está mostrando el progreso, se dibuja la célula viva.
                    color = vida
        else: # Si la célula está muerta.
            if vid == 3:
                celda_actualizada[row, col] = 1
                if progreso: # Si se está mostrando el progreso, se dibuja la célula viva.
                    color = vida
        
        pygame.draw.rect(pantalla, color, (col*tamano, row*tamano, tamano - 1, tamano - 1)) #Dibujamos la célula.
        
    return celda_actualizada

def main():
    pygame.init()
    pygame.display.set_caption("Laboratorio 3 - Juego de la vida")
    pantalla = pygame.display.set_mode((650, 650))
    
    cells = np.zeros((600//10, 800//10)) #Matriz de células.
    pantalla.fill(fondo)
    actualizar(pantalla, cells, 10)
    
    pygame.display.flip()
    pygame.display.update()

    r = False #Variable para saber si se está mostrando el progreso.

    puntos = [
        [20, 20],
        [20, 21], 
        [20, 22], 
        [20, 23], 
        [25, 13],
        [25, 14],
        [25, 15],
        [25, 16],
        [25, 17],
        [25, 18],
        [25, 19],
        [25, 20],
        [29, 21],
        [30, 21],
        [29, 22],
        [30, 22],
        [29, 23],
        [30, 23],
        [35, 5],
        [35, 6],
        [36, 5],
        [36, 6],
        [37, 7],
        [37, 8],
        [38, 7],
        [35, 8],
        [50, 25],
        [51, 26],
        [52, 24],
        [52, 25],
        [52, 26],
        [52, 27],
    ] #Puntos iniciales.

    #Recorremos la lista de puntos iniciales y cambiamos el estado de las células.
    for punto in puntos:
        cells[punto[0], punto[1]] = 1
        pygame.draw.rect(pantalla, vida, (punto[1]*10, punto[0]*10, 10 - 1, 10 - 1))
        actualizar(pantalla, cells, 10)
        pygame.display.update()
    
    while True: #Bucle principal.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # = True
                pygame.quit()
                return
            # if event.type == pygame.KEYDOWN: #Si se pulsa una tecla se muestra el progreso.
            #     if event.key == pygame.K_SPACE: #Si se pulsa la barra espaciadora, se muestra el progreso.
            #         r = not r #Cambiamos el valor de la variable.    
            #         actualizar(pantalla, cells, 10) #Actualizamos el estado de las células.
            #         pygame.display.update()
            else: 
                r = not r #Cambiamos el valor de la variable.    
                actualizar(pantalla, cells, 10) #Actualizamos el estado de las células.
                pygame.display.update()

            # if pygame.mouse.get_pressed()[0]: #Si se pulsa el ratón, se cambia el estado de la célula.
            #     pos = pygame.mouse.get_pos()
            #     cells[pos[1]//10, pos[0]//10] = 1
            #     #pygame.draw.rect(pantalla, vida, (x//10*10, y//10*10, 10 - 1, 10 - 1))
            #     actualizar(pantalla, cells, 10)
            #     pygame.display.update()


        pantalla.fill(grid) #Dibujamos la cuadrícula.
        if r: #Si se está mostrando el progreso, se actualiza el estado de las células.
            cells = actualizar(pantalla, cells, 10, progreso = True)
            pygame.display.update()
        
        time.sleep(0.1)

if __name__ == "__main__":
    main()
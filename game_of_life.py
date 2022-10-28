import time 
import pygame
import numpy as np

fondo = (50, 50, 50)
grid = (30, 30, 30)
muerte = (100, 100, 100)
vida = (150, 150, 150)

#Función para actualizar el estado de la matriz de células.
def actualizar(pantalla, celda, tamano, progreso=False):
    celda_actualizada = np.empty((celda.shape[0], celda.shape[1]))
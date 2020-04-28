import pygame
import numpy as np


def crear_ventana(ancho, alto, fondo):
    # Creando la pantalla con pygame
    ventana = pygame.display.set_mode((alto, ancho))
    # Aplicando un color de fondo
    ventana.fill(fondo)
    return ventana


def main():
    alto, ancho = 1000, 1000
    # 
    celdas_x, celdas_y = 25, 25
    grosos_linea = 1
    fondo = (25, 25, 25)
    ventana = crear_ventana(alto, ancho, fondo)
    alto_celda = alto / celdas_x
    ancho_celda = ancho / celdas_y
    while True:
        for x in range(celdas_x):
            for y in range(celdas_y):
                poligono = [(x * ancho_celda, y * alto_celda),
                            ((x+1) * ancho_celda, y * alto_celda),
                            ((x+1) * ancho_celda, (y+1) * alto_celda),
                            (x * ancho_celda, (y+1) * alto_celda)
                            ]
                pygame.draw.polygon(ventana, (128, 128, 128), poligono,
                                    grosos_linea)
        pygame.display.flip()


if __name__ == '__main__':
    main()

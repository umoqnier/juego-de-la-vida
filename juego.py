import pygame
import numpy as np
import time

def crear_ventana(ancho, alto, fondo):
    # Creando la pantalla con pygame
    ventana = pygame.display.set_mode((alto, ancho))
    # Aplicando un color de fondo
    ventana.fill(fondo)
    return ventana


def calcula_vecinos(estado, x, y, celdas_x, celdas_y):
    return estado[(x-1) % celdas_x, (y-1) % celdas_y] + \
            estado[x % celdas_x, (y-1) % celdas_y] + \
            estado[(x+1) % celdas_x, (y-1) % celdas_y] + \
            estado[(x-1) % celdas_x, y % celdas_y] + \
            estado[(x+1) % celdas_x, y % celdas_y] + \
            estado[(x-1) % celdas_x, (y+1) % celdas_y] + \
            estado[x % celdas_x, (y+1) % celdas_y] + \
            estado[(x+1) % celdas_x, (y+1) % celdas_y]




def main():
    pygame.init()
    alto, ancho = 1000, 1000
    # Número de celdas en el eje X y Y
    celdas_x, celdas_y = 25, 25
    grosos_linea = 1
    fondo = (25, 25, 25)
    ventana = crear_ventana(alto, ancho, fondo)
    # Tamaño de la celda
    alto_celda = alto / celdas_x
    ancho_celda = ancho / celdas_y
    # Estado de las celdas. 1 = Vivo || 0 = Muerto
    estado = np.zeros((celdas_x, celdas_y))

    estado[5, 3] = 1
    estado[5, 4] = 1
    estado[5, 5] = 1

    estado[21, 21] = 1
    estado[22, 22] = 1
    estado[22, 23] = 1
    estado[21, 23] = 1
    estado[20, 23] = 1
    while True:
        neoestado = np.copy(estado)
        ventana.fill(fondo)
        time.sleep(0.05)
        for x in range(celdas_x):
            for y in range(celdas_y):

                numero_vecinos = calcula_vecinos(estado, x, y, celdas_x,
                                                 celdas_y)
                # Reglas del juego de la vida
                # 1. Una celula con exactamente 3 vecinos revive en la
                # siguiente generación
                if estado[x, y] == 0 and numero_vecinos == 3:
                    neoestado[x, y] = 1
                # 2. Una celula viva con menos de dos vecinos o más de
                # tres muere baja población o sobrepoblación
                elif estado[x, y] == 1 and (numero_vecinos < 2 or numero_vecinos > 3):
                    neoestado[x, y] = 0
                poligono = [(x * ancho_celda, y * alto_celda),
                            ((x+1) * ancho_celda, y * alto_celda),
                            ((x+1) * ancho_celda, (y+1) * alto_celda),
                            (x * ancho_celda, (y+1) * alto_celda)
                            ]
                if neoestado[x, y] == 0:
                    pygame.draw.polygon(ventana, (128, 128, 128), poligono,
                                        grosos_linea)
                else:
                    pygame.draw.polygon(ventana, (255, 255, 255), poligono,
                                        0)
        estado = np.copy(neoestado)
        pygame.display.flip()


if __name__ == '__main__':
    main()

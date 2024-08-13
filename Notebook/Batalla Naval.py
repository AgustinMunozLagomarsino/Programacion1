import math  # Importa funciones matemáticas como sqrt (raíz cuadrada) y pow (potencia)
import numpy as np  # Importa numpy para manejar matrices
import pygame  # Importa pygame para crear la interfaz gráfica

# Inicializar pygame
pygame.init()

# Configuración de la pantalla
screen_size_x = 550  # Ancho de la pantalla en píxeles
screen_size_y = 250  # Alto de la pantalla en píxeles

# Cantidad de cuadrados en la cuadrícula (en este caso 5x5)
grid_size = 5

# Se calcula y determina el tamaño de las celdas
cell_size = (screen_size_x - 50) // (grid_size * 2)

# Crear la pantalla con la resolución especificada
screen = pygame.display.set_mode((screen_size_x, screen_size_y)) 

# Definir colores
WHITE = (255, 255, 255)  # Blanco
BLACK = (0, 0, 0)  # Negro
RED = (255, 0, 0)  # Rojo
BLUE = (0, 0, 255)  # Azul
GREEN = (0, 255, 0)  # Verde

# Crear dos tableros con matrices de ceros
tableros = [np.zeros((grid_size, grid_size)) for _ in range(2)]

# Contar barcos restantes para cada jugador
barcos_restantes = [3, 3]  # Supongamos que cada jugador tiene 3 barcos

# Función para dibujar la cuadrícula del primer tablero
def draw_grid_tablero1():
    for x in range(0, (cell_size * grid_size), cell_size):
        for y in range(0, screen_size_y, cell_size):
            rect = pygame.Rect(x, y, cell_size, cell_size)
            pygame.draw.rect(screen, GREEN, rect, 1)

# Función para dibujar la cuadrícula del segundo tablero
def draw_grid_tablero2():
    for x in range(300, screen_size_x, cell_size):
        for y in range(0, screen_size_y, cell_size):
            rect = pygame.Rect(x, y, cell_size, cell_size)
            pygame.draw.rect(screen, GREEN, rect, 1)

# Función para dibujar los disparos en el tablero
def draw_shots(tablero):
    for x in range(grid_size):
        for y in range(grid_size):
            if tableros[tablero][x, y] == 2:  # Disparo fallido
                center_x = (x * cell_size + cell_size // 2) + 300 * tablero
                center_y = (y * cell_size + cell_size // 2)
                half_diag = cell_size * math.sqrt(2) // 4
                pygame.draw.line(screen, RED, 
                                 (center_x - half_diag, center_y - half_diag), 
                                 (center_x + half_diag, center_y + half_diag), 
                                 5)
                pygame.draw.line(screen, RED, 
                                 (center_x - half_diag, center_y + half_diag), 
                                 (center_x + half_diag, center_y - half_diag), 
                                 5)
            elif tableros[tablero][x, y] == 4:  # Disparo acertado
                pygame.draw.circle(screen, BLUE, ((x * cell_size + cell_size // 2) + 300 * tablero, y * cell_size + cell_size // 2), cell_size // 3)

# Función para procesar el clic del ratón
def handle_click(pos, tablero):
    x, y = pos
    if tablero == 0:
        if 0 <= x < 250 and 0 <= y < 250:  # Dentro del primer tablero
            grid_x = x // cell_size
            grid_y = y // cell_size
        else:
            return  # Clic fuera del primer tablero
    else:
        if 300 <= x < 550 and 0 <= y < 250:  # Dentro del segundo tablero
            grid_x = (x - 300) // cell_size
            grid_y = y // cell_size
        else:
            return  # Clic fuera del segundo tablero

    if 0 <= grid_x < grid_size and 0 <= grid_y < grid_size:
        if tableros[tablero][grid_x, grid_y] == 0:
            tableros[tablero][grid_x, grid_y] = 2  # Marca disparo fallido
        elif tableros[tablero][grid_x, grid_y] == 1:  # Si hay un barco
            tableros[tablero][grid_x, grid_y] = 4  # Marca disparo acertado
            barcos_restantes[tablero] -= 1  # Disminuir el conteo de barcos restantes

# Función para verificar si hay un ganador
def check_winner():
    if barcos_restantes[0] == 0:
        return 1  # Jugador 2 gana
    elif barcos_restantes[1] == 0:
        return 0  # Jugador 1 gana
    return -1  # Aún no hay ganador

# Bucle principal del juego
running = True
tablero = 0
while running:
    screen.fill(WHITE)  # Limpiar la pantalla en cada iteración
    draw_grid_tablero1()
    draw_grid_tablero2()
    draw_shots(0)
    draw_shots(1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN: 
            handle_click(event.pos, tablero)
            ganador = check_winner()
            if ganador != -1:
                print(f"Jugador {ganador + 1} ha ganado!")
                running = False  # Terminar el juego
            else:
                tablero = 1 if tablero == 0 else 0  # Cambiar de tablero
                print(f"Turno de tablero {tablero + 1}")

    pygame.display.flip()

pygame.quit()

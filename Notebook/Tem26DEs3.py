import random

# Número de autos en la carrera
num_autos = 5

# Inicializar las velocidades aleatorias de cada auto
velocidades = [random.randint(1, 10) for _ in range(num_autos)]

# Inicializar las distancias recorridas por cada auto
distancias = [0] * num_autos

# Duración de la carrera en segundos
duracion_carrera = 10

# Simulación de la carrera
for segundo in range(duracion_carrera):
    for i in range(num_autos):
        distancias[i] += velocidades[i]

# Determinar la distancia máxima alcanzada
distancia_maxima = max(distancias)

# Encontrar los autos que alcanzaron la distancia máxima
ganadores = [i + 1 for i, distancia in enumerate(distancias) if distancia == distancia_maxima]

# Imprimir los resultados de la carrera
print("Resultados de la carrera:")
for i in range(num_autos):
    print(f"Auto {i + 1}: {distancias[i]} metros")

# Imprimir el/los ganador(es)
if len(ganadores) > 1:
    print(f"Hay un empate entre los autos: {', '.join(map(str, ganadores))}")
else:
    print(f"El auto ganador es: {ganadores[0]}")
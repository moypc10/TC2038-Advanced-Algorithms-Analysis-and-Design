import matplotlib.pyplot as plt
import numpy as np

def distancia(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def busca_pareja(punto, puntos_disponibles):
    pareja = None
    distancia_minima = float('inf')
    for otro_punto in puntos_disponibles:
        if punto != otro_punto:
            d = distancia(punto, otro_punto)
            if d < distancia_minima:
                distancia_minima = d
                pareja = otro_punto
    return pareja, distancia_minima

def algoritmo_voraz(puntos):
    conectados = []
    puntos_disponibles = set(tuple(p) for p in puntos)

    punto_actual = tuple(puntos[0])
    puntos_disponibles.remove(punto_actual)

    distancia_total = 0

    while puntos_disponibles:
        pareja, distancia_minima = busca_pareja(punto_actual, puntos_disponibles)
        conectados.append((punto_actual, pareja))
        puntos_disponibles.remove(pareja)
        punto_actual = pareja
        distancia_total += distancia_minima

    # Conectar el último punto con el primero para cerrar la figura
    conectados.append((punto_actual, tuple(puntos[0])))
    distancia_total += distancia(punto_actual, puntos[0])

    return conectados, distancia_total

# Generar 32 puntos aleatorios
np.random.seed(45)
puntos = np.random.rand(32, 2)

# Aplicar el algoritmo voraz
conexiones, distancia_total = algoritmo_voraz(puntos)

# Imprimir la distancia total
print(f"Distancia total de la figura: {distancia_total}")

# Graficar los puntos y las conexiones
fig, ax = plt.subplots()
ax.scatter(puntos[:, 0], puntos[:, 1], c='red', marker='o')

for conexion in conexiones:
    x_values = [conexion[0][0], conexion[1][0]]
    y_values = [conexion[0][1], conexion[1][1]]
    ax.plot(x_values, y_values, c='blue')

plt.title('Conexiones Óptimas (Figura Cerrada)')
plt.show()

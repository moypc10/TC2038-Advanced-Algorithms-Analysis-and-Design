import numpy as np
import matplotlib.pyplot as plt

# Función para calcular la longitud total de las líneas
def calcular_longitud_total(puntos, conexiones):
    longitud_total = 0
    for conexion in conexiones:
        longitud_total += np.linalg.norm(puntos[conexion[0]] - puntos[conexion[1]])
    return longitud_total

# Función para generar una solución vecina intercambiando dos conexiones
def generar_vecino(conexiones):
    vecino = conexiones.copy()
    i, j = np.random.choice(len(vecino), 2, replace=False)
    vecino[i], vecino[j] = vecino[j], vecino[i]
    return vecino

# Función de probabilidad para aceptar soluciones peores
def probabilidad_aceptacion(delta, temperatura):
    return np.exp(-delta / temperatura)

# Algoritmo de recocido simulado
def recocido_simulado(puntos, temperatura_inicial=1000, factor_enfriamiento=0.95, iteraciones_por_temp=100):
    n = len(puntos)
    mejor_conexion = [(i, (i + 1) % n) for i in range(n)]
    mejor_longitud = calcular_longitud_total(puntos, mejor_conexion)

    temperatura = temperatura_inicial
    for _ in range(iteraciones_por_temp):
        vecino = generar_vecino(mejor_conexion)
        delta = calcular_longitud_total(puntos, vecino) - mejor_longitud

        if delta < 0 or np.random.rand() < probabilidad_aceptacion(delta, temperatura):
            mejor_conexion = vecino
            mejor_longitud = calcular_longitud_total(puntos, mejor_conexion)

        temperatura *= factor_enfriamiento

    return mejor_conexion, mejor_longitud

# Generar puntos aleatorios
np.random.seed(45)
puntos = np.random.rand(32, 2)

# Ejecutar el algoritmo de recocido simulado
conexiones_optimas, longitud_optima = recocido_simulado(puntos)

# Visualizar la solución
plt.scatter(puntos[:, 0], puntos[:, 1], c='red', marker='o')
for conexion in conexiones_optimas:
    plt.plot([puntos[conexion[0]][0], puntos[conexion[1]][0]], [puntos[conexion[0]][1], puntos[conexion[1]][1]], c='blue')

plt.title(f'Conexiones Óptimas - Longitud Total: {longitud_optima:.4f}')
plt.show()
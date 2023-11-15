# Importar matplotlib.pyplot y numpy
import matplotlib.pyplot as plt
import numpy as np

# Definir los puntos
puntos = [
    [(5,2), (3,2)],
    [(-2,3), (1,2)],
    [(-2,-2), (3,4)],
    [(10,1), (2,5)],
    [(3,4), (5,8)],
    [(-7,3), (3,5)],
    [(14,4), (-14,4)],
    [(8,7), (3,3)],
    [(-1,-1), (2,5)],
    [(5,4), (-3,1)]
]

# Graficar cada linea
for linea in puntos:
    # Extraer las coordenadas x e y de cada punto
    x = [p[0] for p in linea]
    y = [p[1] for p in linea]
    # Graficar la linea con un marcador circular
    plt.plot (x, y, marker='o')

# Crear una lista vacía para guardar las intersecciones
intersecciones = []

# Comparar cada par de líneas
for i in range (len (puntos)):
    for j in range (i+1, len (puntos)):
        # Obtener las coordenadas x e y de cada línea
        x1 = [p[0] for p in puntos [i]]
        y1 = [p[1] for p in puntos [i]]
        x2 = [p[0] for p in puntos [j]]
        y2 = [p[1] for p in puntos [j]]
        # Calcular la pendiente y el intercepto de cada línea
        m1 = (y1 [1] - y1 [0]) / (x1 [1] - x1 [0])
        b1 = y1 [0] - m1 * x1 [0]
        m2 = (y2 [1] - y2 [0]) / (x2 [1] - x2 [0])
        b2 = y2 [0] - m2 * x2 [0]
        # Crear un arreglo con los valores de x en el rango común de las líneas
        x = np.linspace (max (min (x1), min (x2)), min (max (x1), max (x2)), 100)
        # Calcular los valores de y correspondientes para cada línea
        y1 = m1 * x + b1
        y2 = m2 * x + b2
        # Encontrar los índices donde los valores de y son cercanos
        idx = np.argwhere (np.isclose (y1, y2, atol=0.1)).flatten ()
        # Si hay algún índice, agregar la coordenada de la intersección a la lista
        if idx.size > 0:
            intersecciones.append ((x [idx [0]], y1 [idx [0]]))

# Graficar las intersecciones con un marcador de estrella
for inter in intersecciones:
    plt.plot (inter [0], inter [1], marker='*')
    
for inter in intersecciones:
    x, y = inter
    angle_rad = np.arctan2(y, x)
    angle_deg = np.degrees(angle_rad)
    print(f"Interseccion en ({x}, {y}): Angulo = {angle_deg} Grados")

# Mostrar el gráfico
plt.show ()


import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d

# Definir los puntos
points = np.array([(-5,-5), (-5,5), (5,5), (5,-5), (0,0)])

# Calcular el diagrama de Voronoi
vor = Voronoi(points)

# Graficar el diagrama de Voronoi
voronoi_plot_2d(vor)

# Graficar los puntos originales
plt.plot(points[:, 0], points[:, 1], 'o')

# Añadir etiquetas
for i, point in enumerate(points):
    plt.text(point[0], point[1], f'P{i+1}', ha='right')

# Mostrar la gráfica
plt.show()

import matplotlib.pyplot as plt

# Coordenadas de los puntos
coordenadas = [(-19, -17), (-15, 3), (-12, 11), (-8, -5), (-7, 14), (-3, -9), (-1, 0), (2, 18), (4, -13), (6, 7),
               (9, -16), (11, 5), (13, -2), (16, 12), (18, -7), (-20, 6), (-14, -18), (-9, 9), (-4, -12), (-2, 15),
               (1, -14), (3, 10), (7, -8), (12, 19), (17, -4)]

# Desempaquetar las coordenadas en listas separadas de x e y
x, y = zip(*coordenadas)

# Crear el gráfico de dispersión
plt.scatter(x, y)

# Etiquetas y título
plt.xlabel('Coordenada X')
plt.ylabel('Coordenada Y')
plt.title('Gráfico de dispersión de puntos')

# Mostrar el gráfico
plt.show()

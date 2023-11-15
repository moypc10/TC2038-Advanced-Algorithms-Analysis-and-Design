import random
import matplotlib.pyplot as plt

class Node:
    def __init__(self, point, left=None, right=None):
        self.point = point
        self.left = left
        self.right = right

def build_kd_tree(points, depth=0):
    if len(points) == 0:
        return None

    k = len(points[0])
    axis = depth % k
    points.sort(key=lambda x: x[axis])

    median = len(points) // 2
    node = Node(points[median])
    node.left = build_kd_tree(points[:median], depth + 1)
    node.right = build_kd_tree(points[median + 1:], depth + 1)

    return node

def distance(point1, point2):
    return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2) ** 0.5

def points_in_range(root, target_range, depth=0, points=[]):
    if root is None:
        return points

    k = 2  # 2-dimensional space
    axis = depth % k

    if target_range[0] <= root.point[0] <= target_range[1] and target_range[2] <= root.point[1] <= target_range[3]:
        points.append(root.point)

    if axis == 0:
        if target_range[0] <= root.point[0]:
            points = points_in_range(root.left, target_range, depth + 1, points)
        if target_range[1] >= root.point[0]:
            points = points_in_range(root.right, target_range, depth + 1, points)
    else:
        if target_range[2] <= root.point[1]:
            points = points_in_range(root.left, target_range, depth + 1, points)
        if target_range[3] >= root.point[1]:
            points = points_in_range(root.right, target_range, depth + 1, points)

    return points

# Generar 200 puntos aleatorios
random.seed(42)
points = [(random.uniform(-10, 10), random.uniform(-10, 10)) for _ in range(200)]

# Construir el árbol K-d
tree = build_kd_tree(points)

# Definir el rango en x y y
x_range = (-7, 5)
y_range = (-3, 1)

# Encontrar los puntos dentro del rango
points_in_range_list = points_in_range(tree, x_range + y_range)

# Extraer las coordenadas x e y de los puntos
x_values = [point[0] for point in points]
y_values = [point[1] for point in points]

# Extraer las coordenadas x e y de los puntos dentro del rango
x_values_in_range = [point[0] for point in points_in_range_list]
y_values_in_range = [point[1] for point in points_in_range_list]

# Crear el gráfico
plt.scatter(x_values, y_values, label='Puntos Aleatorios', s=10)
plt.scatter(x_values_in_range, y_values_in_range, color='green', label='Puntos en Rango', s=10)
plt.axvline(x_range[0], color='red', linestyle='--', label='Límite en X')
plt.axvline(x_range[1], color='red', linestyle='--')
plt.axhline(y_range[0], color='blue', linestyle='--', label='Límite en Y')
plt.axhline(y_range[1], color='blue', linestyle='--')
plt.legend()
plt.xlabel('Coordenada X')
plt.ylabel('Coordenada Y')
plt.title('Árbol K-d y Puntos en Rango')
plt.grid(True)
plt.show()

print(f"Puntos en el rango ({x_range[0]}, {x_range[1]}, {y_range[0]}, {y_range[1]}): {len(points_in_range_list)} puntos")
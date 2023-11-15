#Actividad: Implementación de "Tries" y recorridos en grafos

# Importaciones de módulos
from queue import Queue
from queue import LifoQueue
from queue import PriorityQueue

# Clase WeightedGraph
class WeightedGraph:
    def __init__(self, directed: bool = False):
        """
        Constructor que inicializa un grafo vacío.
        :param directed: Un indicador que indica si el grafo es dirigido (True) o no dirigido (False).
        """
        self._directed = directed
        self._adjacency_list = {}

    def clear(self):
        """
        Este método borra el grafo.
        """
        self._adjacency_list = {}

    def number_of_vertices(self):
        """
        Este método devuelve el número de vértices del grafo.
        """
        return len(self._adjacency_list)

    def vertices(self):
        """
        Este método devuelve la lista de vértices.
        """
        return list(self._adjacency_list.keys())

    def edges(self):
        """
        Este método devuelve la lista de aristas.
        """
        edge_list = []

        for v in self._adjacency_list:
            for edge in self._adjacency_list[v]:
                if self._directed or (edge[0], v, edge[1]) not in edge_list:
                    edge_list.append((v, edge[0], edge[1]))

        return edge_list

    def add_vertex(self, v):
        """
        Agrega un vértice al grafo.
        :param v: El nuevo vértice que se agregará al grafo.
        """
        if v not in self._adjacency_list:
            self._adjacency_list[v] = []

    def remove_vertex(self, v):
        """
        Elimina un vértice del grafo.
        :param v: El vértice que se eliminará del grafo.
        """
        if v in self._adjacency_list:
            del self._adjacency_list[v]

            for vertex in self._adjacency_list:
                self._adjacency_list[vertex] = [edge for edge in self._adjacency_list[vertex] if edge[0] != v]

    def add_edge(self, v1, v2, e=0):
        """
        Agrega una arista al grafo. La arista está definida por dos vértices v1 y v2, y el peso e de la arista.
        :param v1: El vértice de inicio de la nueva arista.
        :param v2: El vértice final de la nueva arista.
        :param e: El peso de la nueva arista.
        """
        if v1 not in self._adjacency_list:
            print("Advertencia: El vértice", v1, "no existe.")
        elif v2 not in self._adjacency_list:
            print("Advertencia: El vértice", v2, "no existe.")
        elif not self._directed and v1 == v2:
            print("Advertencia: Un grafo no dirigido no puede tener autociclos.")
        elif (v2, e) in self._adjacency_list[v1]:
            print("Advertencia: La arista (", v1, ",", v2, ",", e, ") ya existe.")
        else:
            self._adjacency_list[v1].append((v2, e))

            if not self._directed:
                self._adjacency_list[v2].append((v1, e))

    def remove_edge(self, v1, v2, e):
        """
        Elimina una arista del grafo.
        :param v1: El vértice de inicio de la arista a eliminar.
        :param v2: El vértice final de la arista a eliminar.
        :param e: El peso de la arista a eliminar.
        """
        if v1 not in self._adjacency_list:
            print("Advertencia: El vértice", v1, "no existe.")
        elif v2 not in self._adjacency_list:
            print("Advertencia: El vértice", v2, "no existe.")
        else:
            self._adjacency_list[v1] = [(vertex, weight) for vertex, weight in self._adjacency_list[v1] if vertex != v2]

            if not self._directed:
                self._adjacency_list[v2] = [(vertex, weight) for vertex, weight in self._adjacency_list[v2] if vertex != v1]

    def adjacent_vertices(self, v):
        """
        Devuelve una lista de vértices adyacentes a un vértice dado.
        :param v: El vértice cuyos vértices adyacentes se devolverán.
        :return: La lista de vértices adyacentes a v.
        """
        if v not in self._adjacency_list:
            print("Advertencia: El vértice", v, "no existe.")
            return []
        return self._adjacency_list[v]

    def is_adjacent(self, v1, v2) -> bool:
        """
        Este método indica si el vértice v2 es adyacente al vértice v1.
        :param v1: El vértice de inicio de la relación a probar.
        :param v2: El vértice final de la relación a probar.
        :return: True si v2 es adyacente a v1, False en caso contrario.
        """
        if v1 not in self._adjacency_list:
            print("Advertencia: El vértice", v1, "no existe.")
            return False
        elif v2 not in self._adjacency_list:
            print("Advertencia: El vértice", v2, "no existe.")
            return False
        for edge in self._adjacency_list[v1]:
            if edge[0] == v2:
                return True
        return False

    def print_graph(self):
        """
        Este método muestra las aristas del grafo.
        """
        for vertex in self._adjacency_list:
            for edges in self._adjacency_list[vertex]:
                print(vertex, " -> ", edges[0], " peso de la arista: ", edges[1])

# Clase TreeNode
class TreeNode:
    def __init__(self, parent, v, c):
        """
        Constructor que inicializa un nodo.
        :param parent: El nodo padre.
        :param v: El vértice del grafo que representa el nodo.
        :param c: El costo del camino al nodo desde la raíz.
        """
        self.parent = parent
        self.v = v
        self.c = c

    def path(self):
        """
        Este método construye una lista con los vértices del camino desde la raíz hasta el nodo.
        :return: El camino desde la raíz hasta el nodo.
        """
        node = self
        path = []
        while node is not None:
            path.insert(0, node.v)
            node = node.parent
        return path
    
    def __lt__(self, other):
        return self.c < other.c

# Algoritmo de búsqueda en anchura (Breadth-First Search - BFS)
def bfs(graph: WeightedGraph, v0, vg):
    # Comprobar el grafo y los vértices
    if v0 not in graph.vertices():
        print("Advertencia: El vértice", v0, "no está en el Grafo")
    if vg not in graph.vertices():
        print("Advertencia: El vértice", vg, "no está en el Grafo")

    # Inicializar la frontera
    frontier = Queue()
    frontier.put(TreeNode(None, v0, 0))

    # Inicializar el conjunto explorado
    explored_set = {}

    while True:
        if frontier.empty():
            return None

        # Obtener el nodo de la frontera
        node = frontier.get()

        # Probar el nodo
        if node.v == vg:
            # Devolver el camino y el costo como un diccionario
            return {"Recorrido": node.path(), "Costo": node.c}

        # Expandir el nodo
        if node.v not in explored_set:
            adjacent_vertices = graph.adjacent_vertices(node.v)
            for vertex in adjacent_vertices:
                frontier.put(TreeNode(node, vertex[0], vertex[1] + node.c))

        # Agregar el nodo al conjunto explorado
        explored_set[node.v] = 0

# Algoritmo de búsqueda en profundidad (Depth-First Search - DFS)
def dfs(graph: WeightedGraph, v0, vg):
    # Comprobar el grafo y los vértices
    if v0 not in graph.vertices():
        print("Advertencia: El vértice", v0, "no está en el Grafo")
    if vg not in graph.vertices():
        print("Advertencia: El vértice", vg, "no está en el Grafo")

    # Inicializar la frontera
    frontier = LifoQueue()
    frontier.put(TreeNode(None, v0, 0))

    # Inicializar el conjunto explorado
    explored_set = {}

    while True:
        if frontier.empty():
            return None

        # Obtener el nodo de la frontera
        node = frontier.get()

        # Probar el nodo
        if node.v == vg:
            # Devolver el camino y el costo como un diccionario
            return {"Recorrido": node.path(), "Costo": node.c}

        # Expandir el nodo
        if node.v not in explored_set:
            adjacent_vertices = graph.adjacent_vertices(node.v)
            for vertex in adjacent_vertices:
                frontier.put(TreeNode(node, vertex[0], vertex[1] + node.c))

        # Agregar el nodo al conjunto explorado
        explored_set[node.v] = 0

# Algoritmo de búsqueda de costo uniforme
def uniform_cost(graph: WeightedGraph, v0, vg):
    # Comprobar el grafo y los vértices
    if v0 not in graph.vertices():
        print("Advertencia: El vértice", v0, "no está en el Grafo")
    if vg not in graph.vertices():
        print("Advertencia: El vértice", vg, "no está en el Grafo")

    # Inicializar la frontera
    frontier = PriorityQueue()
    frontier.put((0, TreeNode(None, v0, 0)))  # Usar (costo, nodo)

    # Inicializar el conjunto explorado
    explored_set = {}

    while True:
        if frontier.empty():
            return None

        # Obtener el nodo de la frontera
        node = frontier.get()[1]  # Obtener el segundo elemento de la tupla

        # Probar el nodo
        if node.v == vg:
            # Devolver el camino y el costo como un diccionario
            return {"Recorrido:": node.path(), "Costo": node.c}

        # Expandir el nodo
        if node.v not in explored_set:
            adjacent_vertices = graph.adjacent_vertices(node.v)
            for vertex in adjacent_vertices:
                cost = vertex[1] + node.c
                frontier.put((cost, TreeNode(node, vertex[0], cost)))  # Usar (costo, nodo)

        # Agregar el nodo al conjunto explorado
        explored_set[node.v] = 0

# Prueba del algoritmo de búsqueda de caminos
if __name__ == "__main__":
    # Crear el grafo
    gr = WeightedGraph(directed=False)
    gr.add_vertex('Goding')
    gr.add_vertex('Ylane')
    gr.add_vertex('Ontdale')
    gr.add_vertex('Togend')
    gr.add_vertex('Blebus')
    gr.add_vertex('Oriaron')
    gr.add_vertex('Strento')
    gr.add_vertex('Zrusall')
    gr.add_vertex('Goxmont')
    gr.add_vertex('Adaset')
    gr.add_vertex('Niaphia')
    gr.add_vertex('Ertonwell')
    gr.add_vertex('Lagos')
    gr.add_vertex('Duron')
    
    gr.add_edge('Adaset', 'Ertonwell', 130)
    gr.add_edge('Adaset', 'Goxmont', 103)
    gr.add_edge('Adaset', 'Zrusall', 15)
    gr.add_edge('Blebus', 'Duron', 160)
    gr.add_edge('Blebus', 'Ontdale', 165)
    gr.add_edge('Duron', 'Lagos', 119)
    gr.add_edge('Ertonwell', 'Niaphia', 56)
    gr.add_edge('Goding', 'Ylane', 88)
    gr.add_edge('Goding', 'Ontdale', 98)
    gr.add_edge('Goxmont', 'Niaphia', 212)
    gr.add_edge('Lagos', 'Niaphia', 300)
    gr.add_edge('Oriaron', 'Ontdale', 219)
    gr.add_edge('Oriaron', 'Blebus', 291)
    gr.add_edge('Oriaron', 'Strento', 221)
    gr.add_edge('Strento', 'Zrusall', 121)
    gr.add_edge('Togend', 'Blebus', 121)
    gr.add_edge('Togend', 'Ontdale', 210)
    gr.add_edge('Ylane', 'Strento', 99)
    gr.add_edge('Zrusall', 'Goxmont', 112)

    print("Busqueda en Anchura (BFS):")
    res_bfs = bfs(gr, 'Ylane', 'Ertonwell')
    print(res_bfs)

    print("\nBusqueda en Profundidad (DFS):")
    res_dfs = dfs(gr, 'Ylane', 'Ertonwell')
    print(res_dfs)

    print("\nBusqueda de Costo Uniforme:")
    res_uniform_cost = uniform_cost(gr, 'Ylane', 'Ertonwell')
    print(res_uniform_cost)
    
    print("\nBusqueda de Costo Uniforme desde una ciudad a todas:")
    print("Ciudad Origen: Ylane")
    res_uniform_cost = uniform_cost(gr, 'Ylane', 'Goding')
    print(res_uniform_cost)
    
    res_uniform_cost = uniform_cost(gr, 'Ylane', 'Ontdale')
    print(res_uniform_cost)
    
    res_uniform_cost = uniform_cost(gr, 'Ylane', 'Togend')
    print(res_uniform_cost)
    
    res_uniform_cost = uniform_cost(gr, 'Ylane', 'Blebus')
    print(res_uniform_cost)
    
    res_uniform_cost = uniform_cost(gr, 'Ylane', 'Oriaron')
    print(res_uniform_cost)
    
    res_uniform_cost = uniform_cost(gr, 'Ylane', 'Strento')
    print(res_uniform_cost)
    
    res_uniform_cost = uniform_cost(gr, 'Ylane', 'Zrusall')
    print(res_uniform_cost)
    
    res_uniform_cost = uniform_cost(gr, 'Ylane', 'Goxmont')
    print(res_uniform_cost)
    
    res_uniform_cost = uniform_cost(gr, 'Ylane', 'Adaset')
    print(res_uniform_cost)
    
    res_uniform_cost = uniform_cost(gr, 'Ylane', 'Niaphia')
    print(res_uniform_cost)
    
    res_uniform_cost = uniform_cost(gr, 'Ylane', 'Ertonwell')
    print(res_uniform_cost)
    
    res_uniform_cost = uniform_cost(gr, 'Ylane', 'Lagos')
    print(res_uniform_cost)
    
    res_uniform_cost = uniform_cost(gr, 'Ylane', 'Duron')
    print(res_uniform_cost)
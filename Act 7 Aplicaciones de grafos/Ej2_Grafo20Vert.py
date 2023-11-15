from queue import PriorityQueue
import copy

class WeightedGraph:
    """
    Clase que representa un grafo ponderado. Internamente, la clase
    utiliza una lista de adyacencia para almacenar los vértices y aristas del grafo.
    El grafo puede ser dirigido o no dirigido, lo que se establece en el constructor de la clase.
    Algunas operaciones dependen de esta propiedad.

    Se asume que es posible tener múltiples conexiones entre vértices.
    """

    _directed = True  # Esta bandera indica si el grafo es dirigido o no dirigido.
    _adjacency_list = {}  # Lista de adyacencia del grafo.

    def __init__(self, directed: bool = False):
        """
        Este constructor inicializa un grafo vacío.
        :param directed: Una bandera que indica si el grafo es dirigido (True) o no dirigido (False).
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
        v = []
        for vi in self._adjacency_list:
            v.append(vi)
        return v

    def edges(self):
        """
        Este método devuelve la lista de aristas.
        """
        e = []
        if self._directed:
            for v in self._adjacency_list:
                for edge in self._adjacency_list[v]:
                    e.append((v, edge[0], edge[1]))
        else:
            for v in self._adjacency_list:
                for edge in self._adjacency_list[v]:
                    if (edge[0], v, edge[1]) not in e:
                        e.append((v, edge[0], edge[1]))
        return e

    def add_vertex(self, v):
        """
        Agregar un vértice al grafo.
        :param v: El nuevo vértice que se agregará al grafo.
        """
        if v in self._adjacency_list:
            print("Advertencia: El vértice", v, "ya existe.")
        else:
            self._adjacency_list[v] = []

    def remove_vertex(self, v):
        """
        Eliminar un vértice del grafo.
        :param v: El vértice que se eliminará del grafo.
        """
        if v not in self._adjacency_list:
            print("Advertencia: El vértice", v, "no está en el grafo.")
        else:
            # Eliminar el vértice de la lista de adyacencia.
            self._adjacency_list.remove(v)
            # Eliminar aristas donde el vértice es un punto final.
            for vertex in self._adjacency_list:
                for edge in self._adjacency_list[vertex]:
                    if edge[0] == v:
                        self._adjacency_list[vertex].remove(edge)

    def add_edge(self, v1, v2, e=0):
        """
        Agregar una arista al grafo. La arista está definida por dos vértices v1 y v2,
        y el peso e de la arista.
        :param v1: El vértice de inicio de la nueva arista.
        :param v2: El vértice final de la nueva arista.
        :param e: El peso de la nueva arista.
        """
        if v1 not in self._adjacency_list:
            # El vértice de inicio no existe.
            print("Advertencia: El vértice", v1, "no existe.")
        elif v2 not in self._adjacency_list:
            # El vértice final no existe.
            print("Advertencia: El vértice", v2, "no existe.")
        elif not self._directed and v1 == v2:
            # El grafo es no dirigido, por lo que no está permitido tener autociclos.
            print("Advertencia: Un grafo no dirigido no puede tener autociclos.")
        elif (v2, e) in self._adjacency_list[v1]:
            # La arista ya está en el grafo.
            print("Advertencia: La arista (", v1, ",", v2, ",", e, ") ya existe.")
        else:
            self._adjacency_list[v1].append((v2, e))
            if not self._directed:
                self._adjacency_list[v2].append((v1, e))

    def remove_edge(self, v1, v2, e):
        """
        Eliminar una arista del grafo.
        :param v1: El vértice de inicio de la arista que se eliminará.
        :param v2: El vértice final de la arista que se eliminará.
        :param e: El peso de la arista que se eliminará.
        """
        if v1 not in self._adjacency_list:
            # v1 no es un vértice del grafo.
            print("Advertencia: El vértice", v1, "no existe.")
        elif v2 not in self._adjacency_list:
            # v2 no es un vértice del grafo.
            print("Advertencia: El vértice", v2, "no existe.")
        else:
            for edge in self._adjacency_list[v1]:
                if edge == (v2, e):
                    self._adjacency_list[v1].remove(edge)
            if not self._directed:
                for edge in self._adjacency_list[v2]:
                    if edge == (v1, e):
                        self._adjacency_list[v2].remove(edge)

    def adjacent_vertices(self, v):
        """
        Vértices adyacentes a un vértice.
        :param v: El vértice cuyos vértices adyacentes se devolverán.
        :return: La lista de vértices adyacentes a v.
        """
        if v not in self._adjacency_list:
            # El vértice no está en el grafo.
            print("Advertencia: El vértice", v, "no existe.")
            return []
        else:
            return self._adjacency_list[v]

    def is_adjacent(self, v1, v2) -> bool:
        """
        Este método indica si el vértice v2 es adyacente al vértice v1.
        :param v1: El vértice de inicio de la relación a probar.
        :param v2: El vértice final de la relación a probar.
        :return: True si v2 es adyacente a v1, False en caso contrario.
        """
        if v1 not in self._adjacency_list:
            # v1 no es un vértice del grafo.
            print("Advertencia: El vértice", v1, "no existe.")
            return False
        elif v2 not in self._adjacency_list:
            # v2 no es un vértice del grafo.
            print("Advertencia: El vértice", v2, "no existe.")
            return False
        else:
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

class TspUcsNode:
    """
    Clase que se utiliza para representar un nodo en el algoritmo de búsqueda de costo uniforme para
    el problema del TSP (Problema del Vendedor Viajero).
    Un nodo contiene los siguientes elementos:
    * Una referencia a su nodo padre.
    * El vértice del grafo que representa.
    * El costo total del camino desde la raíz hasta el nodo.
    * La lista de nodos explorados.
    """

    def __init__(self, parent, v, c, explored):
        """
        Este constructor inicializa un nodo.
        :param parent: El nodo padre.
        :param v: El vértice del grafo representado por el nodo.
        :param c: El costo del camino al nodo desde la raíz.
        :param explored: El camino desde la raíz hasta el nodo.
        """
        self.parent = parent
        self.v = v
        self.c = c
        self.explored = explored

    def __lt__(self, node):
        """
        Operador <. Esta definición es requerida por la clase PriorityQueue.
        """
        return False

def tsp_ucs(graph: WeightedGraph, v0):
    """
    Este método encuentra el ciclo hamiltoniano de costo mínimo de un grafo dirigido a partir de
    un vértice dado utilizando el algoritmo de búsqueda de costo uniforme.
    :param graph: El grafo a recorrer.
    :param v0: El vértice inicial.
    :return: Una tupla con el ciclo hamiltoniano de costo mínimo o None si no hay un camino.
    """
    vertices = graph.vertices()
    n = len(vertices)
    
    # Comprobar el grafo y el vértice inicial
    if v0 not in vertices:
        print("Advertencia: El vértice", v0, "no está en el grafo")

    # Inicializar la frontera
    frontier = PriorityQueue()
    frontier.put((0, TspUcsNode(None, v0, 0, [(v0, 0)])))

    # Encontrar el ciclo
    while True:
        if frontier.empty():
            return None

        # Obtener el nodo de la frontera
        node = frontier.get()[1]

        # Comprobar el nodo
        if len(node.explored) == (n + 1) and node.v == v0:
            # Devolver el camino y el costo como un diccionario
            return {"Camino": node.explored, "Costo": node.c}

        # Expandir el nodo
        adjacent_vertices = graph.adjacent_vertices(node.v)
        for vertex in adjacent_vertices:
            already_included = False

            # Comprobar si el vértice adyacente es el vértice inicial. El vértice inicial
            # solo puede incluirse al final del ciclo.
            if vertex[0] == v0 and len(node.explored) < n:
                already_included = True

            # Comprobar si el vértice ya ha sido incluido en el ciclo.
            for i in range(1, len(node.explored)):
                if vertex[0] == node.explored[i][0]:
                    already_included = True
                    break

            # Agregar el vértice si aún no está incluido en el ciclo.
            if not already_included:
                cost = vertex[1] + node.c
                frontier.put((cost, TspUcsNode(node, vertex[0], cost, node.explored + [vertex])))

class TspBBNode:
    """
    Clase que se utiliza para representar un nodo en el algoritmo de búsqueda para el problema del TSP.
    Un nodo contiene los siguientes elementos:
    * Una referencia a su nodo padre.
    * El vértice del grafo que representa.
    * El costo total del camino desde la raíz hasta el nodo.
    * El costo posible del ciclo.
    * La lista de nodos explorados.
    * La matriz de reducción.
    """

    def __init__(self, parent, v, c, cpos, explored, m):
        """
        Este constructor inicializa un nodo.
        :param parent: El nodo padre.
        :param v: El vértice del grafo representado por el nodo.
        :param c: El costo del camino al nodo desde la raíz.
        :param cpos: El costo posible del ciclo.
        :param explored: El camino desde la raíz hasta el nodo.
        :param m: La matriz de reducción del nodo.
        """
        self.parent = parent
        self.v = v
        self.c = c
        self.cpos = cpos
        self.explored = explored
        self.m = m

    def __lt__(self, node):
        """
        Operador <. Esta definición es requerida por la clase PriorityQueue.
        """
        return False
    
# Define the TSP using Branch and Bound function
def tsp_bb(graph, v0):
    # Get the list of vertices from the graph
    vertices = graph.vertices()
    n = len(vertices)

    # Check if the initial vertex is in the list of vertices
    if v0 not in vertices:
        print("Warning: Vertex", v0, "is not in the graph")
        return None

    # Create a dictionary to map vertices to indices
    vindices = {}
    for i, v in enumerate(vertices, 0):
        vindices[v] = i

    # Create an adjacency matrix with initial values set to a high value
    inf_val = 100000000
    m = [[inf_val] * n for i in range(n)]
    for edge in graph.edges():
        i = vindices[edge[0]]
        j = vindices[edge[1]]
        c = edge[2]
        m[i][j] = c
        m[j][i] = c

    # Reduce rows
    rrows = [0] * n
    for i in range(n):
        rrows[i] = min(m[i])
        if rrows[i] == inf_val:
            rrows[i] = 0
        for j in range(n):
            if m[i][j] != inf_val:
                m[i][j] -= rrows[i]

    # Reduce columns
    rcols = [0] * n
    for j in range(n):
        col = [m[i][j] for i in range(n)]
        rcols[j] = min(col)
        if rcols[j] == inf_val:
            rcols[j] = 0
        for i in range(n):
            if m[i][j] != inf_val:
                m[i][j] -= rcols[j]

    # Calculate the reduction cost
    red_cost = sum(rrows) + sum(rcols)

    # Initialize the frontier using a priority queue
    frontier = PriorityQueue()
    frontier.put((0, TspBBNode(None, v0, 0, red_cost, [(v0, 0)], m)))

    # Initialize the best solution
    best = None
    best_val = inf_val

    # Find the cycle
    while not frontier.empty():
        # Get the node from the frontier
        node = frontier.get()[1]

        # Update the best solution if a complete cycle is found
        if len(node.explored) == (n + 1) and node.v == v0:
            if node.c < best_val:
                best = node
                best_val = node.c
            continue

        # Expand the node
        adjacent_vertices = graph.adjacent_vertices(node.v)
        for vertex in adjacent_vertices:
            already_included = False

            # Check if the adjacent vertex is the initial vertex (can only be included at the end)
            if vertex[0] == v0 and len(node.explored) < n:
                already_included = True

            # Check if the vertex has already been included in the cycle
            for i in range(1, len(node.explored)):
                if vertex[0] == node.explored[i][0]:
                    already_included = True
                    break

            # Add the vertex if it is not already included in the cycle
            if not already_included:
                cost = vertex[1] + node.c
                new_explored = node.explored + [vertex]

                # Create a deep copy of the matrix for the new node
                m = copy.deepcopy(node.m)
                row = vindices[node.v]
                col = vindices[vertex[0]]

                # Fill rows and columns of vertices in the path with high values
                for k in range(n):
                    m[row][k] = inf_val
                for k in range(n):
                    m[k][col] = inf_val

                for i in range(len(new_explored)):
                    for j in range(i + 1, len(new_explored)):
                        v1 = vindices[new_explored[i][0]]
                        v2 = vindices[new_explored[j][0]]
                        m[v1][v2] = inf_val
                        m[v2][v1] = inf_val

                # Reduce rows
                rrows = [0] * n
                for i in range(n):
                    rrows[i] = min(m[i])
                    if rrows[i] == inf_val:
                        rrows[i] = 0
                    for j in range(n):
                        if m[i][j] != inf_val:
                            m[i][j] -= rrows[i]

                # Reduce columns
                rcols = [0] * n
                for j in range(n):
                    col = [m[i][j] for i in range(n)]
                    rcols[j] = min(col)
                    if rcols[j] == inf_val:
                        rcols[j] = 0
                    for i in range(n):
                        if m[i][j] != inf_val:
                            m[i][j] -= rcols[j]

                reduced_cost = sum(rrows) + sum(rcols)
                cpos = vertex[1] + node.cpos + red_cost

                # Add the new node to the frontier if its cost is promising
                if cpos < best_val:
                    frontier.put((cpos, TspBBNode(node, vertex[0], cost, cpos, new_explored, m)))

    # Return the best solution as a dictionary with the path and cost
    return {"Path": best.explored, "Cost": best.c}

# Test the algorithm with a sample graph
if __name__ == "__main__":
    # Create a sample graph
    gr = WeightedGraph(directed=False)
    gr.add_vertex('A')
    gr.add_vertex('B')
    gr.add_vertex('C')
    gr.add_vertex('D')
    gr.add_vertex('E')
    gr.add_vertex('F')
    gr.add_vertex('G')
    gr.add_vertex('H')
    gr.add_vertex('I')
    gr.add_vertex('J')
    gr.add_vertex('K')
    gr.add_vertex('L')
    gr.add_vertex('M')
    gr.add_vertex('N')
    gr.add_vertex('O')
    gr.add_vertex('P')
    gr.add_vertex('Q')
    gr.add_vertex('R')
    gr.add_vertex('S')
    gr.add_vertex('T')

    gr.add_edge('A', 'B', 5)
    gr.add_edge('A', 'C', 6)
    gr.add_edge('B', 'C', 7)
    gr.add_edge('B', 'D', 7)
    gr.add_edge('C', 'D', 8)
    gr.add_edge('C', 'E', 5)
    gr.add_edge('D', 'E', 6)
    gr.add_edge('D', 'F', 8)
    gr.add_edge('E', 'F', 9)
    gr.add_edge('F', 'G', 5)
    gr.add_edge('G', 'H', 8)
    gr.add_edge('H', 'I', 7)
    gr.add_edge('H', 'J', 8)
    gr.add_edge('I', 'J', 6)
    gr.add_edge('J', 'K', 8)
    gr.add_edge('K', 'L', 5)
    gr.add_edge('L', 'M', 7)
    gr.add_edge('L', 'N', 5)
    gr.add_edge('M', 'N', 6)
    gr.add_edge('N', 'O', 9)
    gr.add_edge('O', 'P', 5)
    gr.add_edge('O', 'Q', 8)
    gr.add_edge('P', 'Q', 8)
    gr.add_edge('Q', 'R', 7)
    gr.add_edge('Q', 'S', 6)
    gr.add_edge('R', 'S', 6)
    gr.add_edge('R', 'T', 8)
    gr.add_edge('S', 'T', 8)
    gr.add_edge('S', 'A', 7)
    gr.add_edge('T', 'A', 5)
    gr.add_edge('T', 'B', 6)

    print("-----Branch and Bound TSP-----")
    res = tsp_bb(gr, 'A')
    print(res)
    
    print("-----Uniform Cost Search TSP-----")
    res_ucs = tsp_ucs(gr, 'A')
    print("UCS Result:", res_ucs)
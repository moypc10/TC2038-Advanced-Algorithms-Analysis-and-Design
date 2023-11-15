#Actividad: Implementación de "Tries" y recorridos en grafos

class WeightedGraph:
    _directed = True
    _adjacency_list = {}

    def __init__(self, directed=False):
        self._directed = directed
        self._adjacency_list = {}

    def clear(self):
        self._adjacency_list = {}

    def number_of_vertices(self):
        return len(self._adjacency_list)

    def vertices(self):
        return list(self._adjacency_list.keys())

    def edges(self):
        edge_list = []
        if self._directed:
            for v in self._adjacency_list:
                for edge in self._adjacency_list[v]:
                    edge_list.append((v, edge[0], edge[1]))
        else:
            for v in self._adjacency_list:
                for edge in self._adjacency_list[v]:
                    if (edge[0], v, edge[1]) not in edge_list:
                        edge_list.append((v, edge[0], edge[1]))
        return edge_list

    def add_vertex(self, v):
        if v not in self._adjacency_list:
            self._adjacency_list[v] = []

    def remove_vertex(self, v):
        if v not in self._adjacency_list:
            print("Warning: Vertex", v, "is not in graph.")
        else:
            self._adjacency_list.pop(v)
            for vertex in self._adjacency_list:
                self._adjacency_list[vertex] = [(x, w) for x, w in self._adjacency_list[vertex] if x != v]

    def add_edge(self, v1, v2, e=0):
        if v1 not in self._adjacency_list:
            print("Warning: Vertex", v1, "does not exist.")
        elif v2 not in self._adjacency_list:
            print("Warning: Vertex", v2, "does not exist.")
        elif not self._directed and v1 == v2:
            print("Warning: An undirected graph cannot have autocycles.")
        elif (v2, e) in self._adjacency_list[v1]:
            print("Warning: The edge (", v1, ",", v2, ",", e, ") already exists.")
        else:
            self._adjacency_list[v1].append((v2, e))
            if not self._directed:
                self._adjacency_list[v2].append((v1, e))

    def remove_edge(self, v1, v2, e):
        if v1 not in self._adjacency_list:
            print("Warning: Vertex", v1, "does not exist.")
        elif v2 not in self._adjacency_list:
            print("Warning: Vertex", v2, "does not exist.")
        else:
            self._adjacency_list[v1] = [(x, w) for x, w in self._adjacency_list[v1] if x != v2 and w != e]
            if not self._directed:
                self._adjacency_list[v2] = [(x, w) for x, w in self._adjacency_list[v2] if x != v1 and w != e]

    def adjacent_vertices(self, v):
        if v not in self._adjacency_list:
            print("Warning: Vertex", v, "does not exist.")
            return []
        else:
            return self._adjacency_list[v]

    def is_adjacent(self, v1, v2):
        if v1 not in self._adjacency_list:
            print("Warning: Vertex", v1, "does not exist.")
            return False
        elif v2 not in self._adjacency_list:
            print("Warning: Vertex", v2, "does not exist.")
            return False
        else:
            return any(edge[0] == v2 for edge in self._adjacency_list[v1])

    def print_graph(self):
        for vertex in self._adjacency_list:
            for edges in self._adjacency_list[vertex]:
                print(vertex, ": ", edges[0], " edge weight: ", edges[1])


def floyd_marshall(graph):
    BIG_NUMBER = float('inf')
    n = graph.number_of_vertices()  # number_of_vertices para obtener el número de vertex
    adjacency_matrix = [[BIG_NUMBER] * n for _ in range(n)]

    for i in range(n):
        adjacency_matrix[i][i] = 0

    for vertex in graph.vertices():
        vertex_index = graph.vertices().index(vertex)
        for neighbor, weight in graph.adjacent_vertices(vertex):
            neighbor_index = graph.vertices().index(neighbor)
            adjacency_matrix[vertex_index][neighbor_index] = weight

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if adjacency_matrix[i][k] != BIG_NUMBER and adjacency_matrix[k][j] != BIG_NUMBER and (
                        adjacency_matrix[i][k] + adjacency_matrix[k][j] < adjacency_matrix[i][j]):
                    adjacency_matrix[i][j] = adjacency_matrix[i][k] + adjacency_matrix[k][j]

    return adjacency_matrix

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

# Distancias más cortas con Floyd
shortest_distances_floyd = floyd_marshall(gr)

ciudad_origen = 'Ylane'  # Definir la ciudad de origen

print(f"Ciudad Origen: {ciudad_origen}")
origen_index = gr.vertices().index(ciudad_origen)  # Obtener el índice de la ciudad de origen

for i, vertex in enumerate(gr.vertices()):
    print(f"{vertex}: {shortest_distances_floyd[origen_index][i]}")
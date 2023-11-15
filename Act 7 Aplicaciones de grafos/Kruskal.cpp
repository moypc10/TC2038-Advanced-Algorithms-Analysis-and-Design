#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <set>

using namespace std;

// Estructura para representar una arista
struct Edge {
    string source, destination;
    int weight;

    Edge(string s, string d, int w) : source(s), destination(d), weight(w) {}

    // Sobrecarga del operador < para comparar aristas por peso
    bool operator<(const Edge& other) const {
        return weight < other.weight;
    }
};

class Graph {
    map<string, vector<Edge>> adjList;

public:
    // Agregar una arista al grafo
    void addEdge(string source, string destination, int weight) {
        adjList[source].emplace_back(source, destination, weight);
        adjList[destination].emplace_back(destination, source, weight);  // El grafo es no dirigido
    }

    // Algoritmo de Kruskal para encontrar el árbol de expansión mínima
    vector<Edge> kruskal() {
        vector<Edge> minimumSpanningTree;
        vector<Edge> allEdges;

        // Recolectar todas las aristas en el grafo
        for (const auto& pair : adjList) {
            for (const Edge& edge : pair.second) {
                allEdges.push_back(edge);
            }
        }

        // Ordenar todas las aristas en orden creciente de peso
        sort(allEdges.begin(), allEdges.end());

        // Utilizar un conjunto disjunto para detectar ciclos
        map<string, string> parent;
        for (const auto& pair : adjList) {
            parent[pair.first] = pair.first;
        }

        for (const Edge& edge : allEdges) {
            string sourceParent = findParent(parent, edge.source);
            string destParent = findParent(parent, edge.destination);

            // Si agregar esta arista no forma un ciclo, agrégala al árbol de expansión mínima
            if (sourceParent != destParent) {
                minimumSpanningTree.push_back(edge);
                parent[destParent] = sourceParent;
            }
        }

        return minimumSpanningTree;
    }

    // Función para encontrar el padre de un conjunto (utilizada para detectar ciclos)
    string findParent(map<string, string>& parent, string vertex) {
        if (parent[vertex] != vertex) {
            parent[vertex] = findParent(parent, parent[vertex]);
        }
        return parent[vertex];
    }
};

int main() {
    Graph graph;

    // Agregar las aristas al grafo (usando los datos proporcionados en la pregunta)
    graph.addEdge("Ylane", "Strento", 99);
    graph.addEdge("Ylane", "Oriaron", 117);
    graph.addEdge("Ylane", "Goding", 88);
    graph.addEdge("Goding", "Ontdale", 98);
    graph.addEdge("Ontdale", "Oriaron", 219);
    graph.addEdge("Ontdale", "Blebus", 165);
    graph.addEdge("Ontdale", "Togend", 210);
    graph.addEdge("Togend", "Blebus", 121);
    graph.addEdge("Blebus", "Oriaron", 291);
    graph.addEdge("Blebus", "Duron", 160);
    graph.addEdge("Duron", "Ertonwell", 121);
    graph.addEdge("Duron", "Lagos", 119);
    graph.addEdge("Lagos", "Niaphia", 300);
    graph.addEdge("Niaphia", "Ertonwell", 56);
    graph.addEdge("Niaphia", "Goxmont", 212);
    graph.addEdge("Ertonwell", "Adaset", 130);
    graph.addEdge("Adaset", "Goxmont", 103);
    graph.addEdge("Adaset", "Zrusall", 15);
    graph.addEdge("Zrusall", "Goxmont", 112);
    graph.addEdge("Zrusall", "Strento", 121);
    graph.addEdge("Strento", "Oriaron", 221);

    vector<Edge> minimumSpanningTree = graph.kruskal();

    cout << "Arbol de Expansion Minima (Kruskal):\n";
    for (const Edge& edge : minimumSpanningTree) {
        cout << edge.source << " - " << edge.destination << " (" << edge.weight << ")\n";
    }

    return 0;
}
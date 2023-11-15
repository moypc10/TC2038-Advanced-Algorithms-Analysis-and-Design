#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <limits>

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

    // Algoritmo de Prim para encontrar el árbol de expansión mínima
    vector<Edge> prim() {
        vector<Edge> minimumSpanningTree;
        set<string> visited;
        visited.insert(adjList.begin()->first);  // Comenzar desde el primer vértice del grafo

        while (visited.size() < adjList.size()) {
            Edge minEdge("", "", numeric_limits<int>::max());

            // Encontrar la arista de menor peso que conecta un vértice visitado con uno no visitado
            for (const string& visitedVertex : visited) {
                for (const Edge& edge : adjList[visitedVertex]) {
                    if (visited.find(edge.destination) == visited.end() && edge.weight < minEdge.weight) {
                        minEdge = edge;
                    }
                }
            }

            // Agregar el vértice de destino al conjunto visitado y la arista al árbol de expansión mínima
            visited.insert(minEdge.destination);
            minimumSpanningTree.push_back(minEdge);
        }

        return minimumSpanningTree;
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

    vector<Edge> minimumSpanningTree = graph.prim();

    cout << "Arbol de Expansion Minima (Prim):\n";
    for (const Edge& edge : minimumSpanningTree) {
        cout << edge.source << " - " << edge.destination << " (" << edge.weight << ")\n";
    }

    return 0;
}

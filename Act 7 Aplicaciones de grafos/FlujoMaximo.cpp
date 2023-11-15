#include <iostream>
#include <vector>
#include <queue>
#include <cstring>

using namespace std;

const int INF = 1e9;

struct Edge {
    int to, capacity, flow;
};

vector<vector<Edge>> graph;
vector<int> parent;

// Agrega una función para agregar aristas con capacidad y costo a la red
void addEdge(int from, int to, int capacity) {
    graph[from].push_back({to, capacity, 0});
    graph[to].push_back({from, 0, 0}); // Añade la arista de retroceso
}

int maxFlow(int source, int sink) {
    int maxFlow = 0;

    while (true) {
        queue<int> q;
        q.push(source);
        parent.assign(graph.size(), -1);

        while (!q.empty()) {
            int current = q.front();
            q.pop();

            for (const Edge& edge : graph[current]) {
                int to = edge.to;
                if (parent[to] == -1 && edge.capacity - edge.flow > 0) {
                    q.push(to);
                    parent[to] = current;
                }
            }
        }

        if (parent[sink] == -1) {
            break;
        }

        int minCapacity = INF;
        int current = sink;
        while (current != source) {
            int prev = parent[current];
            for (const Edge& edge : graph[prev]) {
                if (edge.to == current) {
                    minCapacity = min(minCapacity, edge.capacity - edge.flow);
                    break;
                }
            }
            current = prev;
        }

        current = sink;
        while (current != source) {
            int prev = parent[current];
            for (Edge& edge : graph[prev]) {
                if (edge.to == current) {
                    edge.flow += minCapacity;
                    bool found = false;
                    for (Edge& backEdge : graph[current]) {
                        if (backEdge.to == prev) {
                            backEdge.flow -= minCapacity;
                            found = true;
                            break;
                        }
                    }
                    if (!found) {
                        graph[current].push_back({prev, 0, -minCapacity});
                    }
                    break;
                }
            }
            current = prev;
        }

        maxFlow += minCapacity;
    }

    return maxFlow;
}

int main() {
    int numNodes = 14;
    graph.resize(numNodes);

    // Agregar las aristas con sus capacidades/costos
    addEdge(0, 1, 70);
    addEdge(0, 2, 80);
    addEdge(0, 5, 37);
    addEdge(1, 7, 72);
    addEdge(2, 3, 54);
    addEdge(3, 11, 82);
    addEdge(4, 2, 44);
    addEdge(4, 3, 69);
    addEdge(4, 11, 71);
    addEdge(5, 0, 43);
    addEdge(5, 4, 47);
    addEdge(5, 6, 24);
    addEdge(6, 5, 25);
    addEdge(6, 10, 76);
    addEdge(7, 1, 85);
    addEdge(7, 6, 61);
    addEdge(7, 8, 23);
    addEdge(8, 6, 82);
    addEdge(8, 9, 60);
    addEdge(9, 6, 42);
    addEdge(9, 13, 90);
    addEdge(10, 11, 50);
    addEdge(10, 12, 42);
    addEdge(10, 13, 34);
    addEdge(11, 12, 66);
    addEdge(12, 13, 75);
    addEdge(13, 10, 55);

    int source = 1;  // Índice del nodo fuente (A en este caso)
    int sink = 6;   // Índice del nodo sumidero (N en este caso)

    int flowMax = maxFlow(source, sink);

    cout << "Flujo maximo de B a H: " << flowMax << endl;

    return 0;
}

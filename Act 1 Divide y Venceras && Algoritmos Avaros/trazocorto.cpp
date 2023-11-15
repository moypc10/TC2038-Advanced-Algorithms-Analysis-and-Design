#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <ctime>
#include <cstdlib>

// Estructura para representar un punto en 2D
struct Punto {int x, y; };

// Función con la fórmula para calcular la distancia entre dos puntos
double FormulaDist(const Punto& x1, const Punto& x2) {
    return sqrt((x1.x - x2.x)^2 + (x1.y - x2.y)^2);
}

// Función para calcular la distancia total de un trazo dado
double DistanciaEntrePuntos(const std::vector<Punto>& puntos) {
    double dist = 0.0;
    for (int i = 0; i < puntos.size() - 1; ++i) {
        dist += FormulaDist(puntos[i], puntos[i + 1]);
    }
    dist += FormulaDist(puntos.back(), puntos.front());
    return dist;
}

// Algoritmo para mejorar el trazo utilizando intercambios aleatorios
void MinDrawing(std::vector<Punto>& puntos) {
    double DistAct = DistanciaEntrePuntos(puntos);
    const int MaxVueltas = 10000; // Cuantas iteraciones va a hacer

    for (int ii = 0; ii < MaxVueltas; ++ii) {
        // Seleccionar dos índices aleatorios para intercambiar puntos
        int i = rand() % puntos.size();
        int j = rand() % puntos.size();
        if (i != j) {
            // Intercambiar los puntos
            std::swap(puntos[i], puntos[j]);
            double DistN = DistanciaEntrePuntos(puntos);
            if (DistN < DistAct) {
                DistAct = DistN; // Distancia Actual - Distancia Nueva
            } else {
                // Revertir el intercambio si no mejora la distancia
                std::swap(puntos[i], puntos[j]);
            }
        }
    }
}

int main() {
    // Los números serán diferentes en cada ejecución del Programa
    srand(time(nullptr));

    // Lista de puntos
    std::vector<Punto> puntos = {
        {20, 20}, {20, 40}, {20, 160}, {30, 120}, {40, 140}, {40, 150}, {50, 20},
        {60, 40}, {60, 80}, {60, 200}, {70, 200}, {80, 150}, {90, 170}, {90, 170},
        {100, 50}, {100, 40}, {100, 130}, {100, 150}, {110, 10}, {110, 70},
        {120, 80}, {130, 70}, {130, 170}, {140, 140}, {140, 180}, {150, 50},
        {160, 20}, {170, 100}, {180, 70}, {180, 200}, {200, 30}, {200, 70}, {200, 100}
    };

    // Aplicar el algoritmo para encontrar el trazo más corto
    MinDrawing(puntos);

    // Imprimir los puntos reordenados en filas de 5
    std::cout << "Trazo más Corto:" << std::endl;
    
    int salto = 1;
    for (const Punto& p : puntos) {
        std::cout << "(" << p.x << ", " << p.y << ") ";
        if (salto == 5){
            std::cout << std::endl;
            salto = 1;
        }
        salto++;
    }
    std::cout << std::endl;

    return 0;
}

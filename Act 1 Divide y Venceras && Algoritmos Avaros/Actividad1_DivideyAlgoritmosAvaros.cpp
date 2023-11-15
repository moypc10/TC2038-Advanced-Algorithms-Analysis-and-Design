/*
 * Actividad: Ejemplos de "Divide y Vencerás" y Algoritmos Avaros
 *
 * Instituto Tecnológico y de Estudios Superiores de Monterrey
 * Campus Guadalajara
 * 
 * Moisés Hiram Pineda Campos - A01625510
 *
 */

#include <iostream>
#include <vector>
#include <chrono>
#include <cmath> //sqrt
#include <algorithm> //swap
#include <ctime> //time
#include <cstdlib> //rand

//MergeSort------------------------------------------------------------------------

// <--------------------> Method Merge <-------------------->
void merge(std::vector<int> &vec, int low, int m, int high, int &compare) {
  int i, j, k;
  int n1 = m - low + 1;
  int n2 = high - m;

  std::vector<int> L(n1);
  std::vector<int> R(n2);
  
  for (i = 0; i < n1; i++)
    L[i] = vec[low + i];
  
  for (j = 0; j < n2; j++)
    R[j] = vec[m + 1 + j];

  // Fusionar los vectores auxiliares Ly R ordenados
  i = j = 0;
  k = low;

  while (i < n1 && j < n2) {
    compare++;
    
    if (L[i] <= R[j]) {
      vec[k] = L[i];
      i++;
    } else {
      vec[k] = R[j];
      j++;
    }
    k++;
  }

   while (i < n1) {
        vec[k] = L[i];
        i++;
        k++;
    }

    while (j < n2) {
        vec[k] = R[j];
        j++;
        k++;
    }
}

// <--------------------> Method Merge Sort <--------------------> 
void mergeSort(std::vector<int> &vec, int low, int high, int &compare) {
  if (low < high) {
    int m = low + (high - low) / 2;
    mergeSort(vec, low, m, compare);
    mergeSort(vec, m + 1, high, compare);
    merge(vec, low, m, high, compare);
  }
}

//8 Reinas-------------------------------------------------------------------------

// Tamaño del Tablero de Ajedrez (8x8) y Contador de Soluciones
const int n = 8; 
int sol = 1;

// Crear "Tablero" del Juego de Tamaño NxN, lleno de "*"
std::vector<std::vector<char>> t(n, std::vector<char>(n, '*')); 

bool Peligro(int x, int y) {
    
    // Verificar Reinas en Peligro en las Columnas
    for (int i = 0; i < x; ++i) {
        if (t[i][y] == 'R') {
            return false;
        }
    }

    // Verificar Reinas en Peligro en la Diagonal Superior Derecha
    for (int i = x, j = y; i >= 0 && j < n; --i, ++j) {
        if (t[i][j] == 'R') {
            return false;
        }
    }

    // Verificar Reinas en Peligro en Diagonal Superior Izquierda
    for (int i = x, j = y; i >= 0 && j >= 0; --i, --j) {
        if (t[i][j] == 'R') {
            return false;
        }
    }

    // No se verifican Renglones porque no puede haber Reinas en el mismo renglón
    // No se verifican Diagonales Izquierda y Derecha porque todavía no se han colocado reinas en las filas posteriores ni en las diagonales inferiores 
    return true;
}

void OchoReinas(int x) {
    if (x == n) {
        // Imprimir el tablero con la solución encontrada
        if (sol != 6) {
            std::cout << "Posición Reina " << sol << ":" << std::endl;
            for (int i = 0; i < n; ++i) {
                for (int j = 0; j < n; ++j) {
                    std::cout << t[i][j] << " ";
                }
                std::cout << std::endl;
            }
            std::cout << "" << std::endl;
            sol++;
        }
        return;
    }

    // Imprimir el tablero
    for (int y = 0; y < n; ++y) {
        if (Peligro(x, y)) {
            t[x][y] = 'R';
            OchoReinas(x + 1);
            t[x][y] = '*';
        }
    }
}

//Trazo Más Corto------------------------------------------------------------------

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
    //MergeSort------------------------------------------------------------------------

    //Creación del Arreglo
    std::vector<int> arr = {9, 27, 45, 18, 63, 54, 90, 81, 72, 54, 36, 45, 32, 93, 23};

    //Imprimir Arreglo Original
    std::cout << "Arreglo Original: ";
    for (int num : arr)
        std::cout << num << " ";
    std::cout << std::endl;

    //Empezar a Contar Tiempo
    auto start = std::chrono::high_resolution_clock::now();

    //Aplicar el MergeSort
    int compSort = 0;
    
    mergeSort(arr, 0, arr.size() - 1, compSort);

    //Terminar de Contar el Tiempo
    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> duration = end - start;

    //Imprimir Arreglo Ordenado
    std::cout << "Arreglo Ordenado: ";
    for (int num : arr)
        std::cout << num << " ";
    std::cout << std::endl;

    //Imprimir Tiempo Usado
    std::cout << "\nTiempo MergeSort: " << duration.count() << " seconds \n" << std::endl;

    //8 Reinas-------------------------------------------------------------------------
    
    OchoReinas(0);

    //Trazo Más Corto------------------------------------------------------------------
    
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
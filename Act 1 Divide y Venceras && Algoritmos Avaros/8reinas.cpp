#include <iostream>
#include <vector>

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

int main() {    
    // Inicialización 1: Tablero vacío (sin reinas)
    OchoReinas(0);

    return 0;
}
#include <iostream>
#include <algorithm>
#include <chrono>
#include <vector>

using namespace std;

//Programación Dinámica - Precio Varillas -----------------------------------------------------------------

int preciosVar [] = {0, 1 , 5, 8, 9, 10, 17, 17, 20, 24 , 30};

int varillaRecursivo(int n){
    if (n <= 0){
        return 0;
    }

    int PrecioMaximo = 0;
    for (int i = 1; i <= n; i++){
        PrecioMaximo = max(PrecioMaximo, preciosVar[i] + varillaRecursivo(n - i));
    }
    return PrecioMaximo;
}

int varillaDinamico(int n){
    std::vector <int> valor(n+1);
    valor [0] = 0;

    for (int i = 1; i <= n; i++){
        int PrecioMaximo = 0;

        for (int j = 1; j <= std::min(i, 10); j++){
            PrecioMaximo = max(PrecioMaximo, preciosVar[j] + valor[i - j]);
        }
        
        valor [i] = PrecioMaximo;
        
    }
    
    return valor[n];
}

//Backtracking - Colores en Regiones ----------------------------------------------------------------------

const int TOTAL_REGIONES = 11;
const string regiones[] = {"Mark", "Julia", "Brian", "Steve", "Amanda", "Derek", "Kelly", "Allan", "Michelle", "Joanne", "Chris"};
const int colores[] = {1, 2, 3, 4}; // 1=rojo, 2=verde, 3=azul, 4=gris
const string coloresNomb[] = {"Rojo", "Verde", "Azul", "Gris"};
int colorRegion[TOTAL_REGIONES] = {0}; // Inicialmente, todos los colores son 0
int solucionesEncontradas = 0;

// Matriz que representa las regiones adyacentes
const bool adyacencias[TOTAL_REGIONES][TOTAL_REGIONES] = {
    //Mark: Julia y Steve
    {false, true, false, true, false, false, false, false, false, false, false},
    //Julia: Mark, Steve, Amanda, Derek,y Brian
    {true, false, true, true, true, true, false, false, false, false, false},
    //Brian: Derek, Julia y Kelly
    {false, true, false, false, false, true, true, false, false, false, false},
    //Steve: Mark, Julia, Amanda, Michelle, y Allan
    {true, true, false, false, true, false, false, true, true, false, false},
    //Amanda: Mark, Julia, Derek, Joanne, Michelle, y Steve
    {false, true, false, true, false, true, false, false, true, true, false},
    //Derek: Kelly, Brian, Julia, Amanda, Joanne y Chris
    {false, true, true, false, true, false, true, false, false, true, true},
    //Kelly: Brian, Derek y Kelly
    {false, false, true, false, false, true, false, false, false, true, true},
    //Allan: Steve y Michelle
    {false, false, false, true, false, false, false, false, true, false, false},
    //Michelle: Allan, Steve, Amanda, y Joanne
    {false, false, false, true, true, false, false, true, false, true, false},
    //Joanne: Michelle, Amanda, Derek, y Chris
    {false, false, false, false, true, true, false, false, true, false, true},
    //Chris: Joanne, Derek y Kelly
    {false, false, false, false, false, true, true, false, false, true, false}
};

// Función para verificar si un color es válido para una región
bool esColorValido(int region, int color) {
    for (int i = 0; i < TOTAL_REGIONES; i++) {
        if (i != region && adyacencias[region][i] && colorRegion[i] == color) {
            return false; // El color está siendo utilizado por una región adyacente
        }
    }
    return true;
}

// Función de backtracking para asignar colores a las regiones
bool asignarColores(int region) {
    if (region == TOTAL_REGIONES) {
        return true; // Todas las regiones tienen un color asignado
    }

    for (int color : colores) {
        if (esColorValido(region, color)) {
            colorRegion[region] = color; // Asignar el color a la región

            // Llamar recursivamente a la función para la siguiente región
            if (asignarColores(region + 1)) {
                return true; // Si se encontró una solución, regresar true
            }

            // Si no se encontró una solución, deshacer la asignación de color
            colorRegion[region] = 0;
        }
    }

    return false; // No se pudo encontrar una solución
}

//Contar Soluciones
/*void asignarColores(int region) {
    if (region == TOTAL_REGIONES) {
        solucionesEncontradas++; // Incrementa el contador de soluciones
        return;
    }

    for (int color : colores) {
        if (esColorValido(region, color)) {
            colorRegion[region] = color; // Asignar el color a la región

            // Llamar recursivamente a la función para la siguiente región
            asignarColores(region + 1);

            // Deshacer la asignación de color para probar con otro color
            colorRegion[region] = 0;
        }
    }
}*/

int main(){

    //Programacion Dinamica ---------------------------------------------------------------------------------
    int n = 8;
    cout << "Longitud Varilla: " << n << endl;

        //Recursivo
        auto TiempoRecursivo = chrono::high_resolution_clock::now();
        int gRecursiva = varillaRecursivo(n);
        cout << "\nGanancia Varilla Recursiva: " << gRecursiva << endl;
        auto FinRecursivo = chrono::high_resolution_clock::now();
        auto durRecursivo = chrono::duration_cast<chrono::microseconds> (FinRecursivo - TiempoRecursivo).count();
        cout << "Tiempo Recursivo: " << durRecursivo << endl;

        //Dinamico
        auto TiempoDinamico = chrono::high_resolution_clock::now();
        int gDinamico = varillaDinamico(n);
        cout << "\nGanancia Varilla Dinamica: " << gDinamico << endl;
        auto FinDinamico = chrono::high_resolution_clock::now();
        auto durDinamico = chrono::duration_cast<chrono::microseconds> (FinDinamico - TiempoDinamico).count();
        cout << "Tiempo Dinamico: " << durDinamico << endl;


    //Backtracking - Pintar Regiones ----------------------------------------------------------------------
    if (asignarColores(0)) {
        // Se encontró una solución
        cout << "\nAsignacion de Colores:" << endl;
        for (int i = 0; i < TOTAL_REGIONES; i++) {
            int color = colores[colorRegion[i] - 1];
            cout << regiones[i] << ": " << coloresNomb[color - 1] << endl;
        }
    } else {
        cout << "Inválido" << endl;
    }

    //asignarColores(0);
    //cout << "Total de soluciones encontradas: " << solucionesEncontradas << endl;

    return 0;
}

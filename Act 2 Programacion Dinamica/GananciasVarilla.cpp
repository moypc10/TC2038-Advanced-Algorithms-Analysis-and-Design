#include <iostream>
#include <algorithm>
#include <chrono>
#include <vector>

using namespace std;
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

int main(){
    
    
    int n;
    cout << "Longitud Varilla: ";
    cin >> n;

    while (n > 0){
        //Recursivo
        auto TiempoRecursivo = chrono::high_resolution_clock::now();
        int gRecursiva = varillaRecursivo(n);
        cout << "Ganancia Varilla Recursiva: " << gRecursiva << endl;
        auto FinRecursivo = chrono::high_resolution_clock::now();
        auto durRecursivo = chrono::duration_cast<chrono::microseconds> (FinRecursivo - TiempoRecursivo).count();
        cout << "Tiempo Recursivo: " << durRecursivo << endl;

        //Dinamico
        auto TiempoDinamico = chrono::high_resolution_clock::now();
        int gDinamico = varillaDinamico(n);
        cout << "Ganancia Varilla Dinamica: " << gDinamico << endl;
        auto FinDinamico = chrono::high_resolution_clock::now();
        auto durDinamico = chrono::duration_cast<chrono::microseconds> (FinDinamico - TiempoDinamico).count();
        cout << "Tiempo Dinamico: " << durDinamico << endl;

    }
    

    return 0;
}

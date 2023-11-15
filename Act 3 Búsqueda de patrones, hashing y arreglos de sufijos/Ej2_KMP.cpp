#include <iostream>
#include <fstream>
#include <string>
#include <string_view>
#include <vector>
#include <algorithm>
#include <chrono>

template<typename T>
std::ostream& operator<<(std::ostream& o, const std::vector<T>& a){
    for (const auto& ai : a)
        o << ai << " ";
    return o;
}

// Función para eliminar espacios en blanco de una cadena
std::string removeSpaces(const std::string& input) {
    std::string result;
    std::remove_copy_if(input.begin(), input.end(), std::back_inserter(result), ::isspace);
    return result;
}

std::vector<int> calcularLPS(const std::string& pat) {
    int m = pat.length();
    std::vector<int> lps(m, 0);
    int j = 0; // Longitud del sufijo coincidente más largo

    for (int i = 1; i < m; ++i) {
        while (j > 0 && pat[i] != pat[j]) {
            j = lps[j - 1];
        }

        if (pat[i] == pat[j]) {
            ++j;
        }
        lps[i] = j;
    }

    return lps;
}

std::vector<int> buscarOcurrenciasKMP(const std::string& texto, const std::string& palabra) {
    int n = texto.length();
    int m = palabra.length();
    std::vector<int> lps = calcularLPS(palabra);
    std::vector<int> indices;
    int j = 0; // Índice para 'palabra'

    for (int i = 0; i < n; ++i) {
        while (j > 0 && texto[i] != palabra[j]) {
            j = lps[j - 1];
        }

        if (texto[i] == palabra[j]) {
            ++j;
        }

        if (j == m) {
            // Encontramos una coincidencia completa
            int inicio = i - m + 1;
            indices.push_back(inicio);
            j = lps[j - 1];
        }
    }

    return indices;
}

void texto(std::string word, std::string libro){
    int longitud = 50, cont = 0, indice = 0;

    std::vector<int> ocurrencias = buscarOcurrenciasKMP(libro, word);

    for (int indice : ocurrencias) {
        cont = indice;
    }
    
    std::cout << "Palabra (" <<  word << "): " << libro.substr(cont,longitud) << std::endl;
}

int main() {
    std::string theAab = "input.txt"; // Reemplaza con el nombre de tu archivo

    std::ifstream archivo(theAab);

    if (!archivo.is_open()) {
        std::cerr << "Error al abrir el archivo." << std::endl;
        return 1;
    }

    std::string libro;
    std::string linea;

    while (std::getline(archivo, linea)) {
        libro += linea; // Agrega cada línea del archivo al string 'libro'
    }

    archivo.close(); // Cierra el archivo después de leerlo
    
    std::string word1 = "black";
    std::string word2 = "fool";
    std::string word3 = "symbols";
    std::string word4 = "wind";
    std::string word5 = "years";
    
    // Iniciar Chronos
    auto start_time = std::chrono::high_resolution_clock::now(); // Registrar el tiempo de inicio

    texto(word1, libro);
    texto(word2, libro);
    texto(word3, libro);
    texto(word4, libro);
    texto(word5, libro);

    // Terminar Chronos
    auto end_time = std::chrono::high_resolution_clock::now(); // Registrar el tiempo de finalización
    auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end_time - start_time); // Cambiar a std::chrono::milliseconds
    std::cout << "Tiempo de ejecucion: " << duration.count() << " milisegundos" << std::endl; // Imprimir en milisegundos

    return 0;
}
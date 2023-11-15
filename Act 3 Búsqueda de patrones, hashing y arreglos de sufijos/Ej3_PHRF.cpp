#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <tuple>
#include <map>
#include <algorithm>
#include <fstream>

long long prhf(const std::string_view& s, long long p = 53, long long m = 1000000009) {
    long long hash = 0;
    long long pwr = 1;
    for (const auto& c : s) {
        hash = (hash + c * pwr) % m;
        pwr = (pwr * p) % m;
    }
    return hash;
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

    // Crear un objeto istringstream para leer el texto
    std::istringstream stream(libro);

    // Mapa para almacenar las palabras divididas y sus conteos
    std::map<long long, std::pair<std::string, int>> palabrasConConteo;

    std::string palabra;
    while (stream >> palabra) {
        long long hash = prhf(palabra);

        // Verificar si la palabra ya está en el mapa
        auto it = palabrasConConteo.find(hash);
        if (it != palabrasConConteo.end()) {
            // Incrementar el conteo si la palabra ya existe
            it->second.second++;
        } else {
            // Agregar la palabra al mapa si es la primera vez que se encuentra
            palabrasConConteo[hash] = std::make_pair(palabra, 1);
        }
    }

    // Almacenar los elementos del mapa en un vector
    std::vector<std::pair<long long, std::pair<std::string, int>>> palabrasVector;
    for (const auto& entry : palabrasConConteo) {
        palabrasVector.push_back(entry);
    }

    // Ordenar el vector en orden descendente por conteo
    std::sort(palabrasVector.begin(), palabrasVector.end(),
              [](const auto& a, const auto& b) {
                  return a.second.second > b.second.second;
              });

    // Imprimir las 20 palabras más repetidas en orden descendente
    int count = 0;
    for (const auto& entry : palabrasVector) {
        if (count >= 20) {
            break;
        }
        std::cout << "Top " << count+1 << " (" << entry.second.first << "): " << entry.second.second << std::endl;
        count++;
    }

    return 0;
}


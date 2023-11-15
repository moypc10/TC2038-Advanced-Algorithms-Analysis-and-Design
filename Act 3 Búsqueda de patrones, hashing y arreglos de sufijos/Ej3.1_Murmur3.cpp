#include <cstdint>
#include <cstring>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <tuple>
#include <map>
#include <algorithm>
#include <fstream>

// Murmur3 hash function
uint32_t Murmur3(const void* key, int len, uint32_t seed) {
    const uint32_t c1 = 0xcc9e2d51;
    const uint32_t c2 = 0x1b873593;
    const int r1 = 15;
    const int r2 = 13;
    const uint32_t m = 5;
    const uint32_t n = 0xe6546b64;

    uint32_t hash = seed;

    const int nblocks = len / 4;
    const uint32_t* blocks = static_cast<const uint32_t*>(key);

    for (int i = 0; i < nblocks; i++) {
        uint32_t k = blocks[i];
        k *= c1;
        k = (k << r1) | (k >> (32 - r1));
        k *= c2;

        hash ^= k;
        hash = ((hash << r2) | (hash >> (32 - r2))) * m + n;
    }

    const uint8_t* tail = static_cast<const uint8_t*>(key) + nblocks * 4;
    uint32_t k1 = 0;

    switch (len & 3) {
        case 3:
            k1 ^= tail[2] << 16;
        case 2:
            k1 ^= tail[1] << 8;
        case 1:
            k1 ^= tail[0];
            k1 *= c1;
            k1 = (k1 << r1) | (k1 >> (32 - r1));
            k1 *= c2;
            hash ^= k1;
    }

    hash ^= len;
    hash ^= (hash >> 16);
    hash *= 0x85ebca6b;
    hash ^= (hash >> 13);
    hash *= 0xc2b2ae35;
    hash ^= (hash >> 16);

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
        const char* data = palabra.c_str();
        uint32_t seed = 0; // You can change the seed as needed.

        uint32_t hash = Murmur3(data, strlen(data), seed);

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

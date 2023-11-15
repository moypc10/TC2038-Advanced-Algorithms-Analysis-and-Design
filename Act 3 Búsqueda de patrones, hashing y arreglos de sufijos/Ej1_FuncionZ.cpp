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

std::vector<int> zFunction(const std::string_view& s) {
    auto n = s.size();
    std::vector<int> z(n, 0);
    int l = 0;
    int r = 0;
    for (int i = 1; i < n; i++) {
        if (i < r) {
            z[i] = (r - i) < z[i - l] ? (r - i) : z[i - l];
        }
        while ((i + z[i] < n) && (s[z[i]] == s[i + z[i]])) {
            z[i]++;
        }
        if ((i + z[i]) > r) {
            l = i;
            r = i + z[i];
        }
    }
    return z;
}

void texto(std::string word, std::string libro){
    int cont = 0, i = 0, longitud = 50;

    // Agregar la palabra al principio de contentWithoutSpaces
    std::string libroPal = word + libro;
    zFunction(libroPal);

    while(cont == 0)
    {
        i++;
        if(word.length() == zFunction(libroPal)[i]){
            cont = i;
        }
    }

    std::cout << "Palabra (" <<  word << "): " << libro.substr(cont-word.length(),longitud) << std::endl;
    
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
    
    std::string word1 = "small";
    std::string word2 = "squatted";
    std::string word3 = "Destruction";
    std::string word4 = "girl";
    std::string word5 = "sacks";
    
    //Iniciar Chronos
    auto start_time = std::chrono::high_resolution_clock::now(); // Registrar el tiempo de inicio

    texto(word1, libro);
    texto(word2, libro);
    texto(word3, libro);
    texto(word4, libro);
    texto(word5, libro);

    //Terminar Chronos
    auto end_time = std::chrono::high_resolution_clock::now(); // Registrar el tiempo de finalización
    auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end_time - start_time);
    std::cout << "Tiempo de ejecucion: " << duration.count() << " microsegundos" << std::endl;

    return 0;
}

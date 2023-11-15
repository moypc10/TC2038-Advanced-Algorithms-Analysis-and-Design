#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <algorithm>

std::pair<int, std::string> findLCS(const std::string &X, const std::string &Y)
// Función para encontrar la longitud de la secuencia común más larga (LCS) y su contenido.
// Adaptado de https://www.geeksforgeeks.org/printing-longest-common-subsequence/
{
    int m = X.size();
    int n = Y.size();
    std::vector<std::vector<int>> L(m + 1, std::vector<int>(n + 1));
    std::string result = "";

    // Construcción de la matriz L
    for (int i = 0; i <= m; i++)
    {
        for (int j = 0; j <= n; j++)
        {
            if (i == 0 || j == 0)
                L[i][j] = 0;
            else if (X[i - 1] == Y[j - 1])
            {
                L[i][j] = L[i - 1][j - 1] + 1;
            }
            else
                L[i][j] = std::max(L[i - 1][j], L[i][j - 1]);
        }
    }

    // Reconstrucción de la LCS a partir de la matriz L
    int i = m, j = n;
    while (i > 0 && j > 0)
    {
        if (X[i - 1] == Y[j - 1])
        {
            result = X[i - 1] + result;
            i--;
            j--;
        }
        else if (L[i - 1][j] > L[i][j - 1])
        {
            i--;
        }
        else
        {
            j--;
        }
    }

    return {L[m][n], result};
}

int main(){
    std::vector<std::string> frases;
    frases.push_back("Moises Hiram Pineda Campos");
    frases.push_back("Anita lava la tina hola");
    frases.push_back("Aprovecha cada dia como una oportunidad unica");
    frases.push_back("La musica es el lenguaje universal");
    frases.push_back("La diversidad enriquece nuestras vidas");
    frases.push_back("La creatividad no tiene fronteras");
    frases.push_back("El viaje es tan importante como el destino");
    frases.push_back("La amistad es un tesoro inestimable");
    frases.push_back("Nunca subestimes tu propio potencial");
    frases.push_back("xyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx");

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

    for (int i = 0 ; i < frases.size(); i++) {
            std::pair<int, std::string> Resultado = findLCS(libro, frases[i]);
            std::cout << "\nFrase (" << frases[i] << "): " << std::endl;
            std::cout << "Longitud: " << Resultado.first << "\n";
            std::cout << "Contenido: " << Resultado.second << "\n";
    }

    return 0;
}
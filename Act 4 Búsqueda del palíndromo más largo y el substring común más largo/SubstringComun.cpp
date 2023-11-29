#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <algorithm>

/*
ELABORADO POR:
Samuel García A01642317
Emilio Berber A01640603
Moisés Pineda A01625510

INSTRUCCIONES:
Finalmente compara los dos archivos transmisionX.txt, encontrando el substring común más largo que haya. 
Realiza lo mismo entre los archivos mcodeX.txt.
*/

std::string txtToString(std::string fileName)
// Función auxiliar para cargar textos a strings
{
    std::ifstream file(fileName);
    if (!file.is_open())
    {
        std::cerr << "Error al abrir el archivo " << fileName << "." << std::endl;
        return "";
    }
    std::string content((std::istreambuf_iterator<char>(file)), std::istreambuf_iterator<char>());
    file.close();

    if (content.empty())
    {
        std::cerr << "El archivo " << fileName << " está vacío." << std::endl;
    }
    return content;
}

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

int main() {
    std::vector<std::string> mcodes = {
        txtToString("mcode1.txt"),
        txtToString("mcode2.txt"),
        txtToString("mcode3.txt")
    };

    std::vector<std::string> transmissions = {
        txtToString("transmission1.txt"),
        txtToString("transmission2.txt")
    };

    // Mostrar cabecera
    std::cout << "=========================================\n";
    std::cout << "    Análisis LCS entre Transmisiones    \n";
    std::cout << "=========================================\n\n";

    // Comparar las dos transmisiones entre sí
    std::pair<int, std::string> lcs_transmissions = findLCS(transmissions[0], transmissions[1]);
    std::cout << "LCS entre las dos transmisiones:\n";
    std::cout << "---------------------------------\n";
    std::cout << "Longitud: " << lcs_transmissions.first << "\n";
    std::cout << "Contenido: \n" << lcs_transmissions.second << "\n\n";
    
    // Mostrar cabecera 2
    std::cout << "=========================================\n";
    std::cout << "    Análisis LCS entre Archivos mcode    \n";
    std::cout << "=========================================\n\n";

    // Comparar todos los pares posibles de mcodes entre sí
    for (size_t i = 0; i < mcodes.size(); i++) {
        for (size_t j = i + 1; j < mcodes.size(); j++) {
            std::pair<int, std::string> lcs_mcodes = findLCS(mcodes[i], mcodes[j]);
            std::cout << "LCS entre mcode" << (i + 1) << " y mcode" << (j + 1) << ":\n";
            std::cout << "---------------------------------\n";
            std::cout << "Longitud: " << lcs_mcodes.first << "\n";
            std::cout << "Contenido: \n" << lcs_mcodes.second << "\n\n";
        }
    }

    return 0;
}

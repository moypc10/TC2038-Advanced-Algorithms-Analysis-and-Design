#include <iostream>
#include <string>
#include <vector>
#include <fstream>

/*
ELABORADO POR:
Samuel García A01642317
Emilio Berber A01640603
Moisés Pineda A01625510

INSTRUCCIONES:
Suponiendo que el código malicioso puede tener código "espejeado" (palíndromos de caracteres), sería buena idea buscar este tipo de código en una transmisión. 
Realiza la búsqueda del palíndromo más largo dentro de los archivos de transmisión utilizando el algoritmo de Manacher. 
Muestra en pantalla el palíndromo encontrado así como su longitud.
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

std::string manacher(const std::string &s)
// Adaptado de https://www.geeksforgeeks.org/manachers-algorithm-linear-time-longest-palindromic-substring-part-4/
{
    int len = s.length();
    // Si la cadena está vacía, no regreso nada.
    if (len == 0)
        return "";

    std::string t = "^"; // agregar '^' al principio y '$' al final nos deja no preocuparnos por desbordamiento (arruina palíndromos que superan el límite).
    for (int i = 0; i < len; i++)
    {
        t += "#" + s.substr(i, 1); // Esta línea crea textos en formato '#a#' por todo el texto, nos permite hacer mini palíndromos centrados en cada letra.
    }
    t += "#$"; // Aquí esta el '$'

    // Trabajamos con el nuevo texto t.
    int tLen = t.length();
    std::vector<int> P(tLen, 0);
    int center = 0, rightBoundary = 0;
    for (int i = 1; i < tLen - 1; i++)
    {
        int iMirror = 2 * center - i; // Este es un truquillo, en realidad es center - (i - center).

        if (rightBoundary > i)
            P[i] = std::min(rightBoundary - i, P[iMirror]);

        // Intentamos expandir el palíndromo centrado en 'i'
        while ((i + 1 + P[i] < tLen) && (i - 1 - P[i] >= 0) && (t[i + 1 + P[i]] == t[i - 1 - P[i]]))
            P[i]++;

        // Si el palíndromo centrado en 'i' supera el rightBoundary, reajustamos el centro.
        if (i + P[i] > rightBoundary)
        {
            center = i;
            rightBoundary = i + P[i];
        }
    }

    // Aquí se extrae el palíndromo (o mejor dicho su tamaño y posición).
    int maxLength = 0, centerIndex = 0;
    for (int i = 1; i < tLen - 1; i++)
    {
        if (P[i] > maxLength)
        {
            maxLength = P[i];
            centerIndex = i;
        }
    }

    // Agrego par poder desplegar los índices encontrados.
    int startIdx = (centerIndex - maxLength) / 2;
    int endIdx = startIdx + maxLength - 1;

    std::cout << "Palíndromo más largo empieza en índice: " << startIdx << "\n";
    std::cout << "Palíndromo más largo acaba en índice: " << endIdx << "\n";

    return s.substr(startIdx, maxLength);
}

int main()
{
    std::vector<std::string> transmissions = {
        txtToString("transmission1.txt"),
        txtToString("transmission2.txt")
    };

    std::cout << "==========================================\n";
    std::cout << " Análisis de Palíndromos en Transmisiones \n";
    std::cout << "==========================================\n\n";

    for (size_t t = 0; t < transmissions.size(); t++)
    {
        std::cout << "Transmisión " << (t + 1) << ":\n";
        std::cout << "------------------------------------------\n";

        std::string longestPalindrome = manacher(transmissions[t]);
        if (longestPalindrome.empty())
        {
            std::cout << "No se encontró ningún palíndromo en esta transmisión.\n";
        }
        else
        {
            std::cout << "El palíndromo más largo encontrado es:\n";
            std::cout << "\"" << longestPalindrome << "\"\n";
            std::cout << "Longitud: " << longestPalindrome.size() << "\n";
        }

        std::cout << "\n\n";
    }

    return 0;
}


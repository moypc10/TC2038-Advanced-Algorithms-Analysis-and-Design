#include <iostream>
#include <vector>
#include <string>
#include <string_view>
#include <fstream>

template<typename T>
std::ostream& operator<<(std::ostream& o, const std::vector<T>& a)
{
    for (const auto& ai : a)
        o << ai << " ";
    return o;
}

size_t lcSub(const std::string_view& s1, const std::string_view& s2)
{
    const auto n = s1.size();
    const auto m = s2.size();
    std::vector<size_t> lcSuff(n * m);
    size_t maxlcs = 0;

    for (size_t i = 0; i < n; i++) {
        for (size_t j = 0; j < m; j++) {
            if (s1[i] != s2[j]) {
                lcSuff[i * m + j] = 0;
            }
            else {
                if ((i == 0) || (j == 0))
                    lcSuff[i * m + j] = 0;
                else
                    lcSuff[i * m + j] = lcSuff[(i - 1) * m + (j - 1)] + 1;
            }
            if (lcSuff[i * m + j] > maxlcs)
                maxlcs = lcSuff[i * m + j];
        }
    }
    return maxlcs;
}

std::vector<std::string> lcSubStrings(const std::string_view& s1, const std::string_view& s2)
{
    const auto n = s1.size();
    const auto m = s2.size();
    std::vector<size_t> lcSuff(n * m);
    size_t maxlcs = 0;
    std::vector<std::string> strings;

    for (size_t i = 0; i < n; i++) {
        for (size_t j = 0; j < m; j++) {
            if (s1[i] != s2[j]) {
                lcSuff[i * m + j] = 0;
            }
            else {
                if ((i == 0) || (j == 0))
                    lcSuff[i * m + j] = 0;
                else
                    lcSuff[i * m + j] = lcSuff[(i - 1) * m + (j - 1)] + 1;
            }
            if (lcSuff[i * m + j] > maxlcs)
                maxlcs = lcSuff[i * m + j];
        }
    }

    for (size_t i = 0; i < n; i++) {
        for (size_t j = 0; j < m; j++) {
            if (lcSuff[i * m + j] == maxlcs)
                strings.push_back(std::string(s1.substr(i - maxlcs + 1, maxlcs)));
        }
    }
    return strings;
}

int main()
{
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
    frases.push_back("xyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyz");
    
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
            std::cout << "\nFrase (" << frases[i] << "): " << std::endl;
            std::cout << "Length of the longest common substrings: " << lcSub(libro, frases[i]) << "\n";
            std::cout << "Vector of the longest common substrings: " << lcSubStrings(libro, frases[i]) << "\n";
    }

    return 0;
}

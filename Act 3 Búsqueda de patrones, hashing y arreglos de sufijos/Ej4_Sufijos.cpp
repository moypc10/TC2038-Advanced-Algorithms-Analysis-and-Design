#include <iostream>
#include <vector>
#include <string>
#include <string_view>
#include <algorithm>

template<typename T>
std::ostream& operator<<(std::ostream& o, const std::vector<T>& a) {
    for (const auto& ai : a)
        o << ai << " ";
    return o;
}

std::vector<int> suffixArray(const std::string_view& s) {
    // Build s$
    std::string t = {s.begin(), s.end()};
    t.append("$");

    // Extract suffixes
    auto n = t.length();
    std::vector<std::string> suffixes;

    for (size_t i = 0; i < n; i++)
        suffixes.push_back(t.substr(n - i - 1, i + 1));

    // Sort suffixes
    std::sort(suffixes.begin(), suffixes.end());

    // Build array
    std::vector<int> a(n);
    for (size_t i = 0; i < n; i++)
        a[i] = n - suffixes[i].size();
    return a;
}

void texto(std::string s){
    std::cout << "\nOracion (" << s << "): " << suffixArray(s) << "\n";
}

int main() {
    std::string Oracion1 = "The cool Martian wind crept across the rust-red expanse of desert";
    std::string Oracion2 = "Destruction of his oxygen mask presented no menace.";
    std::string Oracion3 = "You like meYeah, Monk, breathed";
    std::string Oracion4 = "We will not bother you. Not at all, Monk answered, his heart pounding";
    std::string Oracion5 = "Your old man's busy taking down the tent";
    
    texto(Oracion1);
    texto(Oracion2);
    texto(Oracion3);
    texto(Oracion4);
    texto(Oracion5);

    return 0;
}

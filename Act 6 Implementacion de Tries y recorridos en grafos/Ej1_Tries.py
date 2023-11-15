#Actividad: Implementación de "Tries" y recorridos en grafos

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_word = True

    def search(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_end_of_word

    def starts_with(self, prefix):
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True

# Función para insertar palabras de un archivo .txt en el Trie
def insert_words_from_file(file_path, trie):
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()  # Split the line into words
            for word in words:
                word = word.strip()  # Remove leading/trailing whitespace
                if word:
                    trie.insert(word)

# Crear un Trie
trie = Trie()

# Ruta al archivo de texto
libro = 'input.txt'

# Insertar palabras del archivo en el Trie
insert_words_from_file(libro, trie)

# Search words
print("1. Search hungry: ", trie.search("hungry"))
print("2. Search shower: ", trie.search("shower"))
print("3. Search Moises: ", trie.search("Moises"))
print("4. Search hello: ", trie.search("hello"))
print("5. Search most: ", trie.search("most"))
print("6. Search sand: ", trie.search("sand"))
print("7. Search beautiful: ", trie.search("beautiful"))
print("8. Search car: ", trie.search("car"))
print("9. Search airpods: ", trie.search("airpods"))
print("10. Search algorithm: ", trie.search("algorithm"))
print("11. Search make: ", trie.search("make"))
print("12. Search sand: ", trie.search("sand"))
print("13. Search night: ", trie.search("night"))
print("14. Search yesterday: ", trie.search("yesterday"))
print("15. Search favorite: ", trie.search("favorite"))
print("16. Search place: ", trie.search("place"))
print("17. Search is: ", trie.search("is"))
print("18. Search Las: ", trie.search("Las"))
print("19. Search smi: ", trie.search("smi"))
print("20. Search coo: ", trie.search("coo"))

# Search prefixes
print("\n1. Search hungry: ", trie.starts_with("hungry"))
print("2. Search shower: ", trie.starts_with("shower"))
print("3. Search Moises: ", trie.starts_with("Moises"))
print("4. Search hello: ", trie.starts_with("hello"))
print("5. Search most: ", trie.starts_with("most"))
print("6. Search sand: ", trie.starts_with("sand"))
print("7. Search beautiful: ", trie.starts_with("beautiful"))
print("8. Search car: ", trie.starts_with("car"))
print("9. Search airpods: ", trie.starts_with("airpods"))
print("10. Search algorithm: ", trie.starts_with("algorithm"))
print("11. Search make: ", trie.starts_with("make"))
print("12. Search sand: ", trie.starts_with("sand"))
print("13. Search night: ", trie.starts_with("night"))
print("14. Search yesterday: ", trie.starts_with("yesterday"))
print("15. Search favorite: ", trie.starts_with("favorite"))
print("16. Search place: ", trie.starts_with("place"))
print("17. Search is: ", trie.starts_with("is"))
print("18. Search Las: ", trie.starts_with("Las"))
print("19. Search smi: ", trie.starts_with("smi"))
print("20. Search coo: ", trie.starts_with("coo"))
#----------------------------------------------------------------------------------
# End of file
#----------------------------------------------------------------------------------

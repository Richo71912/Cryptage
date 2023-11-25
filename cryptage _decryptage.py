import string

# Cryptage Vigenere
def chiffrement_vigenere(texte, cle):
    texte = texte.upper()
    cle = cle.upper()
    alphabet = string.ascii_uppercase
    tableau_chiffrement = str.maketrans(alphabet, alphabet[len(cle):] + alphabet[:len(cle)])
    texte_chiffre = texte.translate(tableau_chiffrement)
    return texte_chiffre

def dechiffrement_vigenere(texte_chiffre, cle):
    texte_chiffre = texte_chiffre.upper()
    cle = cle.upper()
    alphabet = string.ascii_uppercase
    tableau_dechiffrement = str.maketrans(alphabet[len(cle):] + alphabet[:len(cle)], alphabet)
    texte = texte_chiffre.translate(tableau_dechiffrement)
    return texte

# Cryptage Cesare
def chiffrement_cesare(texte, cle):
    texte = texte.upper()
    alphabet = string.ascii_uppercase
    tableau_chiffrement = str.maketrans(alphabet, alphabet[cle:] + alphabet[:cle])
    texte_chiffre = texte.translate(tableau_chiffrement)
    return texte_chiffre

def dechiffrement_cesare(texte_chiffre, cle):
    texte_chiffre = texte_chiffre.upper()
    alphabet = string.ascii_uppercase
    tableau_dechiffrement = str.maketrans(alphabet[cle:] + alphabet[:cle], alphabet)
    texte = texte_chiffre.translate(tableau_dechiffrement)
    return texte

# Cryptage Affine
def chiffrement_affine(texte, a, b):
    texte = texte.upper()
    alphabet = string.ascii_uppercase
    tableau_chiffrement = str.maketrans(alphabet, alphabet[a] + alphabet[:a])
    texte_chiffre = texte.translate(tableau_chiffrement)
    return texte_chiffre

def dechiffrement_affine(texte_chiffre, a, b):
    texte_chiffre = texte_chiffre.upper()
    alphabet = string.ascii_uppercase
    tableau_dechiffrement = str.maketrans(alphabet[a] + alphabet[:a], alphabet)
    texte = texte_chiffre.translate(tableau_dechiffrement)
    return texte

# Menu de choix
def menu():
    print("1 - Chiffrement Vigenere")
    print("2 - Dechiffrement Vigenere")
    print("3 - Chiffrement Cesare")
    print("4 - Dechiffrement Cesare")
    print("5 - Chiffrement Affine")
    print("6 - Dechiffrement Affine")
    print("7 - Quitter")

# Boucle principale
while True:
    menu()
    choix = int(input("Veuillez saisir votre choix : "))
    if choix == 1:
        texte = input("Veuillez saisir le texte à crypter : ")
        cle = input("Veuillez saisir la clé de cryptage : ")
        print(chiffrement_vigenere(texte, cle))
    elif choix == 2:
        texte_chiffre = input("Veuillez saisir le texte chiffré à decrypter : ")
        cle = input("Veuillez saisir la clé de cryptage : ")
        print(dechiffrement_vigenere(texte_chiffre, cle))
    elif choix == 3:
        texte = input("Veuillez saisir le texte à crypter : ")
        cle = int(input("Veuillez saisir la clé de cryptage : "))
        print
import hashlib# J'import la bibliotheque hashlib 
def hasher_texte(texte):# def cré une fonction qui s'appelle hasher_texte
    # Créer un objet de hachage SHA-256
    sha256_hash = hashlib.sha256()
    # Hasher le texte encodé en UTF-8
    sha256_hash.update(texte.encode('utf-8'))
    # Retourner le hash en hexadécimal
    return sha256_hash.hexdigest()
# Exemple d'utilisation
texte = "Bonjour, ceci est un test de hachage !"
print("Hash du texte :", hasher_texte(texte))
texte2 = "Bonjour, ceci est un test de hachage !"
print("Hash du texte :", hasher_texte(texte2))

def hasher_fichier(fichier):
    """Calcule le hash SHA-256 d'un fichier."""
    sha256 = hashlib.sha256()
    try:
        with open(nom_fichier, "rb") as f:
            while bloc := f.read(4096):  # Lecture en blocs de 4 Ko
                sha256.update(bloc)
        return sha256.hexdigest()
    except FileNotFoundError:
        print("Erreur : fichier introuvable.")
        return None

# Exemple d'utilisation :
nom_fichier = "fichier.txt"
hash_calcul = hasher_fichier(nom_fichier)
if hash_calcul:
    print(f"Hash SHA-256 de {nom_fichier} : {hash_calcul}")

#Sauvegarde du hash d'un fichier
def sauvegarder_hash(hash_value, fichier_hash):
    """Sauvegarde le hash dans un fichier texte."""
    with open(fichier_hash, "w") as f:
        f.write(hash_value + "\n")

nom_fichier_hash = "hash_sha256.txt"
if hash_calcul:
    sauvegarder_hash(hash_calcul, nom_fichier_hash)
    print(f"Hash sauvegardé dans {nom_fichier_hash}.")

#Comparaison de deux fichiers pour vérifier leur intégrité
def comparer_fichiers(fichier1, fichier2):
    """Compare le hash SHA-256 de deux fichiers pour vérifier leur intégrité."""
    hash1 = hasher_fichier(fichier1)
    hash2 = hasher_fichier(fichier2)
    
    if hash1 and hash2:
        if hash1 == hash2:
            print("Les fichiers sont identiques.")
        else:
            print("Les fichiers sont différents.")
    else:
        print("Impossible de comparer les fichiers.")

# Exemple d'utilisation :
comparer_fichiers("fichier.txt", "copie_fichier.txt")

#Comparaison d'un fichier avec un hash sauvegardé
def verifier_fichier_avec_hash(nom_fichier, fichier_hash):
    """Vérifie si le hash d'un fichier correspond à un hash sauvegardé."""
    try:
        with open(fichier_hash, "r") as f:
            hash_sauvegarde = f.readline().strip()
        
        hash_actuel = hasher_fichier(nom_fichier)
        
        if hash_actuel == hash_sauvegarde:
            print("Le fichier n'a pas été modifié.")
        else:
            print("Attention : le fichier a été modifié !")
    except FileNotFoundError:
        print("Erreur : fichier de hash introuvable.")

# Exemple d'utilisation :
verifier_fichier_avec_hash("fichier.txt", "hash_sha256.txt")

#Menu interactif
def menu():
    while True:
        print("\nMenu:")
        print("1 - Hasher un fichier")
        print("2 - Sauvegarder le hash d'un fichier")
        print("3 - Comparer deux fichiers")
        print("4 - Vérifier un fichier avec un hash sauvegardé")
        print("5 - Quitter")
        
        choix = input("Choisissez une option : ")

        if choix == "1":
            nom_fichier = input("Nom du fichier à hasher : ")
            hash_resultat = hasher_fichier(nom_fichier)
            if hash_resultat:
                print(f"Hash SHA-256 : {hash_resultat}")
        
        elif choix == "2":
            nom_fichier = input("Nom du fichier à hasher : ")
            hash_resultat = hasher_fichier(nom_fichier)
            if hash_resultat:
                nom_fichier_hash = input("Nom du fichier pour sauvegarder le hash : ")
                sauvegarder_hash(hash_resultat, nom_fichier_hash)
                print(f"Hash sauvegardé dans {nom_fichier_hash}.")
        
        elif choix == "3":
            fichier1 = input("Nom du premier fichier : ")
            fichier2 = input("Nom du deuxième fichier : ")
            comparer_fichiers(fichier1, fichier2)
        
        elif choix == "4":
            nom_fichier = input("Nom du fichier à vérifier : ")
            fichier_hash = input("Nom du fichier contenant le hash : ")
            verifier_fichier_avec_hash(nom_fichier, fichier_hash)
        
        elif choix == "5":
            print("Programme terminé.")
            break
        else:
            print("Choix invalide, veuillez réessayer.")

# Exécuter le menu
menu()

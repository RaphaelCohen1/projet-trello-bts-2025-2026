f = open("fichier.txt", "w")
f.write("Bonjour, je suis un fichier !\n")
f.close()

f = open("fichier.txt", "a")
f.write("Je suis ajoutée à la fin du fichier !")
f.close()

f = open("fichier.txt", "r")
contenu = f.read()
print(contenu)
f.close()

f = open("fichier.txt", "r")
print(f.readline())
f.close()
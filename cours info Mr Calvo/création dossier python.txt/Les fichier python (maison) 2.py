# Les fichiers en python

"""
Un fichier est un ensemble de données d’un format déterminé qui est généralement stocké sur un disque dur pour assurer justement la persistance des données.
Il y a deux sortes de fichiers :
•	Fichiers textes
•	Fichiers binaires
Plusieurs types de fichiers binaires :
•	Fichiers exécutables (programmes …exe, .elf)
•	Fichiers images
•	Fichiers sons
•	Fichiers videos
Il y a 4 opérations de base sur les fichiers :
1.	Ouverture d’un fichier
2.	Fermeture d’un fichier
3.	Lecture d’un fichier
4.	Ecriture dans un fichier
"""

# Ouverture d'un fichier en lecture ("r" pour read)
fic = open("Pays.txt","r")

# Lecture du fchier en une seule fois avec fonction read()
contenu = fic.read()
print(contenu)
        
# Fermeture du fichier fonction close()
fic.close()


print("##############################")
fic = open("Pays.txt", "r")

ligne = fic.readline()
while ligne != "":
    print(ligne)
    ligne = fic.readline()
fic.close()



#Ouverture d'un fichier en ecriture ("w")
fic = open("titi.txt", "w")
fic.write("Salut comment allez vous...?\n")
fic.write("comment se sont passees tes vacances...\n")
fic.write("wesh gros:!!!\n")
fic.write("bon ok salut!!!\n")

fic.close()

fic = open("titi.txt", "r")
contenu = fic.read()
print(contenu)
fic.close()


fic = open("tata.txt", "w")
fic.write(str(100))
fic.close()


'''
Exercice
Creer un programme python qui enregistre dans un
fichier 'nombres.txt' les carres des 10 premiers nombres
Dans le fichier, ces carres seront espace par un espace
'''

ficNb = open("nombres.txt",'w')
for i in range(1,11):
    carrée = i*i
    ficNb.write(str(carrée))
    ficNb.write(" ")

ficNb.close()

ficNb = open("nombres.txt","r")
contenu = ficNb.read()
print(contenu)
ficNb.close()

# Ouverture d'un fichier en mode append "a"
ficNb = open("nombres.txt","a")
ficNb.write(str(11*11))
ficNb.write("")
ficNb.write(str(12*12))

ficNb.close()

























    

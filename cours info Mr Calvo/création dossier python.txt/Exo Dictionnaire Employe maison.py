# Exercice I
'''
Une entreprise emploie 5 salaries depuis 6 ans.
Chaque salarie a vu son salaire augmente chaque annee.
L'entreprise a enregistre pour chacun d'eux les differents salaires
sur les 6 ans dans un fichier salairesEmpl.txt
Le format de ce fichier est le suivant:
nom salaire1 salaire2 ... salaire6
Exemple:
Dupont 2000 2150 2200 2290 2320 2350

salaire1 salaire2 ... salaire6 representent les differents salaires
d'un employe sur les 6 ans.

On desire recuperer ces informations de ce fichier de la maniere suivante:
chaque ligne du fichier etant composee d'un nom suivi de 6 valeurs de salaire,
on crée un dictionnaire dont la cle est represente par le nom de l'employe  = etape 1 : ouvrir le  fichier et le lire ligne par ligne puis 
et la valeur correspondante est representee par une liste contenant les 6 valeurs de salaire de l'employe. = 

Le but est de calculer le salaire moyen pour chaque salarie.

On doit donc separer chaque valeur de salaire pour une ligne donnée du fichier 
Pour cela, on utilise la fonction split() de python permettant de separer
les elements d'une chaine de caracteres a l'aide d'un caractere separateur.

Exemple separateur = caractere espace:
chaine = "ceci est un exemple"
print(chaine.split())

animaux = "chien, chat, souris"
print(animaux.split(', '))

animal = animaux.split(', ')
print(animal)
print(animal[0])
'''
dicoEmpl = dict()
#Ouverture du fichier en mode lecture
fic = open("Salaires emp.txt", "r")

#Lecture du fichier ligne par ligne
ligne = fic.readline()
while ligne !="":
    print(ligne)
    listeSal = ligne.split()
    cle = listeSal[0]
    dicoEmpl[cle] = listeSal[1:len(listeSal)-1]
    ligne = fic.readline()
fic.close()
print(dicoEmpl)

print(dicoEmpl["Dupont"])

#Calcul Moyenne
for valeur in dicoEmpl.values():
    print(valeur)

    somme = 0
    for i in range(0,len(valeur)):
        sal = int(valeur[i])
        somme = somme + sal
moyenne = somme / len(valeur)

print("La moyenne = ", moyenne)

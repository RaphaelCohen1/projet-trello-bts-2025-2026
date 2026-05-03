# Ceci est un commentaire sur une ligne
(''')Pour definir un commentaire
'''(')Pour definir un caractère
(")Pour definir une variable
(input)Pour lire une variable
'''
'''
Ce commmentaire utilise
3 lignes de commentaire
La variable a represente un
nombre entier
'''

#Les variables en python
'''
Les variables en python n'ont pas à etre declarées
On les utilises dès que l'ont en a besoin
'''
Exemple
#Initialisation d'une variable ou affectation
a=12  #a est une variable de type entier
b=3014#b est une variable de type réel
c='A' #c est une variable de type caractere
d="Bonjour" #d est une variable de type caracteres
e=True #e est une variable de type booleen
f=False #f est de type booleen

#Affectation
#variable=valeur
a=50

# Instruction Afficher -->fonction print()
# Afficher une chaine de caractères
print("Bonjour comment va tu?")
# Afficher le contenu d'une variable
print(a)
# Afficher une chaine de caractère et  le contenu d'une variable
print("La variable a vaut",a)
# Saisie au clavier -->fonction input() 3 méthodes
# Tout ce que l'on saisi au clavier est FORCEMENT une chaine de caractères
'''
#1ere méthode
print("Veuillez saisir une valeur:")
d = input()
print("vous avez saisi:",d)

#2ème méthode
d=input("Veuillez saisir une valeur:")
print("vous avez saisi:",d)
#3ème méthode
'''
Convertir le résultat de input() qui est une chaine
de caractère en un nombre entier(age)
'''
age=int(input("Entrez votre age"))#"int" sert a convertir les nombres donner entre guillemet en entier ET QUE LES NOMBRES !!!!. Exemple: int("15")-> 15
print("vous avez saisi:",age)                                                                                                          # int("15b")-> "15" 
print(age+1)

# Instruction conditinnelle (SI....ALORS....SINON)--> if..elif..else
if age >=18:
     print("vous etes un adulte!!")
else:
    if age>=1 and age <3:
         print("Tu est un nourrisson!!")
    elif age >=3 and age< 12: #elif=contraction de else et if
         print("Tu est un enfant!!")
    else:
         print("Tu est un ado!!")

# Instruction de boucle TANT QUE ---> while
while age>=0:
    print("vous avez",age,"ans")
    age=int(input("Entrez votre age"))

         
    



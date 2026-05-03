'''
1)
Ecrire un programme python permettant de saisir
un nombre entier de manière repetitive.
La saisie va s'arreter dès lors que le nombre entier est <0.
Le traitement est le suivant:
Si le nombre est pair on affiche "pair" sinon on affiche "impair"
On rappel que le modulo correspond au symbole %
'''
'''#Affectation
#variable=valeur
nb=int(input("Entrer un nombre entier"))
while nb>=0:
     if nb%2==0:
       print("Pair")
     else:
       print("Impair")
     nb = int(input("Entrer un nombre entier"))'''
'''   

2)
Procedure pour obtenir un nombre entier negatif
-prendre un nombre entier en decimal
-convertir ce nombre en binaire
-inverser les bits de l'etape precedente
-ajouter "1" au resultat de l'etape precedente 
'''
'''
3)
Jeu de devinette
Ecrire un programme python qui demande à l'utilisateur d'entrer un nombre entier entre 1 et 100.
Le programme choisi un nombre mystère (ex55) qui reste cache.
L'utilisateur entre une valeur entre 1 et 100 et le programme lui indique par un message "trop petit" si le nombre rentrer est < nombre mystère ou lui indique par message "trpo grand"
si le nombre rentrer est > nombre mystere ou lui affiche le message " Bravo vous avez trouvez!" si le nombre rentre est égal au nombre mystere.
Le programme s'arrete des que le nombre mystère aura été trouvé.
'''
#Choix du nombre mystère
nbMystere = 28

nb=int(input("Entrer un nombre entier entre 1 et 100"))

while nb !=nbMystere:  # "!=" =>comme si que l'on dit "différent"
    if nb <1:
         print ("Désolé votre nombre est <1 recommencez")
    elif nb>100:
         print ("Désolé votre nombre est >100 recommencez")
    else:
        if nb < nbMystere:
            print( "Trop petit!!")
        else:
            print( "Trop Grand!!")
    nb=int(input("Entrer un nombre entier entre 1 et 100:")) 
print ("Bravo vous avez trouver")







    

     

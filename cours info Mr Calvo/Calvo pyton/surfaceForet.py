'''

Une foret initialement de 20Ha perd chaque année 10%
de sa surface et dans le meme temps gagne 3Ha.
Ecrire un programme qui demande à l'utilisateur d'entrer
un nombre d'années (soit N); le programme doit calculer la surface à l'année N et l'afficher


annee 0 S0 = 20
annee 1 S0*0.9+3=18+3=21=S1
annee 2 S1*0.9+3=18.9+3=21.9=S2
annee 2 S2*0.9+3=S3
'''

surface = 20
compteur = 1
nbAnnees= int(input("Entrer un nombre d'années:"))
while compteur<= nbAnnees:
    surface = surface*0.9+3
    compteur =compteur+1
print( "La surface vaut", surface, "au bout de", nbAnnees, "annees")

'''
Demonstration mathématique de la limite
On supose que la surface ne varira pas beaucoup dans les temps très loingtains
sl= sl*0.9+3

sl -  sl*0.9 = 3
sl (1sl-0.9)= 3
0.1*sl=3
sl= 3/0.1= 3/1/10 3*10/1=30
'''

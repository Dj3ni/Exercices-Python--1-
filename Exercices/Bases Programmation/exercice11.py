# Exercice 11

# Dans un autre script:
# Générez deux nombres aléatoire (entre 0 et 100)
# Affichez ces deux nombres en demandant à l'utilisateur d'en donner la
# somme
# Continuez à lui demander tant que la réponse est mauvaise.
# A la fin du programme, affichez à l'utilisateur le nombre d'erreurs qu'il a
# commises

from random import randint

nombre1 = randint(0,100)
nombre2 = randint(0,100)

addition = int(input("Faites l'addition entre les nombres: " + str(nombre1) +" et " + str(nombre2) + " : "))

tentatives = []

while addition != (nombre1 + nombre2):
    addition = int(input("Mauvaise réponse, veuillez réessayer: "))
    tentatives.append(addition)

if tentatives ==[]:
    print("Bravo vous avez réussi du 1er coup!")
else:
    print("Vous avez fait " + str(len(tentatives)) + " erreur" )

# Correction: 
    # Liste inutile de nouveau on stocke dans une variable!

nombre1 = randint(0,100)
nombre2 = randint(0,100)

errors = 0

addition = int(input("Faites l'addition entre les nombres: " + str(nombre1) +" et " + str(nombre2) + " : "))

while addition != (nombre1 + nombre2):
    errors = errors + 1
    addition = int(input("Mauvaise réponse, veuillez réessayer: "))

print("Tu as fait: " + str(errors) + "erreur(s)")

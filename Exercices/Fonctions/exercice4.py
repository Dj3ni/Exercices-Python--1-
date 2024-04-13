# Exercice 4

# Écrivez une fonction qui renvoie au programme appelant une liste de n entiers
# allant de 1 à 6 (déterminés aléatoirement). n étant passé en paramètre.
# Par exemple, si 3 est passé en paramètre, la fonction renvoie une liste de 3
# entiers entre 1 et 6.
from random import randint

def entiers(n):
    liste = []
    for i in range(n):
        pick = randint(1,6)
        liste.append(pick)
    print(liste)

entiers(10)

# Correction: Correct, ici plus court, utiliser return

def entiers(n):
    liste = []
    for i in range(n):
        liste.append(randint(1,6))
    return liste

print(entiers(5))


# Exercice 10

# Demandez à l'utilisateur d'entrer des nombre jusqu'à ce qu'il donne la valeur 0.
# Ensuite, affichez le plus grand et le plus petit nombre que l'utilisateur a donné.

nombre = int(input("Veuillez entrez un nombre, tapez'0 pour terminer: "))

guess = []

while nombre != 0:
    if guess == []:
        guess.append(nombre)
    nombre = int(input("Veuillez entrez un nombre, tapez'0 pour terminer: "))
    
    if nombre < guess[0]:
        guess.insert(0,nombre)
    elif nombre > guess[-1]:
        guess.insert(len(guess), nombre)

guess.remove(0)
print(guess)
print(guess[0], guess[-1])

# Autre façon de faire, plus simple:

guess.append(nombre)

while nombre != 0:
    nombre = int(input("Veuillez entrez un nombre, tapez'0 pour terminer: "))
    guess.append(nombre)

guess.sort()
guess.remove(0)
print(guess)
print(guess[0], guess[-1])

# ne pas utiliser de liste: stocker les valeurs dans les variables (pour une question de mémoire)!! 
# Et pas enlever 0 car il peut y avoir des nombres négatifs
# La deuxieme solution est une fausse bonne idée: cela coûte beaucoup plus en RAM!
# Eviter tant que possible de faire un tableau

# Correctif:

nombre = int(input("Veuillez entrez un nombre, tapez'0 pour terminer: "))

greater = nombre
lower = nombre

while nombre !=0:
    nombre = int(input("Veuillez entrez un nombre, tapez'0 pour terminer: "))
    if nombre < lower:
        lower = nombre
    elif nombre > greater:
        greater = nombre

print("Plus grand: " + str(greater))
print("Plus petit: " + str(lower))
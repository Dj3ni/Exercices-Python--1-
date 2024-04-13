# Exercice 12

# Dans un autre script:
# Créez un programme qui va demander à l'utilisateur d'entrer des nombres.
# Le programme continuera à en demander tant que l'utilisateur n'aura pas donné
# deux nombres identiques d'affilée.
# En fin de programme, affichez la somme de tous les nombres entrés par
# l'utilisateur.


number = int(input("Veuillez entrez un premier nombre: "))

entry = []

if entry ==[] or entry != [0,1]:
    entry.append(number)
    number = int(input("Veuillez entrez le nombre suivant: "))
    entry.append(number)

while entry[-1] != entry [-2]:
    number = int(input("Entrez deux nombres identiques d'affilée pour terminer: "))
    entry.append(number)

entry.remove(entry[-1])

print(entry)

print("Voici la somme des différents nombres encodés: " + str(sum(entry)))

# Pas besoin de liste! ça marche mais c'est  moins performant!

# Correctif :

previous = int(input("Nombre: "))
number = int(input("Nombre: "))
sum_number = number + previous

while number != previous:
    previous = number
    number = int(input("Nombre: "))
    sum_number = sum_number + number

print("Voici la somme des différents nombres encodés: " + str(sum_number))
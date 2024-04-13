from random import randint

# # Partie 1

couleurs = ["a","b","c","d","e","f"]
index = randint(0,len(couleurs)-1)
print(couleurs)
print(couleurs[index])

# # Partie 2

stagiaires = ["Mara", "Leslie", "Dorothée", "Mélusine","Déborah","Chantal"]
cible = randint(0,5)
print(stagiaires[cible])

# # Partie 3

victime = int(input("Choisis un nombre entre 0 et 5: "))
print(stagiaires)

print(stagiaires[1:victime])
print(stagiaires [victime:5])

while victime > len(stagiaires) -1:
    victime = int(input("Nombre invalide, choisis un nombre entre 0 et 5: "))
print(stagiaires[1:victime])
print(stagiaires [victime:5])

# # Partie 4: correct

frontend = []
membres = input("Entrez un nom, tapez 'stop' pour finir: ")

while membres != "stop":
    frontend.append(membres)
    membres = input("Entrez un autre nom, tapez 'stop' pour finir: ")

print(frontend)

# Partie 5

wad = []
membres = input("Veuillez entrer le nom d'une participante, entrez 'stop'pour finir: ")

while membres != "stop":
    position = int(input("A quelle place doit-on la mettre dans la liste?" ))
    wad.insert(position, membres)
    membres= input("Participante suivante, tapez 'stop' pour terminer: ")
print(wad)

# Partie 6: correct

numbers = [1,2,3,4,5,5,4,3,2,1]
print(numbers)

modif= int(input("Entrez un nombre à supprimer de la liste: ")) 
numbers.remove(modif)
print(numbers)

# Partie 7

numbers = [1,2,3,4,5]
print(numbers)

# while numbers != []: ne pas mettre de liste!!!
while len(numbers)>0:
    removed= numbers.pop(0)
    print(removed)
print(numbers)


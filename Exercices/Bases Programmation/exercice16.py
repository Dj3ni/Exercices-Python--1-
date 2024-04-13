# Exercice 16

# Créez un script qui demande à l'utilisateur un mot.
# Ensuite donner à l'utilisateur le nombre de voyelle de ce mot.
# Indice: vous pouvez établir la liste des voyelles facilement ["a", "e", "i",
# "o", "u", "y"] et nous avons vu un moyen de vérifier qu'un élément se trouve
# dans un groupe.

mot = list(input("Donnez-moi un mot: "))
# mot = list(mot)
print(mot)

voyelles = ["a","e", "i","o","u", "y"]

voyelles_mot = []

i = 0

for i in range(len(mot)):
    if mot[i] in voyelles:
        voyelles_mot.append(mot[i])

print("Nombre de voyelles dans votre mot: " + str(len(voyelles_mot)))
print( "Les voyelles de votre mot sont: " + str(voyelles_mot) )


# Correction:Pas de liste!!!

VOWELS = ["a","e", "i","o","u", "y"]

word = input("Donnez-moi un mot: ")
print(word)

compteur = 0

for letter in word:
    if letter in VOWELS:
        compteur = compteur +1

print("Nombre de voyelles dans votre mot: " + str(compteur))
# print( "Les voyelles de votre mot sont: " + str(voyelles_mot) )

# Alternative

VOWELS = ["a","e", "i","o","u", "y"]

word = input("Donnez-moi un mot: ")
print(word)

compteur = 0

for letter in word:
    if letter in VOWELS:
        compteur += 1

print(f"Nombre de voyelles dans votre mot: {compteur}")

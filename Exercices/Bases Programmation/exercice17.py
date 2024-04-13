# Exercice 17
# A l'aide de 2 boucles, créez un script qui énumère toutes les cartes d'un jeu de
# cartes à jouer. Une des boucles concerne les symboles (cœur, carreau, pique,
# trèfle) et une autre les valeurs (as, deux, trois, …, dame, roi).

SYMBOLS = [" of Hearts", " of Spades", " of Clubs", " of Diamonds"]
FIGURES = ["Jack", "Queen", "King", "Ace"]
NUMBERS = list(range(2,10))
CARDS = NUMBERS + FIGURES

for i in CARDS:
    for j in SYMBOLS:
        print(i,j)

# Correction:

SYMBOLS = [" of Hearts", " of Spades", " of Clubs", " of Diamonds"]
VALUE = ["2","3","4","5","6", "7", "8", "9","Jack", "Queen", "King", "Ace"]

for i in SYMBOLS:
    for j in VALUE:
        print(f"{j}{i}")

# Exercice 10

# Écrivez une fonction qui renvoie une carte au hasard.
# Cette fonction n'a pas d'argument et renvoie As, 2, 3, 4, 5, 6, 7, 8, 9,
# 10, Valet, Dame, Roi.
# En utilisant la fonction décrite ci-dessus, écrivez une fonction qui renvoie une
# liste de cartes. Le nombre de cartes sera déterminé par un argument de la
# fonction
from random import randint

def pick_card():
    SYMBOLS = [" of Hearts", " of Spades", " of Clubs", " of Diamonds"]
    VALUE = ["2","3","4","5","6", "7", "8", "9","Jack", "Queen", "King", "Ace"]
    pick = f"{VALUE[randint(0,len(VALUE)-1)]}" f"{SYMBOLS[randint(0,len(SYMBOLS)-1)]}"
    return pick

# print(pick_card())


def deck(n):
    DECK = []
    for i in range (n):
        DECK.append(pick_card())
    return DECK

# print(deck(6))

# Autre manière: 

# def deck2(n):
#     deck = ""
#     for i in range (n):
#         deck = deck + pick_card() + ", " # ou "\n" pour renvoi à la ligne
#     return deck

# print(deck2(6))

# Exercice 10-Bis

# Ensuite, créez une fonction qui reçoit une liste de cartes en paramètre.
# Cette fonction renverra le mot “Poker” s' il y a 5 fois la même valeur dans la liste.
# Si il y a 4 fois la même valeur elle renverra “Carré”.
# Si il y a 3 fois la même valeur elle renverra “Brelan”.
# Enfin si il n'y a que 2 fois la même valeur elle renverra “Paire”.
# Dans les autres cas, elle renverra “Rien”.

def card_points(HAND):
    count = 0
    cartes = []
    print (HAND) # pour debug
    for i in HAND:
        cartes.append(i[0])
        # print(i[0]) # pour debug
    print(cartes) # pour debug
    for i in cartes:
        total = cartes.count(i)
        if count < total:
            count = total
        # print (count) # pour debug
    print(count)
    if count == 5:
        print("POKER!")
    elif count == 4:
        print("Carré!")
    elif count == 3:
        print("Brelan!")
    elif count == 2:
        print("Paire!")
    else:
        print("Rien")

HAND = deck(6)

card_points(HAND)
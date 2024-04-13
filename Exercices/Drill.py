from random import randint
# Exercice 1 et 2

# word = input("Donnez-moi un mot: ")
# print("Votre mot est: "f"{word}")

# Exercice 3 à 5

# number = int(input("Donnez-moi un nombre: "))

# if number > 10:
#     print("Ce nombre est plus grand que 10")
# else:
#     print("Ce nombre est plus petit ou égal à 10")

# Exercice 6

# number = int(input("Donnez-moi un nombre: "))

# if number >= 10:
#     print("You rock!")
# elif 8 < number:
#     print("Well done!")
# elif 5 < number:
#     print("Really?")
# else:
#     print("No comment...")

# Exercice 7

# number = int(input("Donnez-moi un nombre entre 1 et 10: "))

# while 1 > number or number > 10:
#     number = int(input("Donnez-moi un nombre entre 1 et 10: "))

# print("Votre nombre est:" f"{number}")

# Exercice 8:

# PWD = "Pyth0n"
# tentative = 3

# pwd = input("Entrez votre mdp: ")

# while pwd != PWD and tentative > 1:
#     tentative -= 1
#     pwd = input("Entrez votre mdp, il vous reste " f"{tentative}" " tentatives: ")

# if tentative == 0:
#     print("Mot de passe incorrect!")
# else:
#     print("Mot de passe correct")

# Exercice 9

# n1 = randint(0,6)
# n2 = randint(0,6)
# n3 = randint(0,6)

# while n1 != n2 or n2 != n3:
#     n2 = randint(0,6)
#     n3 = randint(0,6)

# print(f"{n1}{n2}{n3}")

# Exercice 10

# number = int(input("Donnez un nombre, tapez 0 pour stopper: "))

# lowest = number
# highest = number

# while number != 0:
#     number = int(input("Donnez un nombre, tapez 0 pour stopper: "))
#     if number < lowest:
#         lowest = number
#     elif number > highest:
#         highest = number

# print(f"{lowest} {highest}")

# Exercice 11

# n1 = randint(0,100)
# n2 = randint(0,100)
# count = 0

# somme = int(input("Faites la somme des nombres "f"{n1}" " et " f"{n2}"" : "))

# while somme != (n1 + n2):
#     count += 1
#     somme = int(input("Faites la somme des nombres "f"{n1}" " et " f"{n2}"" : "))

# print(" Bravo! Il vous a fallu " f"{count}" " tentatives")

# Exercice 13

# COUNTDOWN = 100

# while COUNTDOWN > 0:
#     print(COUNTDOWN)
#     COUNTDOWN -= 1

# print("Décollage!!!!")

# Exercice 14

# word = input("Donnez un mot, appuyez sur 'end' pour arrêter: ")

# trigger = "t"
# count = 0

# while word != "end":
#     count += 1
#     if word[0] == trigger:
#         print(word + "!!!")
#     word = input("Donnez un mot, appuyez sur 'end' pour arrêter: ")

# print(count)

# Exercice 16

# number = int(input("Entrez un nombre entre 1 et 100: "))

# while number > 100 or number < 1:
#     number = int(input("Entrez un nombre entre 1 et 100: "))

# somme = sum(range(number+1))

# print(somme)

# word = input("Donnez un mot: ")

# VOWELS = ["a","e","i","o","u","y"]
# count = 0

# for letter in word:
#     if letter in VOWELS:
#         count += 1

# print("Il y a " f"{count}" "voyelles")

# Exercice 17

SYMBOLS = ["Spades", "Diamonds", "Hearts", "Clubs"]

VALUES = ["2","3","4","5","6", "7", "8", "9","Jack", "Queen", "King", "Ace"]

for i in SYMBOLS:
    for j in VALUES:
        print(str(j) + " of " + str (i))





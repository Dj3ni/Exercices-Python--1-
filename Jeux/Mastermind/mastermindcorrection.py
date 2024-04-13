# Correctif exercices

from random import randint


# CODE_LENGHT = 4 # peut le mettre en constante pour avoir un seul endroit pour les modifications
# LETTERS = ["a","b","c","d","e", "f"]

# code = []

# while len(code) < CODE_LENGHT:
#     index = randint(0,len(LETTERS)-1)
#     code.append(LETTERS[index])

# print(code)

# Partie 3

# liste = ["Je","t'","aime","mon","coeur"]

# for i in range(len(liste)):
#     print(str(liste[i]))

# Partie 4 : utiliser boucle for

CODE_LENGHT = 4

LETTERS = ["a","b","c","d","e","f"]
code = []

for b in range(CODE_LENGHT):
    index = randint(0,len(LETTERS)-1)
    letter = LETTERS[index]
    code.append(letter)

print(code)

# Partie 5: Demander une proposition

# guess = input("Devinez le code de: " + str(CODE_LENGHT) + " couleurs parmi les lettres 'a,b,c,d,e,f': ")

# while len(guess)!= CODE_LENGHT:
#     guess = input("Devinez le code de: " + str(CODE_LENGHT) + " couleurs parmi les lettres 'a,b,c,d,e,f': ")

# guess = list(guess)

# Partie 5: confirmer les lettres exactes

# correct= []

# for i in range(CODE_LENGHT):
#     if code[i] == guess[i]:
#         # print("same!")
#         correct.append(i)

# print("Vous avez : "+ str(len(correct))+ " lettre(s) bien placée(s)")

# Partie 6: 

guess = None
essai_max = 12
essai = 0

while guess != code and essai < essai_max:
    guess = input("Devinez le code de: " + str(CODE_LENGHT) + " couleurs parmi les lettres 'a,b,c,d,e,f': ")

    while len(guess)!= CODE_LENGHT:
        guess = input("Devinez le code de: " + str(CODE_LENGHT) + " couleurs parmi les lettres 'a,b,c,d,e,f': ")
    
    guess = list(guess)

    correct= []

    for letter in range(CODE_LENGHT):
        if code[letter] == guess[letter]:
            correct.append(letter)

    print("Vous avez : "+ str(len(correct))+ " lettre(s) bien placée(s)")


# Partie 7: verification lettres mal placées

    wrong = []
    for i_guess in range(CODE_LENGHT):
        for i_code in range(CODE_LENGHT):
            if guess[i_guess] == code[i_code]:
                if i_code not in correct and i_guess not in correct:
                        if i_code not in wrong:
                            wrong.append(i_code)
                            break # permet d'arrêter de checker
    
    print(f"{len(wrong)} lettres mal placées")
    essai +=1

if code == guess:
    print("Bravo!")
else: 
    print(f"Dommage, il ne te reste plus de tentative. Le code était: {code}")


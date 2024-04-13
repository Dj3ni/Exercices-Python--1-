# Exercice 7

# Écrivez une fonction qui écrit un mot de 5 lettres avec les lettres suivantes: "a",
# "i", "l", "n", "o","r", "s", "t". Le mot sera ensuite retourné par la fonction.
# Attention, les lettres ne peuvent être utilisées qu'une seule fois chacune dans le
# mot.
# Par exemple: "tsoni" est un mot valide mais pas "liara"

from random import randint
# Correction
# def random_word():
#     LETTERS = ["a","i","l","n","o","r","s","t"]
#     new = ""
#     for i in range(5):
#         pick = randint(0,len(LETTERS)-1)
#         letter = LETTERS[pick]
#         new += letter
#         LETTERS.remove(letter)
#     return(new)

# print(random_word())

# Deuxième possibilité

def random_word(n):
    if n > 8:
        n = 8
    LETTERS = ["a","i","l","n","o","r","s","t"]
    new = ""
    for i in range(n):
        pick = randint(0,len(LETTERS)-1)
        new += LETTERS.pop(pick)        
    return(new)

print(random_word(10))

# attention à prévoir les erreurs de programme: 
# Dans le cas ici, prévoir que si "n" > 8, n=8

def random_word(liste,n):
    if n > len(liste):
        n = len(liste)
    new = ""
    for i in range(n):
        pick = randint(0,len(liste)-1)
        new += liste.pop(pick)        
    return(new)

LETTERS = ["a","i","l","n","o","r","s","t"]

print(random_word(LETTERS,10))
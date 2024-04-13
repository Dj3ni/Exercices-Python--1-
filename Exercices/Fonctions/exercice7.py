# Exercice 7

# Écrivez une fonction qui écrit un mot de 5 lettres avec les lettres suivantes: "a",
# "i", "l", "n", "o","r", "s", "t". Le mot sera ensuite retourné par la fonction.
# Attention, les lettres ne peuvent être utilisées qu'une seule fois chacune dans le
# mot.
# Par exemple: "tsoni" est un mot valide mais pas "liara"

from random import randint

n = 0

def random_word(n):
    LETTERS = ["a","i","l","n","o","r","s","t"]
    word = ""
    for i in range(n):
        pick = randint(0,len(LETTERS)-1)
        while LETTERS[pick] in word:
            pick = randint(0,len(LETTERS)-1)
        word = word + LETTERS[pick]
    print(word)


random_word(7)

# Exercice 7 tris

def random_word(n,LIST):
    word = ""
    for i in range(n):
        pick = randint(0,len(LIST)-1)
        while LIST[pick] in word:
            pick = randint(0,len(LIST)-1)
        word = word + LIST[pick]
    print(word)

LETTERS = ["a","i","l","n","o","r","s","t"]
n = 0

random_word(5,LETTERS)
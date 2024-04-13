# Exercice 6

# Écrivez une fonction qui prend un mot en paramètre et qui retourne ce même
# mot, mais sans les voyelles ("a", "e", "i", "o", "u", "y").
# Exemple: Si je passe "telegramme" comme paramètre, la fonction retournera
# "tlgrmm"
# Attention: on ne gère pas les caractères spéciaux !

def no_vowels(word):
    VOWELS = ["a","e","i","o","u","y"] # ou "aeiouy"
    new = ""
    for letter in word:
        if letter not in VOWELS:
            new = new + letter # ou new += letter
    return new

word = input("Donnez un mot à transformer: ")
print(no_vowels(word))

# Autre façon:

def no_vowels(word):
    VOWELS = ["a","e","i","o","u","y"] # ou "aeiouy"
    new = word
    for letter in word:
        if letter in VOWELS:
            new = new.replace(letter,"")
    return(new)

word = input("Donnez un mot à transformer: ")
print(no_vowels(word))
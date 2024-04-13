# Exercice 1
"""
Écrivez une fonction qui prend un mot en argument et qui renvoie le mot 
inversé.
Dans le programme principal, demandez à l'utilisateur de saisir un mot au clavier 
et affichez le mot inverse.
Exemple:
Si le mot entré au clavier est "hologramme", le mot affiché sera "emmargoloh"
"""
def anagramme(word): # Correct
    anagram = ""
    i = -1
    for letter in word:
        pick = word[i]
        anagram = anagram + f"{pick}"
        i -= 1
    return anagram

word = input("Tapez un mot pour en connaître l'annagramme: ")
print(anagramme(word))

# Correction:construction d'un range en rapport au mot

def invert_word(word):
    result = ""
    for i in range(-1,-len(word)-1,-1):
        result = result + word[i]
    return result

user_word = input("Tapez un mot pour en connaître l'annagramme: ") 
print(invert_word(user_word))

# Troisième possibilité

def invert_word(word):
    result = word[-1:-(len(word))+1:-1] # ou [::-1] (premier est 0 de base, le deuxième la logeur du mot) il le fait automatiquement
    return result

user_word = input("Tapez un mot pour en connaître l'annagramme: ") 
print(invert_word(user_word))
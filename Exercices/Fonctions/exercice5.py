# Exercice 5

# Écrivez une fonction qui a pour arguments un mot et une lettre. Cette fonction
# doit retourner le nombre de fois que la lettre apparaît dans le mot.
# Par exemple si le mot est "cacao" et la lettre est "c", la fonction retourne 2.
# Dans le programme principal, écrivez du code qui teste la fonction

def iteration(word,letter):
    count = 0
    for i in word:
        if i == letter:
            count += 1
    print(count)

word = input("Donnez un mot: ")
letter = input("Donnez une lettre pour compter son iteration dans le mot: ")
iteration(word,letter)
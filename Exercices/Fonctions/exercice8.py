# Exercice 8

# Écrivez une fonction qui prend une liste et un caractère comme arguments.
# La fonction va placer le caractère dans la dernière "case" (celle avec l'index le
# plus grand) de la liste qui est rempli par un ".".
# Après coup la fonction retournera la liste.
# Dans votre programme principal, utilisez la fonction pour remplir une liste
# remplie avec 6 ".".
# Faites donc en sorte d'exécuter la fonction tant que la liste n'est pas remplie.
# Après chaque exécution de la fonction, affichez la liste

to_fill = [".",".",".",".",".","."]

def fill_a_list (LIST,a):
    i = -1
    while LIST[i] != a:
        LIST[i] = a
        i -= 1
        print(LIST)

fill_a_list(to_fill,"a")
# Exercice 9

# Écrivez une fonction qui ajoute la TVA à un prix donné en paramètre. La TVA sera
# toujours de 21%.
# Exemple: Si la fonction reçoit 2, elle renverra 2.42 car 2 + 2 * 0.21 = 2.42

def tvac(n):
    n = n + (n*0.21)    
    return n

print(tvac(10))

# 9bis: Écrivez une autre fonction qui reçoit une liste de prix en paramètre et qui
# renvoie la somme des éléments de cette liste auxquels on ajoute la TVA.
# Pour calculer la TVA, utilisez la fonction précédemment créée.

def liste_tvac(LIST):
    somme = sum(LIST)
    tvac = somme + (somme *0.21)
    return tvac

prices = [3.5,1,5.5] # les floats se notent avec un point et non une virgule!!!


print(liste_tvac(prices))
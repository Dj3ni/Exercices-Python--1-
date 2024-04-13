# Exercice 2

# Écrivez une fonction qui affiche l'addition de tous les éléments d'un tableau (une
# liste de liste) passé en paramètre.
# Dans votre programme principal, vous pouvez tester votre fonction avec un
# tableau 3x3 rempli des 9 premiers entiers, la fonction devrait afficher 45.


GRID = [[1,2,3],
        [4,5,6],
        [7,8,9]]

line_lenght = 3
col_lenght = 3


def addition_tableau(GRID):
    somme = 0
    for line in range(line_lenght):
        for column in range(col_lenght):
            somme = int(somme) + int(GRID[line][column])
    print(somme)

addition_tableau(GRID)


# Correction: on n'a pas besoin d'index vu qu'on passe toutes les valeurs donc on utilise pas de range

def sum_list(table):
    sum_numbers = 0
    for line in table:
        for value in line:
            sum_numbers += value
    print(sum_numbers)

sum_list(GRID)

# Autre possibilité: sum() elle va additionner toutes les valeurs de la ligne

def sum_list(table):
    sum_numbers = 0
    for line in table:
        sum_numbers += sum(line)
    print(sum_numbers)

sum_list(GRID)


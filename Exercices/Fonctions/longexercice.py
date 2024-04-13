#  Partie 1

# Ecrivez une fonction qui affiche un tableau à 2 dimensions (une liste de listes,
# comme dans le Puissance 3).
# Le tableau sera passé en argument à votre fonction.
# Vous pouvez considérer que les tableaux reçus ne seront que des tableaux de
# nombres entiers (pas besoin de gérer les autres cas).

def check_table_lenght(grid,n):
    if len(grid) > n:
        return False
    elif len(grid) < n:
        for line in grid:
            if len(line) > n:
                return False
    return True

def display_table(grid):
    if check_table_lenght(grid,9) == True:
        for line in range(len(grid)):
            fill = ""
            i = 0
            for col in range(len(grid[line])):
                if grid[line][col] < 10:
                    fill = str(fill) + str(grid[line][col]) +" " + " "
                else:
                    fill = str(fill) + str(grid[line][col]) +" " 
                
            print(fill)
    else:
        print("Tableau trop grand!")

table = [   [1,2,3,4,5],
            [6,7,8,9,10],
            [11,12,13,14,15],
        ]

display_table(table)

# Partie 2

# Ecrivez une fonction qui renvoie un tableau à 2 dimensions (une liste de liste).
# La fonction recevra un nombre de lignes et de colonnes en paramètre et
# renverra un tableau de nombres entiers allant de 1 à N.
# N représente le nombre de lignes multiplié par le nombre de colonnes.
from random import randint

def empty_grid(n_line,n_col):
    grid =[[0]* n_col for i in range(n_line)]
    return grid
# display_table(empty_grid(2,3)) #test fonction

def grid_construct(n_line,n_col):
    n = n_line * n_col
    grid = []
    line_fill = ""
    y = 1
    z = n_col

    for column in range(n_line):
        line_fill = list(range(y,z+1))
        grid.append(line_fill)
        y += n_col
        z+= n_col

    return grid

# print(grid_construct(4,4)) # pour debug

# display_table(grid_construct(4,4)) #test fonction

# Partie 3
# Ecrivez une fonction similaire à celle de la partie 2, qui renvoie un tableau à 2
# dimensions (de nouveau une liste de listes).
# La fonction aura les même arguments, mais remplira le tableau de manière
# différente
# ● Les entiers dans le tableau renvoyé doivent êtres rangés en "serpent" de
# gauche à droite sur une ligne et de droite à gauche sur la suivante, et ainsi
# de suite

def snake_grid(n_line,n_col):
    n = n_line * n_col
    grid = []
    line_fill = ""
    y = 1
    z = n_col
    for line in range(0,n_line):
        if line in range(0,n_line,2):
            line_fill = list(range(y,z+1))
            grid.append(line_fill)
            y += n_col
            z += n_col
        else:
            line_fill = list(range(z,y-1,-1))
            grid.append(line_fill)
            y += n_col
            z += n_col
    return grid

print(snake_grid(4,4))
display_table(snake_grid(4,4)) # test fonction

# fonction marche mais pas 1/2


def snail_grid(n_line, n_col): # inspiré de https://codes-sources.commentcamarche.net/source/31776-algo-simple-remplissage-d-un-tableau-en-spirale
    result = []
    for i in range (n_line):
        result.append([])
        for j in range (n_col):
            result[-1].append(0)
    
    x = 0
    y = 0
    line_up = 0
    line_down = 0
    left_side = 0
    right_side = 0
    direction = "right"

    for i in range(n_line, n_col): #gestion des absicces et ordonnées
        if n_line - x -right_side > 1 and direction == "right":
            result[x][y] = i
            x += 1
        elif (direction == "down" and y < n_col - line_down):
            result[x][y] = i
            y += 1
        elif (direction == "left" and x >= left_side):
            result[x][y] = i
            x -= 1
        elif direction == "up" and y >= line_up:
            result[x][y] = i
            y -= 1
        else: # changement de direction
            if direction == "right":
                direction =="down"
                right_side += 1
                result[x][y] = i
                y +=1
            elif direction == "down":
                direction == "left"
                right_side += 1
                result[x-1][y-1] = i
                y = n_col - line_down -1
                x = left_side - right_side -2
            elif direction == "left":
                direction == "up"
                line_down += 1
                y = n_col - line_down -1
                x = left_side
                result[x][y] = i
                y -= 1
            elif direction == 'up':
                direction == "right"
                left_side += 1
                result[x+1][y+1] = i
                x += 2
                y = line_up
    fill = ""
    for j in range(n_col):
        for k in range(n_line):
            num = str(result[k][j])
            if len(num) < len(str(n_line*n_col-1)):
                num = (len(str(n_line*n_col-1)) - len(num)) * " " + num
            fill += num + " "
    print (fill)

    return result

display_table(snail_grid(5,5))


# print(snail(table))

"""
Programme principal

"""

n_line = int(input("Combien de lignes doit avoir le tableau? "))
n_col = int (input("Combien de colonnes doit avoir le tableau? "))

sorting = input("Comment souhaitez trier les valeurs dans le tableau? 'S', 'N' ou 'E'? ")

while sorting != "S" and sorting != "N" and sorting != "E":
    sorting = input("Comment souhaitez trier les valeurs dans le tableau? 'S', 'N' ou 'E? ")
else:
    if sorting == "N":
        display_table(grid_construct(n_line,n_col))
    elif sorting == "S":
        display_table(snake_grid(n_line,n_col))
#     # else:
#     #     display_table(snail_grid_construct(n_line,n_col))


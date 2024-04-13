TOKEN_1 = "X"
TOKEN_2 = "O"

"""
Fonctions

"""

def get_token(player):
    if player == 1:
        return TOKEN_1
    return TOKEN_2

# affichage grille

def display_grid(grid):
    for line in range(len(grid)):
        text = ""
        for col in range(len(grid[line])):
            text = text + " " + grid[line][col]
        print(str(line) + text)

    text = ""
    for last_line in range(len(grid[0])):
        text = text + f" {last_line}"
    print(f" {text}")


def display_grid2(grid):
    i = 0
    for line in grid:
        text = ""
        for element in line:
            text = text + " " + element
        print(str(i) + text)
        i = i + 1

    text = ""
    i = 0
    for last_line in grid[0]:
        text = text + f" {i}"
        i = i + 1
    print(f" {text}")

#Tour de jeu

def play(grid, column, player):
    # trouver pour la colonne passeée en paramètre la première ligne vide
    line = 4

    while grid[line][column] != '.' and line > -1:
        line -= 1
    # placer le bon token dans la colonne à la ligne trouvée. 
    if line > -1:
        grid[line][column] = get_token(player)

    return grid

# Conditions de victoire

def check_vertical(grid, column, line):
    if line >= 3:
        return False
    
    if grid[line][column] == grid[line + 1][column]:
        if grid[line][column] == grid[line + 2][column]:
            return True

    return False

def check_horizontal(grid, column, line):
    if column <= 2:
        # Si les jetons à droite sont identiques
        if grid[line][column] == grid[line][column +1]:
            if grid[line][column] == grid[line][column +2]:
                return True
    elif column >=2:
        # Si les jetons à gauche sont identiques
        if grid[line][column] == grid[line][column -1]:
            if grid[line][column] == grid[line][column -2]:
                return True
    elif column >=1 and column <=3:
        # Si le jeton à gauche et à droite sont identiques
        if grid[line][column] == grid[line][column -1]:
            if grid[line][column] == grid[line][column +1]:
                return True
    return False

def check_diagonale(grid, column, line):
    if column >= 0 and line <= 2:
        # Diagonale vers le bas droite
        if grid[line][column] == grid[line-1][column +1]:
            if grid[line][column] == grid[line-2][column +2]:
                return True
    elif column >= 0 and line <= 4:        
        # Diagonale vers le haut droite
        if grid[line][column] == grid[line+1][column +1]:
            if grid[line][column] == grid[line+2][column -2]:
                return True
            
    elif column >= 2 and line >= 2:
        # Diagonale vers le haut gauche
        if grid[line][column] == grid[line+1][column -1]:
            if grid[line][column] == grid[line+2][column -2]:
                return True

    elif column >= 2 and line <= 2:        
        # Diagonale vers le bas droite
        if grid[line][column] == grid[line-1][column -1]:
            if grid[line][column] == grid[line-2][column -2]:
                return True
            
    elif column >= 1 and line <=3:
        # Diagonale haut et bas gauche
        if grid[line][column] == grid[line+1][column -1]:
            if grid[line][column] == grid[line-1][column +1]:
                return True

    elif column >= 1 and line <=3:    
        # Diagonale haut et bas droite
        if grid[line][column] == grid[line+1][column +1]:
            if grid[line][column] == grid[line-1][column-1]:
                return True
    return False

def check_winner(grid, column, current_player):
    line = 0
    while grid[line][column] == '.':
        line += 1
    if check_vertical(grid,column,line):
        return True
    elif check_horizontal(grid,column,line):
        return True
    # elif check_diagonale(grid,column,line):
    #     return True

    return False

# Remplissage grille

def grid_full(grid, column,line):
    if grid[line[0]][column]!= ".":
        return True
    return False




"""
Programme principal

"""
tableau = [
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."],
]

winner = None
player = 1

while winner == None:
    display_grid(tableau)

    column = input(f"Joueur {get_token(player)}, où va tu jouer? ")
    column = int(column)

    play(tableau, column, player)

    if check_winner(tableau, column, player):
        winner = player
    else:
        if player == 1:
            player = 2
        else:
            player = 1
    
    # if grid_full(tableau,column,0) == True:
    #     winner == 0

if winner == 0:
    print("Dommage, réessayez!")

else:
    print(f"Bravo! le gagnant est le joueur {winner}!")
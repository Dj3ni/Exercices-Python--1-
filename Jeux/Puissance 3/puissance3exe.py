# """ Nous allons programmer la version pour deux joueurs humains (pas de joueur contrôlé par l'ordinateur donc).
# Chaque joueur va choisir à tour de rôle une colonne pour mettre son jeton. 
# Le jeton va "tomber" jusqu'à la case vide la plus basse de cette colonne.
# Ensuite le jeu vérifiera si il y a un alignement de 3 qui s'est créé. Si oui, le joueur à gagné, sinon c'est le tour du joueur suivant.
# Si, après un coup non-gagnant, le tableau est rempli, il est vidé avant de passer au joueur suivant. """

# # Exemple

# # GRID= [ ["a","b","c"],
# #         ["d","e","f"],
# #         ["g","h","i"]]

# # for line in range(3): 
# #     txt = ""
# #     for column in range(3):
# #         txt = txt + GRID[line][column]
# #     print(txt + "\n")

# # Exercice 1 : correct

# # GRID = [[1,2,3,4],
# #         [5,6,7,8],
# #         [9,10,11,12]]

# # for line in range(3):#on peut mettre range(len(GRID)) pour si jms il y a des changements
# #     txt = ""
# #     for column in range(4):#on peut mettre range(len(GRID[line]))
# #         txt = txt + str(GRID[line][column]/2) + " "
# #     print(f" {txt}")

# # autre manière:
# # for line in GRID:
# #     txt=""
# #     for value in line:
# #         txt += f"{value/2}"
# #     print(txt)

# # Exercices fonctions
# # 1

from random import randint

# # def bonjour():
# #     hello = ["Bonjour","Hello", "Ola","Ciao"]
# #     index = randint(0,len(hello)-1)
# #     coucou = hello[index]
# #     print(coucou)

# # for i in range(100):
# #     bonjour()

# # 2

# # CODELENGTH = 1

# # def mastermind ():
# #     LETTRES = ["a","b","c","d","e"]
# #     selection = randint(0,len(LETTRES)-1)
# #     code = LETTRES[selection]        
# #     return code

# # CODE = []
# # for i in range(5):
# #     txt =""
# #     result = txt + mastermind()
# #     CODE.append(result)
    
# # print(CODE) 

# """
# Correction:

# def random_letter():
#     possibilities = ["a","b","c","d","e"]
#     index = randint(0,len(possibilities)-1)
#     letter = possibilities[index]
#     return letter

# word = ""
# for _ in range(5):
#     word += random_letter()
# print(word)

# """

# 3: correct

# def suite_lettres(number_letters):
#     LETTERS = ["a","h","k","o","n","s","t"]
#     word = ""
#     for i in range(number_letters):
#         selection = randint(0,len(LETTERS)-1)
#         pick = LETTERS[selection]
#         word = word + f"{pick}"
#     return word

# number_letters = int(input("Combien de lettres: "))

# print(suite_lettres(number_letters))

# # Cutting the mammoth

GRID = [["0",".",".",".",".","."],
        ["1",".",".",".",".","."],
        ["2",".",".",".",".","."],
        ["3",".",".",".",".","."],
        ["4",".",".",".",".","."],
        [" ","0","1","2","3","4"],
        ]
Col_size = 6

def affiche_GRID():
    for line in GRID:
        txt = ""
        for value in line:
            txt += f"{value}" + " "
        print (f"{txt}" "\n")

# affiche_GRID() # pas besoin de print vu que la fonction contient un print!!!

winner = None
player = 0
token1 ="o"
token2 = "x"

def player_shot(player): # quel jeton doit être affiché
    if player == 1:
        return token1
    else:
        return token2
# print(player_shot(player2)) : controle debug

def new_turn(GRID, player, col): # encoder un nouveau tour (code Mélusine)
    for line in range(Col_size):
        if GRID[line][col+1] == ".": 
            if GRID[line+1][col+1] != ".":
                GRID[line][col+1] = player_shot(player)
                break
    return affiche_GRID()

# new_turn(GRID, 1, 1) # controle debug attention pas de print!!!


def player_turn(): # encoder le coup du joueur dans la grille
    player = 0
    if player == 0:
        player +=1
        if player == 1:
            player -= 1
    return player

# Programme principal

while winner == None:
    player_turn()
    col = int(input("Dans quelle colonne souhaitez vous mettre le jeton? "))
    new_turn(GRID,player,col)





#  Commencer par faire une simulation avant d'écrire la fonction

# 1 :commencer la fonction

def affiche_tableau(tableau):
    print(tableau)

table = [   [1,2,3,4,5],
            [6,7,8,9,10],
            [11,12,13,14,15],
        ]
print(table)

# 2: boucler

def affiche_tableau(tableau):
    for line in range(len(tableau)):
        txt= ""
        for col in range (len(tableau[line])):
            txt = txt + str(tableau[line][col]) + " "
        print(txt)

affiche_tableau(table)

# 3: gérer les espaces

def affiche_tableau(tableau):
    for line in range(len(tableau)):
        txt= ""
        for col in range (len(tableau[line])):
            if tableau[line][col] < 10:
                txt = txt + str(tableau[line][col]) + " " + " "
            else:
                txt = txt + str(tableau[line][col]) + " " 
        print(txt)

affiche_tableau(table)
""""
Même fonction, sans index, plus adaptée à Python

"""
def affiche_tableau(tableau):
    for line in tableau:
        txt= ""
        for elm in line:
            if elm < 10:
                txt = txt + str(elm) + " " + " "
            else:
                txt = txt + str(elm) + " " 
        print(txt)

# amélioration: si des parties sont redondantes, penser à épurer le code

def affiche_tableau(tableau):
    for line in tableau:
        txt= ""
        for elm in line:
            txt += str(elm) + " "
            if elm < 10:
                txt += " "
        print(txt)

# condition longueur tableau, si tout dans la meme fonction:

def affiche_tableau(tableau):
    
    if len(tableau) < 10:
        if len(tableau[0]) <10:
            for line in tableau:
                txt= ""
                for elm in line:
                    txt += str(elm) + " "
                    if elm < 10:
                        txt += " "
                print(txt)
    else: 
        print("Tableau trop grand")

# avec une deuxième fonction, hardcodé pour éviter la multiplication des exemples:

def tableau_valide(tableau):
    if len(tableau) > 9:
        return False
    for line in tableau:
        if len(line) > 9:
            return False
    return True

def affiche_tableau(tableau):
    if tableau_valide(tableau): # == True pas utile car le tableau ne renverra qqch que si True!
            for line in tableau:
                txt= ""
                for elm in line:
                    txt += str(elm) + " "
                    if elm < 10:
                        txt += " "
                print(txt)
    else:
        print("Tableau trop grand")

"""
Partie 2: 

"""
#  Première approche:partir des éléments à remplir et travailler avec les index pour

def renvoie_tableau(n_lines, n_cols):
    # n = n_lines * n_cols: inutile dans ce cas-ci
    result = []
    elem = 1

    for i in range (n_lines):
        line = []
        for j in range(n_cols):
            line.append(elem)
            elem += 1
        result.append(line)
    return result

affiche_tableau(renvoie_tableau(5,6))

# autre façon:
def renvoie_tableau(n_lines, n_cols):
    # n = n_lines * n_cols # inutile dans ce cas-ci
    result = []
    elem = 1

    for i in range (n_lines):
        line = []
        for j in range(n_cols):
            line.append(i*n_cols +j+1) # on augmente du nombre de colonnes
        result.append(line)
    return result

"""
Partie 3
"""
#  utilisation d'un insert(): on met les éléments au début
# il y a 2 possibilités: une variable qui agit comme compteur True /False
def renvoie_tableau_serpent(n_lines, n_cols):
    result = []
    elem = 1
    en_arriere = False

    for i in range(n_lines):
        line = []
        for j in range(n_cols):
            if en_arriere:# supposé = True
                line.insert(0,elem)
                elem += 1
            else:
                line.append(elem)
                elem += 1
        result.append(line)
        en_arriere = not en_arriere
        # Cette ligne remplace la condition ci-dessous
        # if en_arriere:
        #     en_arriere = not True
        # else:
        #     en_arriere = True
    return result

table = renvoie_tableau_serpent(5,6)
affiche_tableau(renvoie_tableau_serpent(5,6))

# Modulo:
def renvoie_tableau_serpent(n_lines, n_cols):
    result = []
    elem = 1
    for i in range(n_lines):
        line = []
        for j in range(n_cols):
            if i % 2 == 1: #ligne impaire
                line.insert(0,elem)
                elem += 1
            else:
                line.append(elem)
                elem += 1
        result.append(line)
    return result
affiche_tableau(renvoie_tableau_serpent(5,6))

"""
Partie 4

"""
# Travailler en 2 temps!!

# 1: comment faire juste le contour? (correspond à 75 % de l'exo)
#  Travailler avec des index!

def renvoie_tableau_escargot(n_lines, n_cols):
    # 1: on crée un tableau "vide"
    result = []
    for i in range(n_cols):
        line = []
        for j in range (n_cols):
            line.append(0)
        result.append(line)
            
    elem = 1
    # 2: remplissage des bords extérieurs du tableau
    
    # remplissage de la ligne 0
    for c in range(n_cols):
        result[0][c] = elem 
        elem += 1
    
    # remplissage dernière colonne 
    for l in range(1,n_lines):
        result[l][n_cols-1] = elem
        elem += 1

    # remplissage ligne du bas (-2 car -1 est déjà rempli!)
    for c in range (n_cols-2,-1,-1):
        result[n_lines -1][c] = elem
        elem += 1
    
    # remplissage ligne de gauche
    for l in range( n_lines-2,0,-1):
        result[l][0] = elem
        elem += 1
    return result

affiche_tableau(renvoie_tableau_escargot(5,5))

# 2: une fois que cela est fait, modifier ce code et le généraliser avec des variables

def renvoie_tableau_escargot(n_lines, n_cols):
    # 1: on crée un tableau "vide"
    result = []
    for i in range(n_cols):
        line = []
        for j in range (n_cols):
            line.append(0)
        result.append(line)
    
    #  variables      
    start_line = 0
    end_line = n_lines -1
    start_col = 0
    end_col = n_cols -1
    elem = 1

    # remplissage vers droite
    for c in range(start_col,end_col+1):
        result[start_line][c] = elem 
        elem += 1
    
    # remplissage vers le bas
    for l in range(start_line+1,end_line +1):
        result[l][end_col] = elem
        elem += 1

    # remplissage vers la gauche
    for c in range (end_col-1,start_col-1,-1):
        result[end_line][c] = elem
        elem += 1
    
    # remplissage vers le haut
    for l in range(end_line-1,start_line,-1):
        result[l][start_col] = elem
        elem += 1

    return result


affiche_tableau(renvoie_tableau_escargot(5,5))

# 3: Utiliser une boucle pour que la fonction s'adapte à n'imprte quelle dimension de tableau

def renvoie_tableau_escargot(n_lines, n_cols):
    # 1: on crée un tableau "vide"
    result = []
    for i in range(n_lines ):
        line = []
        for j in range (n_cols):
            line.append(0)
        result.append(line)
    
    #  variables      
    start_line = 0
    end_line = n_lines -1
    start_col = 0
    end_col = n_cols -1 
    elem = 1

    while start_col <= end_col and start_line <= end_line:# on travaille avec les colonnes et les lignes
        # while elem <= (n_lines*n_cols): on travaille avec le nbr elem du tableau

        # remplissage vers droite
        for c in range(start_col,end_col+1):
            result[start_line][c] = elem 
            elem += 1
        # Dans le cas du 1er while :evite que dans le cas des lignes impaires /colonnes paires il fasse un tour de trop
        if elem > (n_lines * n_cols):
            break

        # remplissage vers le bas
        for l in range(start_line+1,end_line +1):
            print(l)
            result[l][end_col] = elem
            elem += 1
        # Dans le cas du deuxième while, quand lignes plus grandes que colonnes
        if elem > (n_lines * n_cols):
            break

        # remplissage vers la gauche
        for c in range (end_col-1,start_col-1,-1):
            result[end_line][c] = elem
            elem += 1

        # remplissage vers le haut
        for l in range(end_line-1,start_line,-1):
            result[l][start_col] = elem
            elem += 1
        
        start_line += 1
        end_line -= 1
        start_col += 1
        end_col -= 1
    return result

affiche_tableau(renvoie_tableau_escargot(9,5))

"""
Programme principal

"""
# Première façon de faire

n_line = int(input("Combien de lignes doit avoir le tableau? "))
n_col = int (input("Combien de colonnes doit avoir le tableau? "))

sorting = input("Comment souhaitez trier les valeurs dans le tableau? 'S', 'N' ou 'E'? ")

while sorting != "S" and sorting != "N" and sorting != "E":
    sorting = input("Comment souhaitez trier les valeurs dans le tableau? 'S', 'N' ou 'E? ")
else:
    if sorting == "N":
        affiche_tableau(renvoie_tableau(n_line,n_col))
    elif sorting == "S":
        affiche_tableau(renvoie_tableau_serpent(n_line,n_col))
    else:
        affiche_tableau(renvoie_tableau_escargot(n_line,n_col))

# Deuxième façon de faire

n_line = int(input("Combien de lignes doit avoir le tableau? "))
n_col = int (input("Combien de colonnes doit avoir le tableau? "))

sorting = None

while sorting not in ["N","S","E"]:
    sorting = input("Comment souhaitez trier les valeurs dans le tableau? 'S', 'N' ou 'E? ")
else:
    if sorting == "N":
        tab = renvoie_tableau(n_line,n_col)
    elif sorting == "S":
        tab = renvoie_tableau_serpent(n_line,n_col)
    else:
        tab = renvoie_tableau_escargot(n_line,n_col)

affiche_tableau(tab)
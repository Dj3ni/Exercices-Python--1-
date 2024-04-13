"""
Exercice 1: Créez un petit programme qui contient un dictionnaire très simple contenant les 
pseudos de joueurs en clés et leurs meilleurs scores en valeurs :
scores = {"MokoSempai": 16, "Grungi": 30, "Elocin03": 56}
Faite en sorte que le programme propose au joueur d'entrer son pseudo, puis 
d'entrer son score. Ces deux élément doivent être entré dans le dictionnaire.
Ensuite afficher le score de "Elocin03" ainsi que le score du nouveau pseudo 
entré. 

"""

# scores = {"MokoSempai": 16, "Grungi": 30, "Elocin03": 56}

# pseudo = input("Quel est votre pseudo?: ")
# new_score = int(input("Quel est votre meilleur score? "))

# scores[pseudo] = new_score

# print(f"Elocin03 : {scores["Elocin03"]}")
# print(f"{pseudo} : {new_score}")

"""
Exercice 2: En reprenant notre exercice précédent, au lieu d'afficher seulement deux 
pseudos, vous allez plutôt afficher tous les pseudos et leurs scores associés.

"""
# for pseudo,score in scores.items():
#     print(f"{pseudo}: {score}")

"""
Exercice 3: Créez un programme qui utilise un dictionnaire pour stocker le rang des joueurs 
dans un club.
● Marie: 1
● Bernard : 4
● François: 2
● Thomas: 12
● Hila: 15
Créez un dictionnaire incluant ces données et sur base de celui-ci, déterminez le 
niveau (rang) moyen des membres du club.

"""
players = {}

def add_player(name, rank):
    players[name] = rank

name = None

# while name != 'stop':
#     name = input("Quel est le pseudo? ")
    # if name == stop:
        # break
#     rank = int(input("Quel est votre ranking? "))
#     add_player(name,rank)
# print(players)

players = {
    "Marie": 1,
    "Bernard" : 4,
    "François": 2,
    "Thomas": 12,
    "Hila": 15
}

print(players)
somme = 0
nbr_joueurs = 0

for name,rank in players.items():
    somme += rank
    nbr_joueurs += 1
    print(somme)

moyenne = somme / nbr_joueurs
print(moyenne)

#  autre possibilité:

average = sum(players.values())
average /= len(players)
print (f"Moyenne des rangs du club: {average}")

# Bonus: calculer la médiane (valeur du milieu)
# Pour cela on a besoin d'ordonner les valeurs

rank_values = list(players.values())
rank_values.sort()
print(rank_values)


n = len(rank_values)//2 # division entière

if len(rank_values) % 2 == 0: #si nombre de résultats pair
    median = rank_values [n-1:n+1] #on pren une tranche
else:
    median = rank_values[n]

print(f"Notre médiane est de : {median}")

"""
Exercice 4: Dans l'exercice précédent, avant de calculer la moyenne, retirez du dictionnaire 
les membres qui ont un rang supérieur ou égal à 10. Ensuite, faites le calcul de la 
moyenne.

"""

# Correction: attention, dans l'énoncé, il faut SUPPRIMER les éléments de la liste

somme = 0
nbr_joueurs = 0

for name,rank in players.items():
    if rank < 10: 
        somme += rank
        nbr_joueurs += 1
    print(somme)#debug

moyenne = somme / nbr_joueurs
print(moyenne)

# attendu, 1 ère façon:

to_remove = []
#  supprimer les rangs supérieur à 10:
for name, rank in players.items():
    if rank >=10:
        to_remove.append(name)

for name in to_remove:
    players.pop(name)

print(players)

# deuxième possibilité: utiliser un clonage de dictionnaire

players = {
    "Marie": 1,
    "Bernard" : 4,
    "François": 2,
    "Thomas": 12,
    "Hila": 15
}

clone = {}
clone.update(players)

for name, rank in clone.items():
    if rank >=10:
        players.pop(name)

# Tris: on bosse sur une liste temporaire/ tuple est possible aussi

players = {
    "Marie": 1,
    "Bernard" : 4,
    "François": 2,
    "Thomas": 12,
    "Hila": 15
}

players= {name:rank for name, rank in players.items() if rank < 10}

for name, rank in list(players.items()):
    if rank >=10:
        players.pop(name)






# Exercice 1

players = {}

def add_player(pseudo,score):
    players[pseudo] = score

""""""
pseudo = input("Quel est votre pseudo?: ")
score = int(input("Quel est votre meilleur score? "))

add_player(pseudo,score)

print(players)

"""Correction"""
scores = {"MokoSempai": 16, "Grungi": 30, "Elocin03": 56}

pseudo = input("Quel est votre pseudo?: ")
new_score = int(input("Quel est votre meilleur score? "))

scores[pseudo] = new_score

print(f"Elocin03 : {scores["Elocin03"]}")
print(f"{pseudo} : {new_score}")

"""Boucles dans dicos"""
for elem in scores:
    print(elem)

for elem in scores.items():
    print(elem)

for elem in scores.items():
    pseudo,score = elem
    print(pseudo)

# autre manière de faire, sucre syntaxique :
for pseudo,score in scores.items():
    print(f"{pseudo}: {score}")











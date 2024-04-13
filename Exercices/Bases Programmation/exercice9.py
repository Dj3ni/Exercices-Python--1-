from random import randint

# Exercice 9

# Écrivez un programme qui va générer trois nombres aléatoirement (entre 1 et 
# 6).
# Ensuite le programme va afficher les trois nombres
# Si les trois nombres ne sont pas identiques, il recommence.

tirage1 = randint(1,6)
tirage2 = randint(1,6)
tirage3 = randint(1,6)

print(tirage1, tirage2, tirage3)

while tirage1 != tirage2 or tirage2 != tirage3:
    tirage2 = randint(1,6)
    tirage3 = randint(1,6)
print("Le numero gagnant est le: " + str(tirage1) + str(tirage2) + str(tirage3))

# correct( si a==b et b==c, du coup a==c, pas besoin de le noter!)
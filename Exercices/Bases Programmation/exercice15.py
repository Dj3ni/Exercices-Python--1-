#Exercice 15

# Écrivez un script qui demande à l'utilisateur un nombre entier entre 1 et 100,
# redemandez tant que l'utilisateur ne donne pas un entier entre 1 et 100.
# Ensuite affichez la somme des chiffres de 1 à l'entier donné par l'utilisateur.
# Si l'utilisateur vous donne 10, la somme affichée sera 55 car 55 est la somme des
# entiers de 1 à 10.


proposal = int(input("Veuillez entrer un nombre entre 1 et 100: "))

while 1> proposal or proposal> 100: # not (1<=proposal<=100): correct aussi mais attention que en Python!
    proposal = int(input("Veuillez entrer un nombre entre 1 et 100: "))

value = range(proposal+1)
somme = sum(value)

print(somme)

# Correction:

proposal = int(input("Veuillez entrer un nombre entre 1 et 100: "))

while 1> proposal or proposal> 100: # not (1<=proposal<=100): correct aussi mais attention que en Python!
    proposal = int(input("Veuillez entrer un nombre entre 1 et 100: "))

somme = 0
i= 1

while i <= proposal:
    somme = somme + i
    i = i+1

print(somme)

# Deuxieme manière: descendante:

while proposal >0:
    somme = somme + proposal
    proposal = proposal -1

print(somme)

#Troisième proposition
somme =0
for i in range(proposal+1):
    somme = somme +1

# Quatrième proposition:
for i in range(1, proposal+1):
    somme = somme +1


from random import randint

# Partie 1: Correct
couleurs = ["a","b","c","d","e","f"]
code = []

while len(code) != 4:
    selection = randint(0,5)
    code.append(couleurs[selection])       
print(code)


# Partie 2
# Créer une séquence décroissante

sequence = range(10)
liste = list(sequence)
print(liste)

print(list(range(10,0,-1)))

# Partie 3

liste = ["Je","t'","aime","mon","coeur"]

i = 0
for i in liste:
    print(str(i))

# Partie 4
# Remplacer la boucle while par la boucle for

couleurs = ["a","b","c","d","e","f"]
code = [0,0,0,0]

i = 0

for elm in code:
    selection = randint(0,5)
    code[i] = couleurs[selection]
    i = i+1

print(code)

# Partie 5
# Demander au joueur de deviner le code

tentative = input("Devinez le code de 4 couleurs, entrez la première: ")

essais = []

essais.append(tentative)

while len(essais) != 4:
    tentative = input("Entrez la couleur suivante: ")
    essais.append(tentative)

i = 0
for elm in essais:
    key = essais[i]
    essais[i] = couleurs[key-1]
    i = i+1

print(essais)

# list(essai) --> pour quoi faire?

# Partie 6
# Vérifier quelles lettres sont exactes

correct = []
misplaced = []
wrong = 0

i = 0

while correct != code :
    for j in range (len(code)):
        if essais[i] == code [i]:
            correct.append(essais[i])
            print(str(correct[i]) +" : est au bon emplacement")
        for k in range(len(code)):  
            if essais[i] != code [i] and essais[i] not in code:
                wrong = essais[i]
                print(str(wrong) + ": n'est pas dans le code")
                break
            
            elif code[i] not in correct and essais[i] not in correct and essais[i] not in misplaced:
                misplaced.append(essais[i])
                print(str(misplaced[i]) + ": n'est pas au bon emplacement")
                break
        i=i+1            
    tentative = int(input("Veuillez réssayer: "))

print("Bravo, tu as trouvé!: le code était bien " + str(correct))



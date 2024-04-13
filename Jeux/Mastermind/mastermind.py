from random import randint

# Générer un code

couleurs = ["a","b","c","d","e", "f"]
CODELENGTH = 4
code = list(range(CODELENGTH))

i = 0

for elm in code:
    selection = randint(0,CODELENGTH-1)
    code[i] = couleurs[selection]
    i = i+1

print(code) # pour debug, mettre en commentaire quand code ok

# Demander à l'utilisateur de deviner le code

attempt = input("Devinez le code de " + str(CODELENGTH) + " couleurs parmi les lettres 'a,b,c,d,e,f': ")
# print(tentative)
attempt = list(attempt)
# print(attempt)

while len(attempt) != 4:
        attempt = list("Devinez le code de " + str(CODELENGTH) + " couleurs parmi les lettres 'a,b,c,d,e,f': ")

# Confirmer les lettres exactes:

i = 0
correct = []
misplaced = []
wrong = []

for k in range(9): # mettre un nombre x de tentatives
    if attempt != code :
        for i in range(len(code)):
            # Bon index
            if attempt[i] == code [i]: 
                correct.append(i)
            
            # Mauvais index    
            for j in range(len(code)): #boucle coomparaison code

                    #Lettre pas dans le code
                if attempt[i] not in code:
                    wrong.append(i)
                    break
                    #Lettre à la mauvaise place
                elif i not in correct and j not in correct and i not in misplaced:
                    misplaced.append(i)
                    break
        #debug
        # print(correct)                 
        # print(misplaced)
        
        print( "Il y a " + str(len(correct)) + " bonne(s) couleur(s) au bon endroit et " + str(len(misplaced)) + " bonne(s) couleur(s) au mauvais endroit")
        print("Il ne te reste plus que " + str(9-k) + " tentative(s)")

        #Vider les listes pour eviter de garder les infos en mémoire        
        correct = []
        misplaced = []
        wrong = []
        
        attempt = list(input(("Devinez le code de " + str(CODELENGTH) + " couleurs parmi les lettres 'a,b,c,d,e,f': ")))

if attempt == code:
    print("Bravo, tu as trouvé!: le code était bien " + str(code))
else:
    print("Dommage, il ne te reste plus de tentative. Le code était: " + str(code))

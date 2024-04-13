# Exercice 14:
# Écrivez un script qui demande un mot à l'utilisateur.
# Tant que le mot n'est pas "end" le script redemandera un mot à l'utilisateur.
# A chaque fois que le mot commence par "t", affichez-le suivi de "!!!"
# (rappelez-vous que pour lire un seul caractère d'une chaîne de caractères, on
# doit lui donner son index (comme pour les listes)).
# A la fin du script, affichez le nombre de mots entrés par l'utilisateur.

mot = input("Veuillez entrez un mot, tapez 'end'pour terminer: ")

tentatives= []

tentatives.append(mot)

while mot != "end":
    tentatives.append(mot)
    if len(mot)> 0 and mot [0] == "t":# rajouter 1ère partie dans la condition afin d'éviter que le code plante si la châine de caractère est vide)
        print(mot + "!!!")
        mot = input("Veuillez entrez un mot, tapez 'end'pour terminer: ")
        tentatives.append(mot)
    mot = input("Veuillez entrez un mot, tapez 'end'pour terminer: ") # à mettre après condition sinon si le premier mot commence avec un "t" il ne sera pas affiché

print("Vous avez entré " + str(len(tentatives)-1) + " mots.")

# Correction: Pas de liste!!!! Eviter de stocker si c'est pas demandé.

mot = input("Veuillez entrez un mot, tapez 'end'pour terminer: ")
counter = 1

while mot != "end":
    tentatives.append(mot)
    if len(mot)> 0 and mot [0] == "t":# rajouter 1ère partie dans la condition afin d'éviter que le code plante si la châine de caractère est vide)
        print(mot + "!!!")
        mot = input("Veuillez entrez un mot, tapez 'end'pour terminer: ")
        tentatives.append(mot)
    mot = input("Veuillez entrez un mot, tapez 'end'pour terminer: ")
    counter = counter +1

print(counter)
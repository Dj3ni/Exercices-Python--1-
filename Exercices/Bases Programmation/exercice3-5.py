# Exercice 3

    # Récupérez au clavier un nombre et stockez-le dans une variable.
    # Ensuite, affichez cette variable.
    # Rappelez-vous, la saisie clavier revient sous forme de chaîne de caractères.

number = input("Encodez un nombre: ")
number= int(number)
print(number)

# autre moyen de faire
numero = int(input("Encodez un nombre: "))
print(numero)

# Exercice 4 et 5:
    # Si le nombre qui se trouve dans la variable number est plus grand que 10, 
    # affichez la chaîne de caractères “Ce nombre est plus grand que 10”.

if number > 10:
    print("Ce nombre est plus grand que 10.")
else:
    print("Le nombre est plus petit ou égal à 10")

# Exercice D
# Écrivez un programme qui demande à l'utilisateur d'entrer un mot de passe.
# Si le mot de passe n'est pas "Pyth0n", le programme affichera: "Code erroné."

password = input("Entrez votre mot de passe: ")
if password != "Pyth0n":
    print("Code erroné")
    input("Réessayez: ")
    if password == "Pyth0n":
        print ("tu vois quand tu veux")
    else: 
        print("Non vraiment pas.")
else: 
    print("Code valide") 

a = 3
if a < 10:
    print("message 1")
else:
    if a < 100:
        print ("message 2")
    else: 
        print ("message3")




# Exercice 6
#Récupérez un nombre au clavier et stockez-le dans une variable.
# Si le nombre récupéré est plus grand ou égale à 10 affichez “Bravo!”.
# Sinon, si il est plus grand que 8 affichez “Pas mal.”
# Sinon, si le nombre est plus grand que 5 affichez “Mouais, bof”
# Et sinon dans les autres cas affichez “Pas terrible” 

number = input("Entrez un nombre: ")
number= int(number)

if number >= 10:
    print("Bravo!")
elif 8 <= number <10:
    print("Pas mal.")
elif 8 <number>= 5:
    print("Mouais, bof.")
else:
    print("Pas terrible.")

# correct

# Exercice 7
    # Écrivez un script qui demande à l'utilisateur un nombre (entre 1 et 10).
# Tant qu'il ne rentre pas un chiffre entre 1 et 10, le programme demande à 
# nouveau à l'utilisateur un nombre (entre 1 et 10).

number = int(input("Choisis un nombre entre 1 et 10: "))

while 1> number or number >10:
    number = int(input("Choisis un nombre entre 1 et 10: "))
print("votre nombre est le: " + str(number))

# correct

# Exercice 8
    # Écrivez un script qui demande à l'utilisateur un mot de passe.
    # Si le mot de passe entré n'est pas "Pyth0n" le programme demande à nouveau 
    # le mot de passe.
    # Quand le mot de passe est bon, le programme affiche "Mot de passe valide."
    # Après 3 tentatives infructueuses, le programme affiche "Mot de passe 
    # incorrect."

password= input("Entrez votre mot de passe: ")

essai= 1
# On a dejà fait un essai donc pas essai = 0 !

while password != "Pyth0n" and essai < 3:
    password = input("Mot de passe incorrect, veuillez réessayer: ")
    essai = essai +1

if password == "Pyth0n":
    print("Mot de passe validé")
else:
    print("mot de passe incorrect")

# correct
# Constante: on met tout en MAJUSCULE
# PASSWORD = "Pyth0n" du coup PASSWORD va remplacer "Python" partout :comme ça si changement, on change à un seul endroit    
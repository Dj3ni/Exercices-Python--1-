# Partie 1
user_number = input("Donne un nombre de 1 à 10: ")
user_number =int(user_number)
print("Nombre récupéré: "+ str(user_number))

# Partie 2

from random import randint

guessing= randint(1,10)

user_number = input("Donne un nombre de 1 à 10: ")
user_number = int(user_number)

if user_number > guessing:
    print("Trop haut")    
elif user_number < guessing:
    print("Trop bas")    
else:
    print("Gagné!")

# Partie 3

guessing= randint(1,10)
user_number = None

while user_number != guessing:
    user_number = int(input("Donne un nombre de 1 à 10: "))
    
    if user_number > guessing:
        print("Trop haut")
        # user_number= int(input("Réessaye: "))
    else:
        print("Trop bas")
        # user_number= int(input("Réessaye: "))
print("Bravo tu as trouvé!")


# Partie 4

guessing= randint(1,10)

user_number = input("Donne un nombre de 1 à 10: ")
user_number = int(user_number)

i = 0
# i est une variable, on peut mettre "essai"
while user_number != guessing and i < 3:
    
    if user_number > guessing:
        print("Trop haut")
        user_number= int(input("Réessaye: "))
        i = i+1
    elif user_number < guessing:
        print("Trop bas")
        user_number= int(input("Réessaye: "))
        i = i+1

if user_number == guessing:
    print("Bravo tu as trouvé!")
else:
    print("Pas de chance! Le nombre était " + str(guessing))



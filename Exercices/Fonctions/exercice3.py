# Exercice 3 et 3 bis

# Écrivez une fonction affiche la table de multiplication de 7 (les 10 premiers
# multiples de 7) de la manière suivante
# 1x7=7
# 2x7=14
# 3X7=21

n = 0

def tables_multiplication(n):
    multiple = 0
    while multiple <= 10:
        product = multiple * n
        print( f"{multiple} x {n} = {product}")
        multiple += 1

tables_multiplication(7)

# Correction:

def multiplication_table(number):
    for n in range(1,10):
        print(f"{n}x{number} = {n*number}")

multiplication_table()
# On veut lancer un dé 6 face 10* et concerver le résultat

from random import randint

result = []

for i in range(10):
    result.append(randint(1,6))

print(result)
if 6 not in result:
    print("Aucun 6")

# Break
i =0
while i < 100:
    print(i)
    i = i+1
    if i == 10:
        break

print("stop")

for counter in range(3):
    i = 0
    while i < 100:
        print(i)
        i = i+1
        if i == 3:
            break
    break
print("stop")
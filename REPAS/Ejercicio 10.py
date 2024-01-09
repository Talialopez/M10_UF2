import random

secreto = random.randrange(1, 100)
count = 0

numero = int(input("Adivina el número: "))

while numero != secreto:
    if numero > secreto:
        print("El número es más pequeño")   
    elif numero < secreto:
        print("El número es más grande")
    
    numero = int(input("Adivina el número: "))
    count += 1

print("¡Felicidades, este es el número!", secreto)
print("Intentos realizados:", count)
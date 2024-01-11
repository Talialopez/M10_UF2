valor = int(input("Introduce un numero entre 10 y 100: "))

if 10 <= valor <= 100:
    numeros_tupla = tuple(range(1, valor + 1))

    print("Tupla:", numeros_tupla)
else:
    print("El numero no corresponde al rango indicado")
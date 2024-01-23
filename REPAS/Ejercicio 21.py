valor = input("Inserta 10 numeros separados por espacio: ")

numeros = []
lista_numeros = valor.split()

for cadena in lista_numeros:
    numero = int(cadena)
    numeros.append(numero)

suma = 0
for numero in numeros:
    suma += numero

media = suma / len(numeros)

numeros.append(suma)
numeros.append(media)

print(numeros)
print(suma)
print(media)




numeros = []

valor = ""

while(valor != 0):
    valor = int(input("Introduce un número, para salir 0: "))    
    numeros.append(valor)

tupla = tuple(numeros)
orden = tuple(sorted(tupla))

print("Tupla ordenada:", orden)
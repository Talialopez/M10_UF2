
numeros = []

for i in range(10):
    valor = int(input("Introduce un número : "))    
    numeros.append(valor)

tupla = tuple(numeros)
orden = tuple(sorted(tupla))

print("Tupla ordenada:", orden)





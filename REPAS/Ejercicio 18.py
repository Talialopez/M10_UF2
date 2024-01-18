primerapalabra = input("Introduce la primera palabra: ")
segundapalabra = input("Introduce la segunda palabra: ")

tupla = (primerapalabra, segundapalabra)

letras = {}

for palabra in tupla:
    for letra in palabra:
        if letra in letras:
            letras[letra] += 1
        else:
            letras[letra] = 1

print("Frecuencia de las letras:")
for letra, cantidad in letras.items():
    print(f"{letra}: {cantidad} veces")


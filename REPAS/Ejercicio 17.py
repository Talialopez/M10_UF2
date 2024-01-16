valor = input("Introduce una frase: ")

espacio = valor.replace(" ", "")
duplicado = ""

for char in espacio:
    if char not in duplicado:
        duplicado += char

final = tuple(duplicado)
print(tuple)

print(final)

valor = input("Introduce una frase: ")

palabras = []

for char in valor:
    if char != " ":
        palabras.append(char)

print(palabras)

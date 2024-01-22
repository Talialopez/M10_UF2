contactos = {}

while True:
    valor = input("Introduce un nombre o la palabra fin para salir: ")

    if valor.lower() == 'fin':
        break

    if valor in contactos:
        print(f"El nombre '{valor}' ya existe.")
    else:
        while True:
            edad_str = input(f"Introduce edad de {valor}: ")
            if edad_str.isdigit():
                edad = int(edad_str)
                contactos[valor] = edad
                break
            else:
                print("No es una edad válida")

print("Contactos:")
for valor, edad in contactos.items():
    print(f"{valor}: {edad} años")

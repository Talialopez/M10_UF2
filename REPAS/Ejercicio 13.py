valor = int(input("Introduce un numero del 1 al 10: "))

count = 1

if 1 <= valor <= 10:
    while count <= 10:
        resultado = valor * count
        print(resultado)
        count += 1

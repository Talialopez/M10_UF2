meses = (
    "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
)

while True:
    valor = int(input("Introduce un numero entre 0 y 12 (0 para finalizar): "))

    if valor == 0:
        print("Programa finalizado")
        break

    elif 0 <= valor <= 12:
        mes = meses[valor - 1]

        print(mes)

    else:
        print("Numero no valido. Introduce un numero entre 0 y 12.")

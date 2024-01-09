
valor = input("Introduce un valor en €")
valor = int(valor)
iva = input("Introduce porcentaje de IVA (4%, 10%, 21%)")
iva = int(iva)
total = (valor - (valor * iva / 100))

print(valor)
print(iva)
print(total)
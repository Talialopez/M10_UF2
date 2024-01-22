areas_pis = {'Menjador':10.15, 'Rebedor': 9.56, 'Habitació1': 12.34, 'Terrassa': 15.55, 'Lavabo': 7.98, 'Cuina': 12, 'Habitació2': 12.23}

segundoElemento = list(areas_pis.values())[1]
print(segundoElemento)

ultimoElemento = list(areas_pis.values())[6]
print(ultimoElemento)

print('Terrassa')

tresElementos = list(areas_pis.items())[:3]
for elemento in tresElementos:
    print(elemento)

desdeTercerElemento = list(areas_pis.items())[2:]
for elemento in desdeTercerElemento:
    print(elemento)

primeraHabitacion = list(areas_pis.values())[2]
segundaHabitacion = list(areas_pis.values())[6]
totalArea = (float)(primeraHabitacion + segundaHabitacion)
print("Total area habitaciones: ", totalArea)

areaLavabo = list(areas_pis.values())
areaLavabo[4] = 56
print("Area lavabo modificada", areas_pis)


areas_pis["Lavabo"] = 52.0
for area in areas_pis:
    print(f"{area}: {areas_pis[area]}")

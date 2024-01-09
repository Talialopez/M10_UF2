primeraPalabra = input("Introduce una palabra: ")
segundaPalabra = input("Introduce otra palabra: ")

primerCaracter = primeraPalabra[0]
segundoCaracter = segundaPalabra [0]
tercerCaracter = primeraPalabra[1]
cuartoCaracter = segundaPalabra[1]

primeraPalabra = primeraPalabra.replace(primeraPalabra[0], segundoCaracter)
primeraPalabra = primeraPalabra.replace(primeraPalabra[1], cuartoCaracter)
segundaPalabra = (segundaPalabra.replace(segundaPalabra [0], primerCaracter))
segundaPalabra = (segundaPalabra.replace(segundaPalabra [1], tercerCaracter))

print(primeraPalabra, segundaPalabra)
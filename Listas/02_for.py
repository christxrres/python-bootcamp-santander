numeros = [1, 30, 21, 2, 9, 65, 34]

pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

        print(numero) # 30 2 34

numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)

print(quadrado) #[1, 900, 441, 4, 81, 4225, 1156]
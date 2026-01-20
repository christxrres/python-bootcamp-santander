numeros = {1,2,3,1,2,4,5,5,6,7,8,9,0}

print(numeros) # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

numeros.discard(1)

print(numeros) # {0, 2, 3, 4, 5, 6, 7, 8, 9}

numeros.discard(5)

print(numeros) # {0, 2, 3, 4, 6, 7, 8, 9}

# Caso elemento não exista, funciona normal. Diferente do remove.
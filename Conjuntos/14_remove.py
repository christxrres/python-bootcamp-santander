numeros = {1,2,3,1,2,4,5,5,6,7,8,9,0}

print(numeros) # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

numeros.remove(0)

print(numeros) # {1, 2, 3, 4, 5, 6, 7, 8, 9}

numeros.remove(4)

print(numeros) # {1, 2, 3, 5, 6, 7, 8, 9}

# Caso elemento não exista, retorna erro. Diferente do discard.


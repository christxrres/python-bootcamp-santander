# Método copy

lista = [10, "teste", True]
lista2 = lista.copy()

print(lista)

print(id(lista2), id(lista))

lista2[0] = 2

print(lista2)
print(lista)

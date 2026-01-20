def somar(a, b):
    return a + b

def subtrair (a, b):
    return a - b

def expo (a, b):
    return a*b

def exibir_resultado(a,b,funcao):
    resultado = funcao(a,b)
    print(f"O resultado da operação é igual a {resultado}")

exibir_resultado(10, 10, somar)
# O resultado da operação é igual a  20
exibir_resultado(10, 10, subtrair)
# O resultado da operação é igual a 0
exibir_resultado(10, 10, expo)
# O resultado da operação é igual a 100

print(somar(1, 25))
# 26
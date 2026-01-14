a = int(input("Informe um número inteiro: "))
print(a)

a += 1
print(a)

a += 1
print(a)

texto = input("Informe um texto: ")

VOGAIS = "bcdfghjklmnpqrstvwxyz"

for letra in texto:
    if letra.lower() in VOGAIS:
        print(letra, end="")
nome = "Christofer"
idade = 21
profissao = "Programador"
linguaguem = "Python"
saldo = 576.9034

# print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s." % (nome, idade, profissao, linguaguem))

# print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}.".format(nome, idade, profissao, linguaguem))

# print("Olá, me chamo {0}. Eu tenho {1} anos de idade, trabalho como {2} e estou matriculado no curso de {3}.".format(nome, idade, profissao, linguaguem))

# print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguaguem}.".format(nome=nome, idade=idade, profissao=profissao, linguaguem=linguaguem))

dados = {"nome": "Christofer", "idade": 21}

print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguaguem}.")

# print("Nome: {nome} Idade: {idade}".format(**dados))

print(f"Nome: {nome} Idade: {idade}")

print(f"Saldo: {saldo:.1f}")



saldo = 300
saque = 3300
status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque!")
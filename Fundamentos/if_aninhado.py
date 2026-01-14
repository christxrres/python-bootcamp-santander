saldo = 2000
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Saque realizado!")
else:
    print("Saldo insuficente!")

opcao = int(input("Informe uma opção\n[1] Sacar\n[2] Extrato: \n"))

if opcao == 1:
    valor = float(input("Informa a quantia para o saque: "))
elif opcao == 2:
    print("Exibindo o extrato...")
else:
    exit("Opção inválida.")

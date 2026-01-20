def mensagem():
    print("Olá mundo!")

def mensagem_2(nome):
    print(f"Seja bem-vindo, {nome}!")

def mensagem_3(nome="Anônimo"):
    print(f"Seja bem-vindo, {nome}!")

mensagem()
mensagem_2(nome="Geo")
mensagem_3()
mensagem_3("Christofer")


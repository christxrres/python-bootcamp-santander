contatos = {
    "chris@gmail.com": {"nome": "Christofer", "idade": 21, "telefone": "91111-1111"},
    "geovana@gmail.com": {"nome": "Geovana", "idade": 22, "telefone": "91111-1112"},
    "pele@gmail.com": {"nome": "Pele", "idade": 97, "telefone": "91111-1113", "extra": {"a": 1}},
}

print(contatos["geovana@gmail.com"]["idade"]) #22

extra = contatos["pele@gmail.com"]["extra"]["a"]
print(extra) # 1

# for

for chave in contatos:
    print(chave, contatos[chave])


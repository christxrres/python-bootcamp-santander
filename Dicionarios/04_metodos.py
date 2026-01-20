########## MÉTODO CLEAR #############
print("============ MÉTODO CLEAR ============")

contatos = {
    "christofer@gmail.com": {"Nome": "Christofer", "Idade": 21}
}

print(contatos) # {'christofer@gmail.com': {'Nome': 'Christofer', 'Idade': 21}}
contatos.clear()
print(contatos) # {}

########## MÉTODO COPY #############
print("============ MÉTODO COPY ============")

contatos = {
    "christofer@gmail.com": {"Nome": "Christofer", "Idade": 21}
}

copia = contatos.copy()

copia["christofer@gmail.com"] = {"Nome": "Chris"}

print(contatos["christofer@gmail.com"])
print(copia)

########## MÉTODO FROMKEYS #############
print("============ MÉTODO FROMKEYS ============")

print(dict.fromkeys(["nome", "telefone"]))
print(dict.fromkeys(["nome", "telefone"],"Inserir"))

########## MÉTODO GET #############
print("============ MÉTODO GET ============")

contatos = {
    "christofer@gmail.com": {"Nome": "Christofer", "Idade": 21}
}

# contatos["chave"]

print(contatos.get("chave"))
print(contatos.get("chave",{}))
print(contatos.get("christofer@gmail.com",{}))

########## MÉTODO ITEMS #############
print("============ MÉTODO ITEMS ============")

contatos = {
    "christofer@gmail.com": {"Nome": "Christofer", "Idade": 21}
}

print(contatos.items())

########## MÉTODO KEYS #############
print("============ MÉTODO KEYS ============")

contatos = {
    "christofer@gmail.com": {"Nome": "Christofer", "Idade": 21},
    "teste@gmail.com" : {"Nome": "Teste", "Telefone": "91111-1111"}
}

print(contatos.keys())

########## MÉTODO POP #############
print("============ MÉTODO POP ============")

contatos = {
    "christofer@gmail.com": {"Nome": "Christofer", "Idade": 21},
    "teste@gmail.com" : {"Nome": "Teste", "Telefone": "91111-1111"}
}

print(contatos.keys())

contatos.pop("christofer@gmail.com")
print(contatos.keys())

contatos.pop("teste@gmail.com")
print(contatos.keys())

########## MÉTODO POP ITEM #############
print("============ MÉTODO POP ITEM ============")

contatos = {
    "christofer@gmail.com": {"Nome": "Christofer", "Idade": 21},
    "teste@gmail.com" : {"Nome": "Teste", "Telefone": "91111-1111"}
}

print(contatos)

contatos.popitem()
print(contatos)

contatos.popitem()
print(contatos)

########## MÉTODO SET DEFAULT #############
print("============ MÉTODO SET DEFAULT ============")

contato = {"Nome": "Chris", "Idade": 21}
print(contato)

contato.setdefault("Nome", "Geovana")
print(contato)

contato.setdefault("Telefone", "111111111")
print(contato)

########## MÉTODO UPDATE #############
print("============ MÉTODO UPDATE ============")

contatos = {
    "christofer@gmail.com": {"Nome": "Christofer", "Idade": 21}
}

print(contatos)
contatos.update({"christofer@gmail.com": {"Nome": "Chris"}})
print(contatos)
contatos.update({"geovana@gmail.com": {"Nome": "Geo"}})
print(contatos)

########## MÉTODO VALUES #############
print("============ MÉTODO VALUES ============")

contatos = {
    "christofer@gmail.com": {"Nome": "Christofer", "Idade": 21},
    "teste@gmail.com" : {"Nome": "Teste", "Telefone": "91111-1111"}
}

print(contatos.values())

########## MÉTODO IN #############
print("============ MÉTODO IN ============")

contatos = {
    "christofer@gmail.com": {"Nome": "Christofer", "Idade": 21},
    "teste@gmail.com" : {"Nome": "Teste", "Telefone": "91111-1111"}
}

resultado = "christofer@gmail.com" in contatos
print(resultado)

resultado = "testando@gmail.com" in contatos
print(resultado)

resultado = "Nome" in contatos["christofer@gmail.com"]
print(resultado)

########## MÉTODO DEL #############
print("============ MÉTODO DEL ============")

contatos = {
    "christofer@gmail.com": {"Nome": "Christofer", "Idade": 21},
    "teste@gmail.com" : {"Nome": "Teste", "Telefone": "91111-1111"}
}

print(contatos)

del contatos["christofer@gmail.com"]["Idade"]
print(contatos)

del contatos["teste@gmail.com"]
print(contatos)

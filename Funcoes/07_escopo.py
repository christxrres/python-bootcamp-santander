salario = 2000

def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario

print(salario_bonus(500)) # 2500
      # Má prática.

def salario_bonus2(salario, bonus):
    salario += bonus
    return salario

print(salario_bonus2(2000, 500)) # 2500
    
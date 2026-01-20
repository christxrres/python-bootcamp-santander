conjunto_a = {1,2,3}
conjunto_b = {4,5,6}
conjunto_c = {1,7,8}

isdis_a = conjunto_a.isdisjoint(conjunto_b)
isdis_c = conjunto_a.isdisjoint(conjunto_c)

print(isdis_a) # True
print(isdis_c) # False
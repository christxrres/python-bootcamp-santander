conjunto_a = {1,2,3}
conjunto_b = {1,2,3,4,5}

issuper_a = conjunto_a.issuperset(conjunto_b)
issuper_b = conjunto_b.issuperset(conjunto_a)

print(issuper_a) # False
print(issuper_b) # True
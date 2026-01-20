conjunto_a = {1,2,3}
conjunto_b = {1,2,3,4,5}

issub_a = conjunto_a.issubset(conjunto_b)
issub_b = conjunto_b.issubset(conjunto_a)

print(issub_a) # True
print(issub_b) # False
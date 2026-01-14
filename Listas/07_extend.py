linguagens =["python", "js", "c"]

print(linguagens) # ['python', 'js', 'c']

linguagens.extend(["java", "csharp"])

print(linguagens) # ['python', 'js', 'c', 'java', 'csharp']

exemplo = ["a", "m", "o","r"]

exemplo2 = ["t", "e"]

print(exemplo) # ['a', 'm', 'o', 'r']

print(exemplo2) # ['t', 'e']

exemplo.extend(exemplo2)

print(exemplo) ['a', 'm', 'o', 'r', 't', 'e']
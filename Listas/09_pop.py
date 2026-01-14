linguagens = ["python", "java", "c", "java", "csharp"]

linguagens.pop()
print(linguagens) # ['python', 'js', 'c', 'java']

linguagens.pop()
print(linguagens) # ['python', 'js', 'c']

linguagens.pop()
print(linguagens) # ['python', 'js']

linguagens.pop(0)
print(linguagens) # ['js']

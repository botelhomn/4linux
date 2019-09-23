# 1: abrir o arquivo

with open("arquivo-teste") as f:
    conteudo = f.read()
    
# 2: transformar o conteudo em lista
lista = conteudo.split() 

# 3: efetuar a soma
soma = 0

for elemento in lista:
    soma = soma + int(elemento)

print(soma)
    

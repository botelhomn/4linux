lista = [x**2 for x in range(300) if x % 2 == 0]

print(lista)



#exercicio de contagem de letras
def conta_vogais(args):
    

string = "Olá pessoas"

print(string)
string = string.split()

print(string)

# exercicio de lista de compras

dic = {1:4.50, 2:9.90, 3:5.50} 

lista = []

lista.append(1)
lista.append(1)
lista.append(2)

soma = 0

for elemento in lista:
    if elemento in dic:
        soma += dic[elemento]

print(soma)


exit()
string = " Ola pessoas bonitas!"


vogais = "aeiou"
contador = 0

for letra in string:
    if letra in vogais:
        contador +=1

print(contador)

exit()

def soma(a,b):
    return a + b

def sub(a,b):
    return a - b

dic = {1:soma, 2:sub}

a=5
b=6
opcao = 1

print(dic[opcao](a,b))
    
exit()

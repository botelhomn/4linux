#!/usr/bin/python3 
"""
    Script para realizar funções de uma calculadora
    Autor:
    Data:
    Alterações....

"""

def escolhe_op():
    opcao = int(input("Digite a opcao desejada:"))
    while opcao < 1 or opcao > 4 :
        print("Opcao Invalida")
        opcao = int(input("Digite a opcao desejada:"))
    return opcao

def soma(a,b):
    print(a+b)

def sub(a,b):
    print(a-b)
    
def mult(a,b):
    print(a*b)
    
def div(a,b):
    if b == 0:
        print("Não existe div por zero")
    else:
        print(a/b)

dic = {1:soma, 2:sub, 3:div, 4:mult}

def main():

    print("Calculadora:")

    num1 = int(input("Digite o primeiro n:"))
    num2 = int(input("Digite o segundo n:"))

    print("Escolha a opcao:")
    print("1 - SOMA\n2 - SUB\n3 - DIV\n 4 - MULT")

    opcao = escolhe_op()

    dic[opcao](num1,num2)

if __name__ == "__main__":
    main()

exit()
if opcao == 1:
    soma(num1,num2)
elif opcao == 2:
    sub(num1, num2)
elif opcao == 3:
    div(num1,num2)
elif opcao == 4:
    mult(num1,num2)
else:
    print("Opcao Invalida.")
    

#funções


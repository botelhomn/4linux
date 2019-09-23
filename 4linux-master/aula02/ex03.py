while True: 
    n1= float(input("Digite N1: "))
    n2= float(input("Digite N2: "))

    print("Escolha sua opcao:")
    print(" 1 - SOMA")
    print(" 2 - SUBTRACAO")
    print(" 3 - DIVISAO")
    print(" 4 - MULTIPLICACAO")
    print(" 5 - SAIR")

    opcao= int(input("Digite a opcao:"))

    if opcao == 1:
        print("{0:.2f} + {1:.2f} = {2:.2f}".format(n1,n2,n1+n2))
    elif opcao == 2:
        print("{0:.2f} + {1:.2f} = {2:.2f}".format(n1,n2,(n1-n2)))
    elif opcao == 3:
        print("0:.2f} + {1:.2f} = {2:.2f}".format(n1,n2,(n1/n2)))
    elif opcao == 4:
        print("{0:.2f} + {1:.2f} = {2:.2f}".format(n1,n2,(n1*n2)))
    elif opcao == 5:
        print("Obrigado!")
        break
    else:
        print("Opcao Invalida!")
        
        
exit()        
#calculadora 

#dicionario

dicionario = {"Nome":"João", "Idade":32, "Peso":75.5}

for chave in dicionario:
    print(dicionario[item])

# lista
lista = ["bruna","joao",3,4,5,6]

lista.append("Henrique") 

lista[0] = "Joana"

print(lista)

exit()
for elemento in lista:
    print(elemento) 

exit()
while i < 6:
    print(lista[i])
    i = i+1
     

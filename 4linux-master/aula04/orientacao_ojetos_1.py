#!/usr/bin/python3

#### Funções

#passo 7: criar função para realizar soma.
def somaTotal(lista):
    total = 0
    for elemento in lista:
        total += dic[elemento]
    return total

#### Constantes
    #passo 1: criar dicionário com valores de referência
dic = {1:8.5, 2:3.25, 3:4.60}


#### Função Principal
def main():

    #passo 2: criar a lista
    lista = []

    #passo 3: criar o menu de escolha 

    while True:
        print("Escolha o seu produto:")
        print("1- Banana\n2- Pera\n3- Melancia\n4- Sair ")
        
        #passo 4: capturar a escolha da fruta
        opcao = int(input(("Digite a opcão desejada: ")))
        
        #passo 5: validar sea escolha foi sáida:
        if opcao == 4:
            break
                    
        lista.append(opcao)

        #passo 6: validar se existem itens na minha lista:
    if len(lista) != 0:
        total = somaTotal(lista)
        print("O valor da sua compra foi : {0:.2f} ".format(total))
    else:
        print("Sua lista está vazia") 

# verifica se é script ou pacote
if __name__ == "__main__":
    main()

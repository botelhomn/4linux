# Orientação à Objetos

"""
Contexto:
    Chegou em um determinado momento que os desenvolvedores
    e os homens de negócio estavam em um certo descompasso:
    a comunicação entre ambos não estava sendo mais satisfatória,
    além de muitos problemas envolvendo escalabilidade e manutenção
    de código começaram a aparecer.
    
    É nesse contexto que um novo paradigma de programação foi
    desenvolvido : Orientação a Objetos
    
    Em orientação à objetos há um preocupação primária que é
    entender às necessidade de negócio e ao mesmo tempo
    compatibilizar os seus relacionamentos sobre o ponto de vista de 
    código.
    
    
    Características:
        
        atributos - características (forte associação com var)
        métodos   - comportamento (forte associação com função)
        construtor 
        
""" 



class Carrinho:
    #__lista = []
    
    def __init__(self, item):
        self.__lista = []
    
    def __adicionaItem(self,elemento):
        self.__lista.append(elemento)
        
    def getLista(self):
        print(self.__lista)
    
    def setLista(self ,item):
        self.__adicionaItem(item)

def main():
    novaCompra = Carrinho(2)
    novaCompra.setLista(1)
    novaCompra.setLista(3)
    novaCompra.setLista(4)
    novaCompra.setLista(7)
    #novaCompra.__lista.append(5)
    #print(novaCompra.Carrrinho__lista)
    #print(novaCompra.__lista)
    novaCompra.getLista()
    


if __name__ == '__main__':
    main()
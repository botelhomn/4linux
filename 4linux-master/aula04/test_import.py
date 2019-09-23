#import ex01 - imprta o pacote
from ex01 import Carro # importa somente a classe

escort = Carro()
verona = Carro()

escort.cor = "azul"
escort.acelerar()
print(escort.velocidade)

vernona.cor = "vermelho"
verona.acelerar()
print(verona.velocidade)

# Criar Classe do Onibus
# atributos: 
    #viacao 
    #linha
    #Lugares
    #Capacidade_Atual (+) (-)

#Metodos: 
    #pegarpassageiros()
    #desembarcar()
    #validar se o onibus esta cheio



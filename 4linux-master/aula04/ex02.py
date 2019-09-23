#modulos 
import random
import time 


#lista = [random.randint(0,9) for p in range(20) ]

#print(lista)

#exit()
participantes = ["Joao", "Marcela", "Leticia", "Filomena", "Arnaldo"]
jogadores = 5

while jogadores > 1:
    print("começa a rolar a musica ....")
    time.sleep(3)
    print("PAROU!")
    
    print("Pessoas se movimentando....")
    
    index = random.randint(0,jogadores-1) 
    nome = participantes.pop(index)
    print("O jogador {} não conseguiu sentar...".format(nome))
    
    jogadores -= 1


print("O participante {} venceu!".format(participantes[0]))
    

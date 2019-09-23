
#2 
##end_arquivo = "C:\Teste\Arquivo.txt"

with open("arquivo2.txt") as arquivo: 
    texto = arquivo.read() 


frase = texto + " novo arquivo"

with open("arquivo3.txt", "a+") as novoArquivo:
    novoArquivo.write(frase)
    


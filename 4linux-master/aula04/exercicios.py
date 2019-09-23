## módulos 

### Arquivos:

### Abrindo arquivos

## 1a forma:

file = open('nome do arquivo', 'modoabertura')
conteudo = f.read

# sempre precisa fechar o arquivo caso utilizar essa forma:
file.close()

## 2a forma: 
with open('caminho/para/arquivo.txt'. 'modo abertura') as f:
    conteudo = f.read()

# para coletar o arquivo 

while open ("aruivo", "as") as arq:
    arq.write(conteudo)

## 3


## modos de abertura
r - reading - leitura (modo padrão caso não informar o conteúdo do arquivo)
w - writing - escrita (modo para escrita de arquivos. Caso o arquivo existir ele é sobrescrito)
x - cria um novo arquivo - caso se o arquivo existir ele falha
a - append - inserção (caso queira adicionar conteúdo em um arquivo já existente. caso o arquivo não existir ele cria um novo)
b - binary - abre o arquivo no modo binario (byte a byte)
+ - reading and update

## principais comandos/usos

f.read()  : lê o conteúdo do arquivo
f.write() : salva conteúdo do arquivo
f.readlines(): lê o arquivo linha por linha (lista de linhas de arquivos


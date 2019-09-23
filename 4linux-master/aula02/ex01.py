# pegar 3 notas 
# média < 4 - reprovado
# média 4 < x < 6 - recuperação
# x >= 6 - aprovado 

nota1 = 4
nota2 = 4.5
nota3 = 7.8
media = (nota1+nota2+nota3)/3
print(media)
if media < 4:
    print("Reprovado")
elif media < 6:
    print("Rec.")
else:
    print("Aprovado")

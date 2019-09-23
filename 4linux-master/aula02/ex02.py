anoNasc = int(input("Digite o Ano de Nascimento: "))
text= "Oi"
if anoNasc < 1965:
    print(" Ano de Nascimento: {} {} - Geracao BB".format(anoNasc,text))
elif anoNasc < 1980:
    print("Ano de Nascimento: {} - Geracao X".format(anoNasc))
elif anoNasc < 1999:
    print("Ano de Nascimento: {} - Geracao Y".format(anoNasc))
else:
    print("Ano de Nascimento: {} - Geracao Z".format(anoNasc))

#

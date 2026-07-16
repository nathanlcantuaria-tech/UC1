def idade (ano):
    idade = anoatual - anonascimento
    if idade >= 65:
     print("Idoso")
    elif idade >= 18 and idade < 65:
     print("Maior de idade")
    else:
     print("Menor de idade")     
     print(f"Sua idade é {idade} ")       



anonascimento = int(input("Digite o seu ano de nascimento"))
anoatual = int(input("Digite o ano atual"))
idade(anonascimento,anoatual)

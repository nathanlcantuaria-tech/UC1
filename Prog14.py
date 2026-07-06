anonascimento = float (input ("Digite seu ano de nascimento "))
anoatual = float (input ("Digite o ano atual"))
resultado = anoatual - anonascimento
print (f"Sua idade é {resultado}")
if resultado >=18:
    print("Maior de idade")
else:
    print("Menore de idade")  
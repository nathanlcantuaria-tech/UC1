idade = int(input("Digite a idade do candidato"))
genero = input("Digite seu gênero") .upper()
if idade >= 18 and genero == "M":
    print("Apto")
else:
    print("Inapto")   
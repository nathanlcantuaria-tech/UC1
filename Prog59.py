nome = input("Digite seu nome")
nota1 = float(input("Digite a nota do 1º bimestre"))
nota2 = float(input("Digite a nota do 2º bimestre"))
nota3 = float(input("Digite a nota do 3º bimestre"))
nota4 = float(input("Digite a nota do 4º bimestre"))
media = (nota1 + nota2 + nota3 + nota4)/4
print(f"O aluno {nome} tem a média final no valor de {media}")
if media >=6:
    print("O aluno está aprovado")
else:
    print("Recuperação")    
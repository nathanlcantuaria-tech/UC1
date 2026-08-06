anonascimento = int(input("Digite seu ano de nascimento"))
idade = 2026 - anonascimento
if idade <18:
    print("Menor idade")
elif idade <=65:
    print("Maior idade")
else:
    print("Prioridade/Sênior")
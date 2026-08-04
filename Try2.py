try:
    numerador = int(input("Digite o número a ser dividido"))
    denominador = int(input("Digite o valor da divisão"))

    resultado = numerador/denominador
    print(f"O resultado é {resultado}")

except ValueError:
    print("Dgite apenas números inteiros")

except ZeroDivisionError:
    print("Não pode dividir por zero")
valor1 = int (input ("Digite o 1º valor:"))
valor2 = int (input ("Digite o 2º valor:"))
print("1 - soma")
print("2 - subtracao")
print("3 - multiplicacao")
print("4 - divisao")
operador = int (input("Escolha o operador"))
match operador:
    case 1:
        print(f"Resultado:{valor1 + valor2}")
    case 2:
        print(f"Resultado: {valor1 - valor2}")
    case 3:
        print(f"Resultado: {valor1 * valor2}")     
    case 4:
        print(f"Resultado: {valor1 / valor2}")
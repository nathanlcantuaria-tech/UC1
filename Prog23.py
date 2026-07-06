dia = input("Digite o dia da semana")
match dia:
    case "Segunda"| "Terça"| "Quarta"| "Quinta"| "Sexta":
        print("Dia de semana, dia de programar")
    case "Sábado"| "Domingo":
        print("Final de semana, dia de descansar")
    case  _:
        print("Dia inválido")           
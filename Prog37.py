for i in range(5):
    valor = int(input("Digite um valor"))
    x = valor % 2
    if x == 0:
        print(f"{valor} é par")
    else:
        print(f"{valor} é ímpar")  

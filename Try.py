try:
    idade = int(input("Digite sua idade"))
    print(f"Sua idade é {idade}")
except ValueError:
    print("Digite apenas números válidos")
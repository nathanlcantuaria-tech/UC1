codigo = ""
total = 0
while codigo != "0":
    codigo = input("Digite um código")
    if codigo == "001":
        total = total+4
    elif codigo == "002":
        total = total+7
    elif codigo ==  "003":
        total = total+5 
    else:
        print("Código inválido") 
print(f"O total das compras foi, {total}")           
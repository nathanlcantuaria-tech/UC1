carros = {}
for i in range(2):
    carro = input("Carro:  ")
    marca = input("Marca:  ")
    valor = float(input("Valor do carro  "))
    carros[carro] = {"Marca": marca, "valor": valor}
print(f"As informações coletadas são:  {carros} ")    

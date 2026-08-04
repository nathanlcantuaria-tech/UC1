class Carros:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def buzinar(self):
        return f"{self.modelo} faz bibi"    

carro1 = Carros("toyota", "corolla")
carro2 = Carros("BMW", "X1")

print(f"A marca do seu carro é {carro2.marca} e o modelo do seu carro é {carro2.modelo}")
print(carro1.modelo)
print(carro2.buzinar())
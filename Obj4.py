class Passarinho:
    def __init__(self, raca, cor):
        self.raca = raca
        self.cor = cor
    
    def cantar(self):
        return f"O {self.raca} canta "


passarinho1 = Passarinho("sabiá", "amarelo")
passarinho2 = Passarinho("beija-flor","azul")

print(f"O {passarinho1.raca} da cor {passarinho1.cor} é bonito")
print(passarinho1.cantar())
print(f"O {passarinho2.raca} da cor {passarinho2.cor} é bonito")
print(passarinho2.cantar())
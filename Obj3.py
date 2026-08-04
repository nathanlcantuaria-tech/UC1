class Biscoito:
    def __init__(self, sabor, gosto):
        self.sabor = sabor
        self.gosto = gosto 

    def croc(self):
        return f"O sabor {self.sabor} faz croc croc "  

biscoito1 = Biscoito("chocolate", "amargo")    
biscoito2 = Biscoito("amendoim", "doce")
print(f" O sabor {biscoito2.sabor} tem o gosto {biscoito2.gosto} é bem agradável")
print(biscoito2.croc())
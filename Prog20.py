idade = int(input("Digite sua idade"))
ingresso = input("Você possui ingresso? S - para Sim e F - para Não") .upper()
if idade >=12 and ingresso == "S":
    print("Acesso liberado! Divirta-se no brinquedo")
elif ingresso =="S" and idade <12:
    print("Você tem o ingresso, mas não tem a idade mínima de 12 anos")
else:
        print("Acesso negado, você precisa de um ingresso")
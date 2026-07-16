def media_aluno(n1,n2,n3,n4):
    media = (n1 + n2 + n3 + n4)/4
    if media >= 7:
        print("Aprovado")
    elif media >= 5:
        print("Recuperação")  
    else:
        print("Reprovado")   
    print(f" A média do aluno é {media}")        




nota_1 = int(input("Digite a 1ª nota"))
nota_2 = int(input("Digite a 2ª nota"))
nota_3 = int(input("Digite a 3ª nota"))
nota_4 = int(input("Digite a 4ª nota")) 
media_aluno(nota_1,nota_2,nota_3,nota_4)

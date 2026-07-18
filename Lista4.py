curso = ["Inglês","Espanhol"]
curso_mais = input("Selecione outro curso")
curso.append(curso_mais)
curso.sort()
m = input("Exclua um curso")
curso.remove(m)
print("LISTAGEM DE CURSOS")
for x in curso:
    print(x)

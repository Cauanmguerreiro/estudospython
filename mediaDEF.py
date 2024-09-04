def lernotas():
    n=float(input("Digite a nota para o aluno: "))
    return n

def resultado(n1, n2):
    media=(n1+n2)/2
    print("nota 1:", n1)
    print("nota 2:", n2)
    print("Média: ", media, "Resultado", end="")
    if media >= 7:
        print("Aprovado")
    else:
        print("reprovado")

a = lernotas()
b = lernotas()
resultado (a,b)

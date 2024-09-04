notaA=float(input("Informe a primeira nota: "))
notaB=float(input("Informw a segunda nota: "))

#calcular média
mediafinal = (notaA + notaB) / 2

#verificação
if mediafinal >=7.0:
    print("A média: %.1f - aprovado" % mediafinal)
else:
    print("a média: %.1f- reprovado" % mediafinal)

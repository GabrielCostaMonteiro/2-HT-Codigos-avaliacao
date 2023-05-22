indice_pol = float(input("Digite o índice de poluição medido: "))

if indice_pol <= 0.25:
    print("Índice de poluição aceitável")
elif indice_pol <= 0.3:
    print("Indústrias do 1º grupo devem suspender suas atividades.")
elif indice_pol <= 0.4:
    print("Indústrias do 1º e 2º grupo devem suspender suas atividades.")
else:
    print("Todos os grupos devem paralisar suas atividades imediatamente.")
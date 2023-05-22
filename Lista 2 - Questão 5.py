# Lê o peso de peixes informado
P = float(input("Informe o peso de peixes em quilos: "))

# Verifica se há excesso
if P > 50:
    # Calcula o excesso e a multa a ser paga
    E = P - 50
    M = E * 4
else:
    # Caso não haja excesso, define as variáveis como zero
    E = 0
    M = 0

# Imprime o resultado
print("Excesso de peso: ", E, "kg")
print("Valor da multa: R$", M)
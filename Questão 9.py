
distanciaPercorrida = float(input("Digite a distância percorrida (em km): "))


combustivelGasto = float(input("Digite a quantidade de combustível gasta (em litros): "))

consumo_medio = distanciaPercorrida / combustivelGasto
print("O consumo médio do automóvel é de", round(consumo_medio, 2), "km/l.")

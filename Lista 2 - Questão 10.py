distancia = float(input("Digite a distância percorrida em quilômetros: "))
combustivel_gasto = float(input("Digite a quantidade de combustível gasto em litros: "))
preco_gasolina = float(input("Digite o preço da gasolina por litro: "))

consumo_medio = distancia / combustivel_gasto
gasto_litro = preco_gasolina * 1  # considerando que o usuário informou o preço por litro

print("Consumo médio do veículo: {:.2f} km/l".format(consumo_medio))
print("Gasto com a gasolina por litro: R$ {:.2f}".format(gasto_litro))
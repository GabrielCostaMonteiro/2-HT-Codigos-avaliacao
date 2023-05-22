cor = input("Insira a cor do jogo: ").lower()

if cor == "verde":
    print("O preço deste jogo é R$ 10,00")
elif cor == "azul":
    print("O preço deste jogo é R$ 20,00")
elif cor == "amarelo":
    print("O preço deste jogo é R$ 30,00")
elif cor == "vermelho":
    print("O preço deste jogo é R$ 40,00")
else:
    print("Cor inválida!")
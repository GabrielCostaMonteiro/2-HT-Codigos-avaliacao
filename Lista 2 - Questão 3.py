num_1 = int(input("Digite o primeiro número: "))
num_2 = int(input("Digite o segundo número: "))
num_3 = int(input("Digite o terceiro número: "))

menor = num_1  # considera num_1 o menor número

if num_2 < menor:
    menor = num_2  # num_2 é menor que num_1
if num_3 < menor:
    menor = num_3  # num_3 é menor que o menor número anterior

print("O menor número digitado é:", menor)
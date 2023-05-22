C = int(input("Digite o código do operário: "))
N = int(input("Digite o número de horas trabalhadas: "))

if N > 50:
    E = (N - 50) * 20
    salario_total = 50 * 10 + E
else:
    E = 0
    salario_total = N * 10

print("Salário total: R$ {:.2f}".format(salario_total))
print("Salário excedente: R$ {:.2f}".format(E))
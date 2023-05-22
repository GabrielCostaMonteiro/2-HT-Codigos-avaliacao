num = int(input("Digite um número: "))

# Considera o número 1 como não primo
if num == 1:
    print(f"{num} não é um número primo")
else:
    # Verifica se há divisores entre 2 e a metade do número
    for i in range(2, num//2+1):
        if num % i == 0:
            print(num, "não é um número primo")
            break
    else:
        print(num, "é um número primo")
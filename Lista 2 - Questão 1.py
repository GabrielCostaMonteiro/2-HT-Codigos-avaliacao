notas = []

for i in range(4):
    nota = float(input(f"Informe a {i+1}ª nota: "))
    while nota < 0 or nota > 10:
        nota = float(input("Nota inválida. Informe novamente: "))
    notas.append(nota)

media = sum(notas)/len(notas)

if media < 4:
    situacao = "Em processo de Aprendizagem (Reprovado)"
elif media < 8:
    situacao = "Recuperação"
else:
    situacao = "Aprovado"

print(f"Média: {media:.1f}")
print(f"Situação: {situacao}") 
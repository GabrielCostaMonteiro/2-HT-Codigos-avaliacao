pesoDoPaciente = float(input("Digite o seu peso em kg: "))


alturaDoPaciente = float(input("Digite a sua altura em metros: "))


imc = pesoDoPaciente / alturaDoPaciente**2


if imc < 18.5:
    diagnóstico = "baixo peso"
elif imc < 25:
    diagnóstico = "intervalo normal"
elif imc < 30:
    diagnóstico = "sobrepeso"
elif imc < 35:
    diagnóstico = "obesidade classe I"
elif imc < 40:
    diagnóstico = "obesidade classe II"
else:
    diagnóstico = "obesidade classe III"


print("Seu IMC é de:", imc)

print("Diagnóstico:", diagnóstico)

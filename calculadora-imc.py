def calcular_imc(peso, altura):
    imc = peso / (altura * altura)
    return imc


peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))


imc = calcular_imc(peso, altura)

print(f"Seu IMC é: {imc:.2f}")

if (imc < 18.5):
    print("Abaixo do peso")
elif (imc < 24.9):
    print("Peso normal")
elif (imc < 29.9):
    print("Sobrepeso")
elif (imc < 34.9):
    print("Obesidade grau 1")
elif (imc < 39.9):
    print("Obesidade grau 2")
else:
    print("Obesidade grau 3")

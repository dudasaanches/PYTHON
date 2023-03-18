p = float(input("Informe o peso: "))
a = float(input("Informe a altura: "))

result = p / (a * a)

if result < 18.5:
	print("Abaixo do peso, seu IMC é: " + str(result))
elif result >= 18.5 and result <= 24.9:
	print("Peso normal, seu IMC é: " + str(result))
elif result >= 25 and result <= 29.9:
	print("Sobrepeso, seu IMC é: " + str(result))
elif result >= 30 and result <= 34.9:
	print("Obesidade grau I, seu IMC é: " + str(result))
elif result >= 35 and result <= 39.9:
	print("Obesidade grau II, seu IMC é: " + str(result))
else:
	print("Obesidade grau III, seu IMC é: " + str(result))
	
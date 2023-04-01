sal = float (input("Informe o salario: "))
qwl = float(input("Informe o quilowatt: "))

result = sal / 700
print("valor do quilowatt:", result)

valor = result * qwl
print("valor a ser pago:", valor)

desconto = valor - (valor * 0.1)
print("valor com desconto:", desconto)
tamanho = input("Qual o tamanho do ovo desejado\n1-Pequeno\n2-Médio\n3-Grande\nR:")

if tamanho == "1":
    valor = 7.80
elif tamanho == "2":
    valor = 12.90
elif tamanho == "3":
    valor = 23.95

sabor = input("Qual é o sabor desejado:\n1-Chocolate preto\n2-Chocolate branco\n3-Chocolate ao Leite\nR:")

if sabor == "1":
    valor= valor+9.67
elif sabor == "2":
    valor= valor+4.50
elif sabor == "3":
    valor= valor+9.32

recheio = input("Qual é o recheio desejado:\n1-Chocolate preto\n2-Chocolate branco\n3-Os dois\nR:")

if recheio == "1":
    valor = valor+4.83
elif recheio == "2":
    valor = valor+2.25
elif recheio == "3":
    valor = valor+3.46

acrescimo = input ("Qual será o acrescimo: \n1-MM'S \n2-KitKat\n3-Não quero\n4-Os dois\nR:")

if acrescimo == "1":
    valor= valor+4.67
elif acrescimo == "2":
    valor= valor+5.43
elif acrescimo == "4":
    valor= valor+10.1
elif acrescimo == "3":
    valor= valor+0.00

presente = input ("Sua compra sera presente?\n1-Sim\n2-Não\nR:")

if presente == "2":
    valor= valor+0.00
elif presente == "1":
    valor = valor+2.50

entrega = input ("Sua compra sera entrega?\n1-Sim\n2-Não\nR:")
if entrega == "2":
    valor= valor+0.00
elif entrega == "1":
    valor = valor+5.00

pagamento = input ("Informe a forma pagamento\n1-Cartão de crédito\n2-Dinheiro\n3-PIX\nR: ")
if pagamento == "1":
    valor= valor+3.30
elif pagamento == "2" or pagamento == "3":
    valor = valor/1.10

print("Seu ovo ficou R$ " + str(valor))
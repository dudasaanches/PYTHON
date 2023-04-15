lista = []
listaPar = []
listaImpar = []
somaPar = 0
somaImpar = 0
while True:
    num = int(input("Digite um número: "))
    if num == 0:
        break
    lista.append(num)
#percorendo a lista
for x in lista:
    if x%2==0:
        listaPar.append(x)
        somaPar+=x
    else:
        listaImpar.append(x)
        somaImpar+=x
#imprimindo os resultados
listaPar.sort()
listaImpar.sort()
print(f"Os numeros pares são: {listaPar} e sua somátoria é {somaPar}")
print(f"Os numeros impares são: {listaImpar} e sua somátoria é {somaImpar}")
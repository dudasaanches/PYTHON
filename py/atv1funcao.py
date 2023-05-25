def positivo_negativo(numero):
    if numero > 0:
        return "Positivo(P)"
    else:
        return "Negativo(N)"
    
x = int(input('Digite um  nuymero: '))
print(positivo_negativo(x))
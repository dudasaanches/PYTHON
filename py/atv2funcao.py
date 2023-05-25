def somaImposto(taxaImposto, custo):
    custo = custo + (custo * (taxaImposto / 100))
    return custo

C = 100.0
I = 10.0

precoImposto = somaImposto(I, C)

print("Preço com imposto: R$", precoImposto)
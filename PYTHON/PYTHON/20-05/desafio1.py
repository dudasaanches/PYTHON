# Funções lambda para conversão de temperatura
conversoes = {
    'celsius_para_fahrenheit': lambda celsius: (celsius * 9/5) + 32,
    'celsius_para_kelvin': lambda celsius: celsius + 273.15,
    'fahrenheit_para_celsius': lambda fahrenheit: (fahrenheit - 32) * 5/9,
    'fahrenheit_para_kelvin': lambda fahrenheit: (fahrenheit + 459.67) * 5/9,
    'kelvin_para_celsius': lambda kelvin: kelvin - 273.15,
    'kelvin_para_fahrenheit': lambda kelvin: (kelvin * 9/5) - 459.67
}

# Função para receber a entrada do usuário e realizar a conversão
def converter_temperatura():
    print("Unidades de medida disponíveis:")
    print("1 - Celsius")
    print("2 - Fahrenheit")
    print("3 - Kelvin")
    escolha_unidade = int(input("Digite o número da unidade de medida da temperatura inserida: "))

    unidade_entrada = ''
    if escolha_unidade == 1:
        unidade_entrada = 'celsius'
    elif escolha_unidade == 2:
        unidade_entrada = 'fahrenheit'
    elif escolha_unidade == 3:
        unidade_entrada = 'kelvin'
    else:
        print("Opção inválida.")
        return

    temperatura_entrada = float(input("Digite a temperatura com a unidade de medida (ex: 25 Celsius): "))

    print("Unidades de medida para conversão:")
    print("1 - Celsius")
    print("2 - Fahrenheit")
    print("3 - Kelvin")
    escolha_conversao = int(input("Digite o número da unidade de medida para conversão: "))

    unidade_saida = ''
    if escolha_conversao == 1:
        unidade_saida = 'celsius'
    elif escolha_conversao == 2:
        unidade_saida = 'fahrenheit'
    elif escolha_conversao == 3:
        unidade_saida = 'kelvin'
    else:
        print("Opção inválida.")
        return

    # Executar a conversão utilizando a função lambda correspondente
    resultado = conversoes[f"{unidade_entrada}_para_{unidade_saida}"](temperatura_entrada)
    print(f"A temperatura {temperatura_entrada} {unidade_entrada} é igual a {resultado} {unidade_saida}")

# Executar a função para converter temperatura
converter_temperatura()

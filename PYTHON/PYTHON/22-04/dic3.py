filmes = {}

filmes ["Barbie e as Três Mosqueteiras"] = {"vilão": "Phillipe", "ano": 2009}
filmes ["Barbie em A Princesa da Ilha"] = {"vilão": "Wenlock","ano": 2007}
filmes ["Barbie em A Princesa e a Popstar"] = {"vilão": "Tory","ano": 2012}
filmes ["Barbie Escola de Princesas"] = {"vilão": "Dama Devin","ano": 2011}
filmes ["Barbie Fairytopia: A Magia do Arco-fris"] = {"vilão": "Laverna","ano": 2007}
while True:
    filmeNovo = input("Digite o nome do filme(digite 0 para sair):")
    if filmeNovo == 0 :
        break
    vilaoNovo = input("Digite o nome do vilão:")
    anoNovo = input("Digite o ano do filme:")
    filmes[filmeNovo]={"Vilão": vilaoNovo, "ano": anoNovo}
print(filmes)
pesquisa = input('digite o filme procurado: ')
if pesquisa in filmes:
    print(filmes[pesquisa])
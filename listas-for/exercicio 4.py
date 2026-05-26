listaMaiores = []
listaMenores = []


for i in range(7):

    anoNacimento = int(input('digite a data de nacimento:'))
    idade = 2026 - anoNacimento
    if idade >= 18:
        listaMaiores.append(idade)
    else:
        listaMenores.append(idade)
print(f"\nQuantidade de pessoas maiores de idade: {len(listaMaiores)}")
print(f"Quantidade de pessoas menores de idade: {len(listaMenores)}")
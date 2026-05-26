lista = []
for i in range(10):
    idade = int(input('digite sua idade'))
    lista.append(idade)

print('imprimindo idades uma abaixo da outra')

lista.sort()
for i in lista:



     print('\nLista completa', lista)
print(f'a soma e:{sum(lista)}')
print(f'o maior numero e:{max(lista)}')
print(f'o menor numero e:{min(lista)}')
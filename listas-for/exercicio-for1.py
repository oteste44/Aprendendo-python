from turtledemo.penrose import sun

lista = []
for i in range(1, 7):
    num = int(input(f'digite o {i} numero:'))

lista.append(num)



print('\nLista completa', lista)
print(f'a soma e:{sum(lista)}')
print(f'o maior numero e:{max(lista)}')
print(f'o menor numero e:{min(lista)}')



# notas = [ ['joao', 2.3, 3.3],
#           ['mario', 5.7, 8.0],
#           ['beto', 9.0, 7.0]
#
# ]
# mediaAlunos = []
# for i in notas:
#     media = (i[1] + i[2])/2
#     lista = (i[0],media)
#     mediaAlunos.append(lista)
# print(f'lista de notas do alunos: {notas}')
# print(f'lista de media de alunos:{mediaAlunos}'
#
# estoque = [
#
#     [12, 5, 8],
#
#     [3, 15, 2],
#
#     [19, 0, 7]
#
# ]
# prateleira = int(input('digite o numero da prateleira:'))
# armario  = int(input('digite o numero do armario:'))
#
# for i in estoque:
#     for c in estoque:
#         print([estoque][prateleira][armario])

# dados = {
#     'nome': 'joao',
#     'idade': 21,
#     'sexo': 'M',
#     'altura': 1.80,
#     'temCNH': True
# }
#
# dados['altura'] = 1.78
# dados['peso'] = 92
# dados.pop('idade')
#
# continuar = 's'
# while continuar == 's':
#     dados_pessoais = input('digite oq vc quer:')
#     print(dados.get(dados_pessoais,'valor nao encontrado!'))
#     continuar = input('quer continuar? (s/n):')[0].lower()
#
#     for dadoss,valor in dados.items():
#         print(f'{dados_pessoais},: {valor}')
#
#
#
#





# vendas = [
#     [1200, 850, 900, 1500],
#     [900, 1100, 1000, 1300],
#     [1500, 1600, 1400, 1800],
#     [700, 600, 800, 900]
# ]

# vendas_vendedores = []
#
# for vendendor in vendas:
#     soma = 0
#     for dias in vendendor:
#         soma += vendendor
#         vendas_vendedores.append(soma)
#
#     vendas_dia = [0,0,0,0]
#     for vendendor in range(len(vendas)):
#         for dias in range(len(vendas[0])):
#             vendas_dia[dias] += vendas[vendas_vendedores][dias]
# ]
# print(f'total de vendas por vendendor foi de R$:')
# for i in range(len(vendas)):
#     print(f'vendendor {i+1} = R$ {vendas_vendedores[i]:.2f}')
#     print('')
#     print('total de vendas por dia foi de R$:')
#     for i in range(len(vendas)):
#         print(f'Dia {i+1} = R$ {vendas_vendedores[i]:.2f}')
#

# matriz_a = [ [1,2,3],
#              [4,5,6]
# ]
#
#
# matriz_t = [ [1,4],
#              [2,5],
#              [3,6]
# ]
#
# matriz_t = [list(coluna) for coluna in zip(*matriz_a)]
#
#
# for i in matriz_t:
#     print(f'pisiçao{i+1} tem o valor')

# exercicio da 1 - 1 dicionario de quadrado
# pessoa = {
#     'nome': 'alfredo',
#     'cidade': 'fortaelza',
#     'idade': 21
# }
#
# print('---------------------------')
# print(pessoa)

# exercicio da 1 - 2 dicionario de quadrado


# pessoa = {
#     'nome': 'alfredo',
#     'cidade': 'fortaelza',
#     'idade': 21
# }
#
# print('---------------------------')
# print(pessoa)
#
#







# exercicio da 1 - 3  dicionario de quadrado

# dicionario_de_quadrados = {}
#
# for i in range(1,6):
#     dicionario_de_quadrados.setdefault(i, i**2)
#     print(dicionario_de_quadrados)





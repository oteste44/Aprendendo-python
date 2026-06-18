# # notas = [ ['joao', 2.3, 3.3],
# #           ['mario', 5.7, 8.0],
# #           ['beto', 9.0, 7.0]
# #
# # ]
# # mediaAlunos = []
# # for i in notas:
# #     media = (i[1] + i[2])/2
# #     lista = (i[0],media)
# #     mediaAlunos.append(lista)
# # print(f'lista de notas do alunos: {notas}')
# # print(f'lista de media de alunos:{mediaAlunos}'
# #
# # estoque = [
# #
# #     [12, 5, 8],
# #
# #     [3, 15, 2],
# #
# #     [19, 0, 7]
# #
# # ]
# # prateleira = int(input('digite o numero da prateleira:'))
# # armario  = int(input('digite o numero do armario:'))
# #
# # for i in estoque:
# #     for c in estoque:
# #         print([estoque][prateleira][armario])
# # dados = {
# #     'nome': 'joao',
# #     'idade': 21,
# #     'sexo': 'M',
# #     'altura': 1.80,
# #     'temCNH': True
# # }
# #
# # dados['altura'] = 1.78
# # dados['peso'] = 92
# # dados.pop('idade')
# #
# # continuar = 's'
# # while continuar == 's':
# #     dados_pessoais = input('digite oq vc quer:')
# #     print(dados.get(dados_pessoais,'valor nao encontrado!'))
# #     continuar = input('quer continuar? (s/n):')[0].lower()
# #
# #     for dadoss,valor in dados.items():
# #         print(f'{dados_pessoais},: {valor}')
# #
# #
# #
# #
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
#
# exercicio da 1 - 1 dicionario de quadrado
# pessoa = {
#     'nome': 'alfredo',
#     'cidade': 'fortaelza',
#     'idade': 21
# }
#
# print('---------------------------')
# print(pessoa)
#
# # exercicio da 1 - 2 dicionario de quadrado
#
#
# # pessoa = {
# #     'nome': 'alfredo',
# #     'cidade': 'fortaelza',
# #     'idade': 21
# # }
# #
# # print('---------------------------')
# # print(pessoa)
# #
# #
#
#
# # exercicio da 1 - 3  dicionario de quadrado
# #
# # dicionario_de_quadrados = {}
# #
# # for i in range(1,6):
# #     dicionario_de_quadrados.setdefault(i, i**2)
# #     print(dicionario_de_quadrados)
# #
# # atividade da 1 - 5
# # palavra = {}
# # for chave in palavra:
# #     if chave not in palavra:
# #         palavra[chave] =1
# #     else:
# #         palavra[]
#
#
#
#
#
# # atividade da 1 - 6
# #
# # estoque  = {'teclado': 15, 'mouse': 22,'monitor': 8}
# #
# # print(estoque)
# # atualiza_estoque = False
# # continuar = 's'
# #
# # while continuar == 's':
# #     nome, quantidade = input('digite o que deseja e a quantidade:').split(',')
# #     for chave, valor in estoque.items():
# #         if nome == chave.lower():
# #             if valor == 0:
# #                 print('estoque esgotado')
# #
# #                 continue
# #
# #             if valor < int(quantidade):
# #                 print('estoque insuficiente!')
# #
# #                 continue
# #             else:
# #                 estoque[chave] -= int(quantidade)
# #                 atualiza_estoque = True
# #
# #     if atualiza_estoque:
# #         print('estoque atualizado')
# #         for chave, valor in estoque.items():
# #             print(f'{chave} : {valor}')
# #
# #     continuar = input('quer continuar? s/n:')[0].lower()
#
# # estoque = {}
# # carrinho = []
# # print()
# # print('-----SHOPEE-----')
# # print()
# # print('[1] Vizualizar Estoque')
# # print('[2] Adicionar Item ao Carrinho')
# # print('[3] Vizualizar Carrinho')
# # print('[4] Finalizar Compra')
# # print('[0] Sair do Sistema')
# #
# # opcao = int(input('digite sua opcao:'))
# #
# # def criar_produto(produto,quantidade,valor):
# #     return  {
# #             'produto' : produto,
# #             'quantidade': quantidade,
# #             'preço': valor
# #         }
# # estoque = {
# #     1:criar_produto('Monitor Husky 240hz',14,899.99),
# #     2:criar_produto('Mouse redragon',25,249.99),
# #     3:criar_produto('Gabinete dark flash',10,339.99),
# #     4:criar_produto('Teclado attack shark',9,449.90)
# #     }
# #
# # def mostrar_estoque():
# #     print('\n----SHOPEE----')
# #     print(f'{'id':<5}{'produto':<15}{'preço':<10}{'qtd'}')
# #     print(f"{id_produto:<5}{dados['produto']:<25}R$ {dados['preço']:<12.2f}{dados['quantidade']}")
# #
# #
# # def adicionar_carrinho():
# #     mostrar_estoque()
# #
# #     try:
# #         id_produto = int(input('digite o id do produto:'))
# #         quantidade = int(input('digite a quantidade do produto:'))
# #
# #         if id_produto not in estoque:
# #             print('produto nao encontrado:')
# #             return
# #
# #         produto = estoque[id_produto]
# #
# #         if quantidade > produto['quantidade']:
# #             print('estoque insuficiente')
# #             return:
# #
# #
# #     print(f"{produto['nome']} adicionado ao carrinho!")
# #
# #
# # def visualizar_carrinho():
# #     if not carrinho:
# #         print("\nCarrinho vazio.")
# #         return
# #
# #     print("\n--- CARRINHO ---")
# #     total = 0
# #
# #     for item in carrinho:
# #         subtotal = item["preco"] * item["quantidade"]
# #         total += subtotal
# #
# #         print(f"{item['nome']} | {item['quantidade']}x R$ {item['preco']:.2f} = R$ {subtotal:.2f}")
# #
# #     print(f"\nSubtotal: R$ {total:.2f}")
#
#
#
#
#

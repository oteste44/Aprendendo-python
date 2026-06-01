#
# Exercício 01 - O Analista de Números
# Enunciado: Desenvolva um script que peça para o usuário digitar 6 números inteiros e os armazene em uma lista. Ao final, o programa deve exibir:
#
# A lista completa na ordem em que foi digitada.
# A soma de todos os valores da lista.
# O maior e o menor valor presente na lista.
# Exercício 2: Média de Notas com Validação
# Enunciado: Escreva um programa que receba 4 notas de um aluno, armazene-as em uma lista e calcule a média aritmética. Se a média for maior ou igual a 7.0, exiba a lista de notas e a mensagem "Aprovado". Caso contrário, exiba "Recuperação".
# Exercício 3: O Separador de Pares e Ímpares
# Enunciado: Crie um programa que leia 10 números inteiros do teclado e os armazene em uma lista principal. Depois, o programa deve criar duas novas listas vazias: pares e impares. Varra a lista principal e mova cada número para a sua respectiva lista de acordo com a sua paridade. No final, exiba as três listas
# Exercício 4: Verificador de Maioridade da Turma (Intermediário)
# Enunciado:  Desenvolva um programa que leia o ano de nascimento de 7 pessoas. Utilizando o for, o programa deve calcular a idade de cada uma com base no ano atual (2026) e, no final, exibir quantas pessoas já atingiram a maioridade (18 anos ou mais) e quantas ainda são menores.
# Exercício 5: Validador de Senhas e Tentativas (Intermediário)
# Enunciado: Um sistema de segurança permite que o usuário tente digitar sua senha de acesso no máximo 3 vezes. Crie um loop for que execute 3 vezes pedindo a senha. Se o usuário digitar a senha correta (defina uma senha padrão no código), o programa deve exibir "Acesso Permitido" e interromper o laço imediatamente usando o break. Se as 3 tentativas falharem, exiba "Conta Bloqueada".
# Exercício 6: Buscador de E-mails Institucionais (Intermediário)
# Enunciado: Imagine que você tem uma lista de e-mails misturados: emails = Utilizando o for, percorra a lista e exiba no terminal apenas os e-mails que pertencem ao domínio institucional do Senac .
# Exercício 7: Validação de Nota Básica (while)
# Enunciado: Escreva um programa que peça para o usuário digitar uma nota entre 0 e 10. Se ele digitar um valor inválido (como 12 ou -2), o programa deve exibir uma mensagem de erro e continuar pedindo a nota até que o usuário digite um valor válido.
# Exercício 8: O Contador Regressivo de Lançamento (while)
# Enunciado: Crie um script que simule a contagem regressiva para o lançamento de um foguete. O programa deve começar em 10 e ir até 0, aguardando 1 segundo entre cada número (Dica: use a função time.sleep(1) da biblioteca time). Ao final, exiba a mensagem: "Decolar!".
# Exercício 9: Menu Interativo de Sistema (Simulando do while)
# Enunciado: Crie um menu interativo de calculadora utilizando while True. O programa deve exibir na tela:
#
# Subtrair
# Somar
# Multiplicar
# Dividir
# Sair
# O programa deve executar a ação escolhida e mostrar o menu novamente. Ele só deve encerrar de verdade quando o usuário digitar a opção 5.
# Exercício 10: Jogo da Adivinhação (while)
# Enunciado: O computador deve "pensar" em um número secreto entre 1 e 20 (Dica: use random.randint(1, 20)). O usuário deve tentar adivinhar. Enquanto o usuário errar, o programa deve dizer se o número secreto é maior ou menor que o palpite digitado. O laço encerra quando o usuário acertar.
# Exercício 11: O Caixa Eletrônico / Saque de Cédulas (while)
# Enunciado: Crie um programa que simule o funcionamento de um caixa eletrônico. O usuário informa o valor que deseja sacar (número inteiro). O programa deve calcular quantas cédulas de cada valor serão entregues, priorizando as maiores. Considere que o banco possui cédulas de R$ 50, R$ 20, R$ 10 , 5 R$ e R$ 2.
#
# Exemplo: Saque de R$ 82 ➔ 1cédula de R$ 50, 1 de R$ 20, 1 de R$ 10 e 1 de R$ 2.
# Exercício 12: Análise de Dados Estatísticos de um Grupo (Simulando do while)
# Enunciado: Construa um script que leia a idade e o sexo (M/F) de várias pessoas. A cada pessoa cadastrada, o programa deve perguntar se o usuário quer continuar. No final do programa, mostre:
#
# Quantas pessoas têm mais de 18 anos.
# Quantos homens foram cadastrados.
# Quantas mulheres têm menos de 20 anos.
# Exercício 13: Carrinho de Compras
# Enunciado: Desenvolva um simulador simplificado de carrinho de compras. O programa deve ter uma lista vazia chamada carrinho. Usando um laço while, permita que o usuário adicione nomes de produtos ao carrinho até que ele digite a palavra "sair". Ao encerrar, exiba a lista de produtos ordenada alfabeticamente.
# Exercício 14: Análise de Desempenho de Vendas
# Enunciado: Uma empresa monitora as vendas mensais de seus analistas através de uma lista de valores float: vendas = [1200.50, 3400.00, 980.00, 5600.20, 2100.00, 850.00]. Crie um script que percorra essa lista e gere uma nova lista contendo apenas as vendas que foram acima da média de faturamento da equipe.
# Exercício 15: Removendo Duplicatas de um Banco de Dados
# Enunciado: Simulando a limpeza de dados de um sistema migrado, você recebeu uma lista com IDs de clientes que contém elementos duplicados devido a falhas no sistema anterior: ids_clientes = [101, 102, 103, 101, 104, 102, 105, 106, 103]. Escreva um algoritmo que remova todos os elementos duplicados dessa lista, mantendo apenas uma ocorrência de cada ID, pode utilizar a função set().
# Exercício 16: O Tabuleiro de Notas (Matrizes / Listas Compostas)
# Enunciado: Crie uma estrutura onde cada elemento da lista principal seja uma sublista contendo o nome de um aluno e suas duas notas.
#
# Exemplo de estrutura: turma = [ ["Ana", 8.0, 9.0], ["Pedro", 5.5, 6.0], ["Carlos", 7.5, 7.0] ]
# O programa deve percorrer essa lista composta, calcular a média de cada aluno e imprimir no terminal no formato: "Aluno(a) [Nome] obteve média [Valor da Média]".
#
# Exercício 17: A Tabuada Automatizada
# Enunciado: Desenvolva um programa que peça para o usuário digitar um número inteiro. Utilizando o laço for e a função range(), exiba a tabuada desse número de 1 a 10 no terminal.
#
# Exemplo de saída esperada: 5 x 1 = 5, 5 x 2 = 10...
#
# Exercício 18: Contador de Intervalos Customizado (Básico)
# Enunciado: Escreva um script que solicite três valores ao usuário: um valor inicial, um valor final e um valor de passo (de quanto em quanto a contagem deve andar). Use o laço for para exibir a contagem na tela.
#
# Exemplo: Inicial: 2, Final: 12, Passo: 3. Saída: 2, 5, 8, 11.
#
# Exercício 19: Somador de Números até o Zero (while)
# Enunciado: Desenvolva um programa que peça para o usuário digitar vários números inteiros. O programa deve somar todos esses números. A repetição só deve parar quando o usuário digitar exatamente o número 0. No final, exiba a soma total.
#
# Exercício 20: O Somador de Números Ímpares
# Enunciado: Crie um programa que calcule e exiba a soma de todos os números ímpares que são múltiplos de 3 e que se encontram no intervalo de 1 até 100.

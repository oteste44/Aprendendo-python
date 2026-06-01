while True:
    print('(1) Somar')
    print('(2) Subtrair')
    print('(3) Multiplicar')
    print('(4) Dividir')
    print('(5) Sair')

    option = input('Digite sua opção: ')

    if option == '5':
        print('Saindo...')
        break

    if option not in ['1', '2', '3', '4']:
        print('Opção inválida!')
        continue

    num1 = float(input('Digite um número: '))
    num2 = float(input('Digite outro número: '))

    if option == '1':
        print('Resultado:', num1 + num2)

    elif option == '2':
        print('Resultado:', num1 - num2)

    elif option == '3':
        print('Resultado:', num1 * num2)

    elif option == '4':
        if num2 == 0:
            print('Não é possível dividir por zero!')
        else:
            print('Resultado:', num1 / num2)
        print('Resultado:')



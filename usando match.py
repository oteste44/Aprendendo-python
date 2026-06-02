while True:
    print('(1) Somar')
    print('(2) Subtrair')
    print('(3) Multiplicar')
    print('(4) Dividir')
    print('(5) Sair')

    opcao = int(input('Qual sua opçao?'))

    match opcao:
        case 1:
            num1 = float(input('digite seu numero:'))
            num2 = float(input('digite outro numero:'))
            print('-----------------------')
            print('Resultado:', num1 + num2)
        case 2:
            num1 = float(input('digite seu numero:'))
            num2 = float(input('digite outro numero:'))
            print('------------------------')
            print('resultado e:', num1 - num2)

        case 3:
            num1 = float(input('digite seu numero:'))
            num2 = float(input('digite outro numero:'))
            print('-------------------------')
            print('resultado e:', num1 * num2)

        case 4:
            num1 = float(input('digite seu numero:'))
            num2 = float(input('digite outro numero:'))
            print('-------------------------')
            print('resultado e:', num1 / num2)

        case 5:
            print('SAINDO.....')
            break












































while True:
    print('(1) DOMINGO')
    print('(2) SEGUNDA')
    print('(3) TERÇA')
    print('(4) QUARTA')
    print('(5) QUINTA')
    print('(6) SEXTA')
    print('(7) SABADO')

    opcao = int(input('DIGITE O DIA DESEJADO:'))

    print('---------------------')


    match opcao:
        case 1:
            print('DOMINGO')
            print('---------------------')


        case 2:
            print('SEGUNDA')
            print('---------------------')


        case 3:
            print('TERÇA')
            print('---------------------')

        case 4:
            print('QUARTA')
            print('---------------------')

        case 5:
            print('QUINTA')
            print('---------------------')

        case 6:
            print('SEXTA')
            print('---------------------')

        case 7:
            print('SABADO')
            print('---------------------')

        case _:
            print('DIA INVALIDO')
            print('---------------------')
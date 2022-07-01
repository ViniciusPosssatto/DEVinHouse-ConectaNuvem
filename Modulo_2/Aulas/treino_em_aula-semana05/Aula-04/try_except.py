def calcula_valores():

    print('Digite dois valores a serem calculados: ')
    try:
        y = int(input('1º >'))
        x = float(input('2º >'))
        media = (x + y) / 2

        # if media == int:
        #     print(media)
        # else:
        #     print('deu ruim')

    except Exception as error:
        print(error)
        calcula_valores()

    else:
        print(f'A média é {media}')

    finally:
        print('Execução terminada.')


if __name__ == "__main__":
    calcula_valores()

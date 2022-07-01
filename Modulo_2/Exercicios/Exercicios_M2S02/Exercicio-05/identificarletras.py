# identificar se é vogal ou consoante em loop

vogal = ['a', 'e', 'i', 'o', 'u']
parar = False

while parar != True:
    print('Digite uma letra ou sair para parar o programa.')
    inp = input('Digite uma letra: ').lower()
    if inp not in vogal:
        print(10 * '-=')
        print('Essa letra não é uma vogal!')
    if inp == 'sair':
        parar = True
        print(10 * '-=')
        print('Saindo do progrma...')
    else:
        print(10 * '-=')
        print('Essa letra é uma vogal.')

print(10 * '-=', 'Fim')

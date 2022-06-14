# desenvolvendo o jogo a forca

from random import choice
import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

file = open('palavras.txt', 'r')
lista = file.readlines() # pega oque tiver no arquivo
file.close()

palavra = choice(lista).split('\n')[0].lower() # escolhe uma palavra que veio la do outro arquivo (separa ela pelo quebra linha e  deixa minusculo)

lista_letras = []
lista_traco = []
lista_erro = []
tentativas = []
acertos = 0

for i in range(len(palavra)):
    lista_letras.append(palavra[i])
    lista_traco.append('_')

# print(lista_letras)
# print(lista_traco)

print(10 * '=-', 'JOGO DA FORCA', 10 * '-=' )


# Informar se acertou ou se errou 10 vezes
while True:
    cls()
    if acertos == len(lista_letras):
        print('Parabéns. Você ganhou!')
        print(f'A palavra é \"{palavra}".')
        break
    
    print(lista_traco)
    print('Tentativas: ' + str(tentativas))
    print('Erros: ' + str(lista_erro))

    chute = input('Digite [1] para chutar uma letra e [2] para adivinhar a palavra: ')

    if chute == '1':
        
        letra = input('Informe uma letra para tentar: ')
    
        tentativas.append(letra)
        
        c = lista_letras.count(letra) # contagem das letras (se não tiver, retorna 0)
        if c > 0:
            print('Você acertou a letra {}.'.format(letra))

            _index = 0

            for i in range(0, c): # para verificar se existem mais de 1 letra igual
                _index = lista_letras.index(letra, _index)
                lista_traco[_index] = letra
                _index += 1
                acertos += 1
            
            continue

        print('A letra {} não está presente na palavra.'.format(letra))
        lista_erro.append(letra)

        if len(lista_erro) == 10:
            print('Você perdeu! Errou mais de 10 vezes...')
            break

        else:
            continue

    elif chute == '2':
        print('Lembre-se: Se errar já era!!!')
        palavra_chutada = input('Informe uma letra para tentar: ').strip().lower()

        if palavra_chutada == palavra:
            print('Parabéns, você acertou a palavra inteira! < Medalinha pra você >')
            break
        else:
            print('Você errou a palavra e PERDEU!')
            break
    else:
        continue

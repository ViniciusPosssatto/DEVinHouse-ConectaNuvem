# Faça um algoritmo que:

# Receba dois valores do usuário (X e Y);
# Retorne o tamanho de cada valor inserido;
# Concatene os valores inseridos e retorne esse novo valor (Z);
# Repita o primeiro valor em inserido por tres vezes e retorne esse valor;
# Valide se X está contido Z e se Y está contido em Z;
# Imprima a primeira posição de X e a última posição de Y;


x = str(input('Digite uma palavra: ')).strip()
y = str(input('Digite outra palavra: ')).strip()

print(f'A primeira palavra tem {len(x)} letras e a segunda tem {len(y)} letras.')

z = x + y

print(f'As duas palavras juntas tem {len(z)} letras.')

print(f'A primeira palavra 3 vezes fica: {x * 3}')
if x in z and y in z:
    print('As duas palavras estão juntas.')
elif x not in z:
    print(f'A palavra {x} não está.')
elif y not in z:
    print(f'A palavra {y} não está.')

print(f'A primeira letra de {x} é {x[0]} e a última letra de {y} é {y[-1]}.')

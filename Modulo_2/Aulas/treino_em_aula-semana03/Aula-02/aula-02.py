# sequencia fibonacci

print(15 * '-=')
print('Sequência de FIBONACCI')
print(15 * '-=')
num = int(input('Quantos termos deseja mostrar: '))

t1 = 0
t2 = 1

print(15 * '-=')
print('{} -> {}'.format(t1, t2), end='')

count = 3
while count <= num:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    count += 1
print(' -> FIM')
print(15 * '-=')

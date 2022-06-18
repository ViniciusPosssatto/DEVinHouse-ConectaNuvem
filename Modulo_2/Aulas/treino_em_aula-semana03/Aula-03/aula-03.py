# Dicionários

dicionario = {'chave': 'valor'}

print(type(dicionario))

lista_1 = ['nome', 'sobrenome', 'idade']
lista_2 = ['Natan', 'Nascimento', 23]

lista_completa = dict(zip(lista_1, lista_2))

print(lista_completa)

lista_completa['nome'] = 'Marcelo' # altera o valor da chave 

print(lista_completa)

lista_completa.get('idade') # pega o valor da chave passada por parâmetro

lista_completa.pop('nome') # remove a chave e os valores passados por parâmetro

lista = {'nome': 'Kaua', 'sobrenome': 'Kisrchner', 'idade': {'nome': 'Kaua', 'sobrenome': 'Kisrchner', 'idade': 23}}

lista['idade']['nome'] # vai retornar o valor do item dentro da idade com a chave 'nome'

lista.popitem() # retira uma chave e o valor dela (pelo teste, ele retira a ultima chave)

print(lista)

# Alterando mais de um valor

lista.update({'nome': 'Marcos', 'idade': 25})

print(lista)

# Pegar 2 valores

print(lista['nome'], lista['idade'])

##### DICT comprehension

num = {x for x in range(20)} # vai retornar os numeros do 0 ao 19
print(num)

# -------------------->>>>>>>>>>>    As chaves de um dicionario nunca serão iguais

# outro exemplo

num = {x : x + 2 for x in range(20)}
print(num)

# para deixar as chaves diferentes dos valores (nesse caso as chaves serão strings):

num = {f'{x}' : x + 2 for x in range(20)} #ou num = {str(x) : x + 2 for x in range(20)}
print(num)

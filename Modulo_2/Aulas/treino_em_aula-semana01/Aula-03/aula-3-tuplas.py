tupla = 12,

tupla = ('elemento', 'elemento2')

tupla = (12, 4, 56)
#ou
tupla = ([1, 3, 6,], [4, 2, 6, 8])

from collections import namedtuple

Estados = namedtuple('Estados', ['sigla', 'nome'])

estado_rj = Estados('rj', 'rio de janeiro')

print()

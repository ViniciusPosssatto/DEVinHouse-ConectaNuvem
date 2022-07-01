# Defina um dicionário com dados referente a informações de usuário, 
# em um primeiro momento esse dicionário deve conter primeiro nome, segundo nome e idade. 
# Caso queira, adicione novas chaves no dicionário. Após a definição do dicionário, 
# adicione novos dados à aquela chave e imprima o dicionário.

# Retorno esperado:
# {'primeiro_nome': '', 'segundo_nome': '', 'idade': ''}
# {'primeiro_nome': 'Natan', 'segundo_nome': '', 'idade': ''}
# {'primeiro_nome': 'Natan', 'segundo_nome': 'Nascimento', 'idade': ''}
# {'primeiro_nome': 'Natan', 'segundo_nome': 'Nascimento', 'idade': '23'}


dicionario = { 'nome': '', 'sobrenome': '', 'idade': '', 'cidade': ''}

dicionario['nome'] = 'Romário'

dicionario['sobrenome'] = 'Silva'

dicionario['idade'] = 23

dicionario['cidade'] = 'Floripa'

print(dicionario)

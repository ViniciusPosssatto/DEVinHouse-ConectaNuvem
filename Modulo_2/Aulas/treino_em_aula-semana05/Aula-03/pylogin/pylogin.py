from os.path import dirname, relpath, join
#  from getpass import getpass
from lib.lib import JsonManager
from textwrap import dedent


class PyLogin(JsonManager):

    def __init__(self):
        self.root = dirname(relpath(__file__))
        self.path_json = join(self.root, 'data/arquive_json.json')

    def sign_in(self):
        print(' Sign in '.center(50, '_'))
        username = str(input('Digite seu username: '))
        #  password = getpass(prompt='Password', stream=None)
        password = int(input('Digite sua senha: '))
        password_verify = int(input('Digite novamente: '))

        while password != password_verify:
            print('Password não coincidem...')
            password_verify = int(input('Digite novamente: '))

        JsonManager().create_arquive_json(self.path_json, username, password_verify)
        print('Registro concluído.')

    def loggin_in(self, data):
        print(' Realizar Login '.center(50, '_'))
        username = input('Coloque seu usuário: ')

        while username != data['username']:
            print('Erro! Usuário inválido.')
            username = input('Repita seu usuário: ')

        password = input('Digite sua senha: ')
        while password != data['password']:
            print('Erro! Senha incorreta.')
            password = input('Repita sua senha: ')

        if username == data['username'] and password == data['password']:
            print('Login realizado com sucesso!')
            self.home(data)
        else:
            print('Erro! Login inválido.')

    def home(self, data):
        opc = ' '
        while opc != 0:
            print(dedent("""
                Menu:
                [1] Alterar login
                [0] Sair
            """))
            opc = int(input('Ecolha a opção: '))
            if opc == 1:
                try:
                    self.update_login(data)
                except KeyboardInterrupt:
                    print('\nSaiu do sitema.')
            if opc == 0:
                print('Saindo do sistema...')

    def update_login(self, data):
        print(' Alterar dados de Login '.center(50, '_'))
        username = input('Digite seu novo usuário: ')

        password_old = input('Digite sua senha anterior: ')
        while password_old != data['password']:
            print('Erro! Senha incorreta.')
            password_old = input('Repita sua senha: ')

        password_new = input('Digite sua NOVA senha: ')
        password_new_verify = input('Digite novamente sua NOVA senha: ')
        while password_new_verify != password_new:
            print('Erro! Senha incorreta.')
            password_new_verify = input('Repita sua senha: ')

        data['username'] = username
        data['password'] = password_new_verify

        JsonManager().update_json(self.path_json, data)

        print('Dados alterados com sucesso!')

    def main(self):
        data = JsonManager().read_arquive_json(self.path_json)

        if data:
            try:
                self.loggin_in(data)
            except KeyboardInterrupt:
                print('\nSaiu do sitema.')
        else:
            try:
                self.sign_in()
            except KeyboardInterrupt:
                print('\nSaiu do sitema.')


if __name__ == '__main__':
    um = PyLogin()
    um.main()

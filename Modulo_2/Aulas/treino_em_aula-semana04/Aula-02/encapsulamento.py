class Conta:
    def __init__(self, nome, agencia, conta):
        self.agencia = agencia
        self.conta = conta
        self.nome = nome
        # o dander faz a privação da propriedade
        self.__saldo = 0

    @property
    def saldoemConta(self):
        return self.__saldo

    @saldoemConta.setter
    def saldo(self):
        raise ValueError('Impossivel alterar saldo diretamente. Use a função depositar ou sacar.')

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor


conta = Conta('Yan', '001', '02345')
conta.depositar(2000)
print(f'O saldo da conta é: R${conta.saldo}')
conta.sacar(450)
print(f'O saldo depois do saque é: R$ {conta.saldo}')

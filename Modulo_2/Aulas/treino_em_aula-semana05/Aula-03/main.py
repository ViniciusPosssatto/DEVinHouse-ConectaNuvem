from abc import ABC, abstractmethod

class Pagamento(ABC):

    @abstractmethod
    def pagar(self):
        print('Pagamento')


class PagarCartaoCredito(Pagamento):

    # def pagar(self):
        pass

if __name__ == "__main__":
    PagarCartaoCredito().pagar()
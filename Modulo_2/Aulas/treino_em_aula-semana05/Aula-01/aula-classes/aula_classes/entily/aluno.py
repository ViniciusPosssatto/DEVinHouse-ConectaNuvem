class Aluno:

    def __init__(self, nome: str, dia_nasc: int, mes_nasc: int, ano_nasc: int, matricula: int, cpf: str):

        self.__nome: nome
        self.__dia_nasc: dia_nasc
        self.__mes_nasc = mes_nasc
        self.__ano_nasc = ano_nasc
        self.__matricula = matricula
        self.__cpf = cpf
        self.nota_final = None

    def get_info(self):
        keys = ["nome", "dia_nasc", "mes_nasc", "ano_nasc", "matricula", "cpf", "media"]
        values = [self.__nome, self.__dia_nasc, self.__mes_nasc, self.__ano_nasc, self.__matricula, self.__cpf]
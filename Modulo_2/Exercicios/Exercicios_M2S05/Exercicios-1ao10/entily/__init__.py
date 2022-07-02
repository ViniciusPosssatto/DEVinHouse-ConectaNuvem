from entily.agenda.cls_agenda import Agenda
from entily.pessoas.cls_pessoa import Pessoa
from entily.pessoas.cls_medico import Medico
from entily.pessoas.cls_paciente import Paciente
from entily.endereco.cls_endereco import Endereco


if __name__ == "__main__":

    med = Medico('clau', 'aas@sas.com', 234324, 234234, 234234)
    pac = Paciente('vineh', 'vineh@email.com', 11111, "3333333", 23423432, True, "22/234/23432")
    age = Agenda(12312312, '2355555553', 12, 3, 1222, '14:24:02', "nada a declarar")

    pac.cadastrar_paciente()
    pac.exibir_pessoa()

    med.cadastrar_medico()
    med.exibir_pessoa()

    age.cadastrar_agenda()
    age.exibir_agenda()

    endereco_ = Endereco()
    endereco_.cadastrar_endereco()
    endereco_.exibir_endereco()

class Funcionario:
    def __init__(self, salario, aumento, demitir):
        self.salario = salario
        self.aumento = aumento
        self.demitir = demitir
    
 
class Dev(Funcionario):
    def __init__(self, salario, aumento, demitir):
        super().__init__(salario, aumento, demitir)

class Designer(Funcionario):
    def __init__(self, salario, aumento, demitir):
        super().__init__(salario, aumento, demitir)
    
class GerenMarketing(Funcionario):
    def __init__(self, salario, aumento, bonificacao, demitir):
        self.bonicacao = bonificacao
        super().__init__(salario, aumento, demitir)

    def bonific(self):
        (self.aumento + self.bonicacao) / 100 * self.salario

func_dev = (3500, 5, False)
func_des = (3500, 5, True)
func_gerent = (3500, 5, 10, False)

     


print(f'O salário completo do desenvolvedor será de R${Funcionario.aumentoSalario(5)}')
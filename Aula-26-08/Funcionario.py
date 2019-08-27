class Funcionario:

    def __init__(self, nome, cpf, salario):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario

    # outros métodos e propertis

    def get_bonificacao(self):
        return self._salario * 0.10
    
    def getSalary(self):
        return self._salario

    def setBaseSalary(self, salario):
        self._salario = salario
        return self._salario

class Gerente(Funcionario):

    def __init__(self, nome, cpf, salario, senha, qtd_funcionarios):
        super().__init__(nome, cpf, salario)
        self._senha = senha
        self._qtd_funcionarios = qtd_funcionarios

    def get_bonificacao(self):
        return self._salario * 0.30

class ControleDeBonificacoes:
    def __init__(self, total_bonificacoes=0):
        self._total_bonificacoes = total_bonificacoes

    def registra(self, funcionario):
        self._total_bonificacoes += funcionario.get_bonificacao()

    @property
    def total_bonificacoes(self):
        return self._total_bonificacoes


if __name__ == '__main__':
    funcionario = Funcionario('João', '222222222-11', 2000.0)

    # print("bonificacao funcionario: {}".format(funcionario.get_bonificacao()))

    gerente = Gerente("José", "222222222-22", 5000.0, '1234', 0)
    # print("bonificacao gerente: {}".format(gerente.get_bonificacao()))

    aux = [funcionario, gerente]
    aux[0].setBaseSalary(20000)
    for value in aux:
        print(value.getSalary())

    
    # controle = ControleDeBonificacoes()
    # controle.registra(funcionario)
    # controle.registra(gerente)

    # print("total: {}".format(controle.total_bonificacoes))

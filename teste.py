from abc import ABCMeta, abstractmethod
from datetime import datetime, timezone
from pytz import timezone
import re

class Funcionario(metaclass=ABCMeta):
    def __init__(self, nome, cpf, salario, telefone):
        self.nome = nome.strip()
        self.cpf = self.sanitiza_cpf(cpf)
        self.valida_cpf()
        self.salario = self.verifica_salario(salario)# salario minimo
        self._telefone = self.sanitiza_telefone(telefone)
        self.valida_telefone()

    def sanitiza_telefone(self, telefone):
        if type(telefone) == str:
            return telefone
        else:
            return str(telefone)


    def valida_telefone(self):
        if not self._telefone:
            raise ValueError("O telefone está vazio!")
        padrao_telefone = re.compile('[0-9]{5}[-]?[0-9]{3}')  # tem q colocar parenteses em strings pq
        match = padrao_telefone.match(
            self._telefone)  # colchetes significa que é pode ser qualquer UM so elementos nos COLCHETES
        if not match:
            raise ValueError("O telefone está ERRADO!")

    def verifica_salario(self, salario):
        if type(salario) == float and salario >= 1.100:
            return salario
        else:
            raise TypeError("tem que ser um numero e acima do salario MINIMO")

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        if not isinstance(novo_nome, str):
            raise TypeError("O nome tem que ser um texto!")
        self._nome = novo_nome.title()

    def bater_ponto(self):
        data_e_hora_atuais = datetime.now()
        fuso_horario = timezone('America/Sao_Paulo')
        data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
        data_e_hora_sao_paulo_em_texto = data_e_hora_sao_paulo.strftime('Dia:%d Mes:%m Ano:%Y \n Hora:%H Minutos:%M  Segundo:%S')

        print(f"Olá {self.nome}, você bateu o ponto:\n {data_e_hora_sao_paulo_em_texto} ")

    def sanitiza_cpf(self, cpf):
        if type(cpf) == str:
            return cpf
        else:
            return str(cpf)

    def mostar_cpf(self):
        print(f'O seu cpf é {self.cpf}')

    def sanitiza_nome(self, nome):
        if type(nome) == str:
            return nome.strip().title()
        else:
            return ""

    def valida_cpf(self):
        if not self.cpf:
            raise ValueError("O CPF está vazio!")
        padrao_cpf = re.compile('[0-9]{3}[.]?[0-9]{3}[.]?[0-9]{3}[-]?[0-9]{2}')#tem q colocar parenteses em strings pq
        match = padrao_cpf.match(self.cpf)                                           # colchetes significa que é pode ser qualquer UM so elementos nos COLCHETES
        if not match:
            raise ValueError("O CPF está ERRADO!")

    @abstractmethod
    def mostar_salario(self):
        print('O seu salário é ', self.salario)


    def __str__(self):
        return  f'Nome: {self.nome} ,CPF: {self.cpf} ,Salario: {self.salario}'


    def salario_novo(self, novo_salario):
        self.salario = novo_salario

class Programador(Funcionario):
    def __init__(self, nome, cpf, salario, telefone, funcao, linguagem):
        super().__init__(nome, cpf, salario,telefone)
        self.funcao = funcao
        self.linguagem = linguagem

    def __str__(self):
        return  f'Nome: {self.nome} ,CPF: {self.cpf} ,Salario: {self.salario} ,' \
                f' Funcao: {self.funcao} , Linguagem: {self.linguagem}'

    def mostrar_programas(self):
        print('Mostrando os programas, Programador {}'.format(self.nome))

    def mostar_salario(self):
        print(f'O seu salário é {self.salario}')


class Gerente(Funcionario):
    def __init__(self, nome, cpf, salario, telefone, departamento):
        super().__init__(nome, cpf, salario,telefone)
        self.departamento = departamento

    def __str__(self):
        return  f'Nome: {self.nome} ,CPF: {self.cpf} ,Salario: {self.salario} ,' \
                f' Departamento: {self.departamento}'

    def mostrar_tarefas(self):
        print('Mostrando as atividades, Gerente {}'.format(self.nome))

    def busca_perguntas_sem_resposta(self):
        print('Mostrando perguntas sem respostas do fórum')

    def mostar_salario(self):
        print('O seu salário é {}'.format(self.salario))



print("--------------------------------------------")
matheus = Gerente('Matheus', '123.456.789-12', 16.666, '12345-123', "programacao")
matheus.busca_perguntas_sem_resposta()
matheus.mostar_salario()
matheus.mostar_cpf()
matheus.bater_ponto()
matheus.mostrar_tarefas()
matheus.salario_novo(20.000)
matheus.mostar_salario()
print('-----------------------------')
roberto = Programador("roberto", "123.457989-45", 1.100, '12345123', "debugger", "python")
roberto.mostar_salario()
roberto.bater_ponto()
roberto.mostar_cpf()
roberto.salario_novo(3.0)
roberto.mostar_salario()




from abc import ABC, abstractmethod
import os
os.system('cls || clear')

class Funcionario(ABC):
    def __init__(self, nome: str, idade: int, salario: float, email: str, endereco: str) -> None:
        self.nome = nome
        self.idade = idade
        self.salario = salario
        self.email = email
        self.endereco = endereco

    @abstractmethod
    def salario_final(self) -> float:
        pass


class Endereco(Funcionario):
    def calcular_salario(self) -> float:
        logradouro: str
        numero: str
        complemento: str
        cep: str
        cidade: str

class Engenheiro(Funcionario):

class Medico(Funcionario):



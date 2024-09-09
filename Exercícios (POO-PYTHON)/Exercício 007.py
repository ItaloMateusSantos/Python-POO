import os
from enum import Enum
os.system('cls || clear')

class Setor(enumerate):
      FINANCEIRO = 'Financeiro'
      RECURSOS_HUMANOS = 'Recursos humanos'
      VENDAS = 'Vendas'
      MARKETING = 'Marketing'

class Sexo(enumerate):
      MASCULINO = 'Masculino'
      FEMININO = 'Feminino'

class Funcionario:
    def __init__(self, id: int, nome: str, idade: int, salario: float, setor: Setor, sexo: Sexo) -> None:
            self.id = id
            self.nome = nome
            self.idade = idade
            self.salario = salario
            self.setor = setor
            self.sexo = sexo

    def __str__(self) -> str:
          return (f'\nID: {self.id}'
                 f'\\nNome: {self.nome}'
                 f'\nIdade: {self.idade}'
                 f'\nSalário: {self.salario}'
                 f'\nSetor: {self.setor.value}'
                 f'\nSexo: {self.sexo.value}'
                )


pessoa_1 = 
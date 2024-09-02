import os
os.system ('cls || clear')

class Aluno:
    def __init__(self, nome: str, idade: int) -> None:

        self.nome = nome
        self.idade = idade

    def exibir_dados:
        return(f'None: {self.nome} \nIdade: {self.idade}')

aluno = Aluno('Marta', 25)

print(f'Nome: {aluno.nome}')
print(f'Idade: {aluno.idade}')
print(aluno.exibir_dados())
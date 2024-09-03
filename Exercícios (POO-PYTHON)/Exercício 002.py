import os
os.system('cls || clear')

#Objeto em Python_____________________________________________________________________
class Livro:
#O possível Getter and Setter em Python_______________________________________________
    def __init__(self, titulo: str, autor: str, numero_paginas: int, preco):
        self.titulo = titulo
        self.autor = autor
        self.numero_paginas = numero_paginas
        self.preco = preco

#O possível Getter and Setter em Python_______________________________________________
    def __str__(self):
        return  (f'Título: {self.titulo} \n'
                f'Autor: {self.autor} \n'
                f'Número de páginas: {self.numero_paginas}\n'
                f'Preço: {self.preco:.2f}')

#O possível construtor em Python______________________________________________________
def main():
    Livro1 = Livro('O homem mais rico da Babilonia', 'Arquimade', 350, 35.90)
    Livro2 = Livro('Maravilhos mundo novo', 'Desconheço', 200, 40.00)

#Exibição dos dados___________________________________________________________________
    print('Informações Livro 01: \n')
    print(Livro1)

    print('Informações Livro 02: \n')
    print(Livro2)

if __name__ == '__main__':
    main()



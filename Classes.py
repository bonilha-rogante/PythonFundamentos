

# class Funcionarios:
#     nome = 'Guilherme'
#     sobrenome = 'Bonilha'
#     data_nasc = '22/01/1992'


# usuario1 = Funcionarios()

# print(usuario1.nome)
# print(usuario1.sobrenome)
# print(usuario1.data_nasc)

# # Criar classe
# class Funcionarios:
#     pass


# # Criar o objeto
# usuario1 = Funcionarios()
# usuario2 = Funcionaios()

# # Criar os parametros
# usuario1.nome = 'Carlos'
# usuario1.sobrenome = 'Almeida'
# usuario1.data_nasc = '28/02/1997'

# usuario2.nome = 'Carol'
# usuario2.sobrenome = 'Silva'
# usuario2.data_nasc = '15/10/2005'


# Criar classe

# class Funcionarios:
#     def __init__(self, nome, sobrenome, data_nasc):
#         self.nome = nome
#         self.sobrenome = sobrenome
#         self.data_nasc = data_nasc

# usuario1 = Funcionarios('Elena', 'Cabral', '12/01/2009')
# usuario2 = Funcionarios('Carol', 'Silva', '15/10/2005')


# class Funcionarios:
#     def __init__(self, nome, sobrenome, data_nasc):
#         self.nome = nome
#         self.sobrenome = sobrenome
#         self.data_nasc = data_nasc

#     def nome_completo(self):
#         return self.nome + ' ' + self.sobrenome


# usuario1 = Funcionarios('Elena', 'Cabral', '12/01/2009')
# usuario2 = Funcionarios('Carol', 'Silva', '15/10/2005')


# print(usuario1.nome_completo())
# print(Funcionarios.nome_completo(usuario1))


from datatime import datetime


class Funcionarios:

    def __init__(self, nome, sobrenome, ano_nasc):
        self.nome = nome
        self.sobrenome = sobrenome
        self.ano_nasc = ano_nasc

    def nome_completo(self):
        return self.nome + ' ' + self.sobrenome

    def idade_funcionario(self):
        ano_atual = datetime.now().year
        self.ano_nasc = int(ano_atual) - ano_nasc
        return self.ano_nascimento


usuario1 = Funcionarios('Elena', 'Cabral', 2013)

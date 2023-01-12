# def boas_vindas():
#     print('Olá, Marcos')
#     print('Temos 5 laptops em estoque.')


# boas_vindas()


# def somar_dois_numeros():
#     numero1 = 10
#     numero2 = 5
#     resultado = numero1 + numero2
#     print(resultado)


# somar_dois_numeros()


# def boas_vindas(nome, quantidade):
#     print(f'Olá, {nome}')
#     print(f'Temos {str(quantidade)} laptops em estoque.')


# boas_vindas('Marcos', 10)
# boas_vindas('Ronaldo', 4)
# boas_vindas('Linda', 2)


# def boas_voindas(quantidade, nome='Guilherme'):
#     print(f'Olá, {nome}')
#     print(f'Temos {str(quantidade)} laptops em estoque.')


# boas_vindas(6)


# def boas_voindas(quantidade=5, nome='Guilherme'):
#     print(f'Olá, {nome}')
#     print(f'Temos {str(quantidade)} laptops em estoque.')


# boas_vindas()


# ERRADO Se for determinar algum valor default, ele precisa ser o último parâmetro

# def boas_voindas(quantidade=5, nome=):
#     print(f'Olá, {nome}')
#     print(f'Temos {str(quantidade)} laptops em estoque.')

# boas_vindas()


# def cliente1(nome):
#     print(f'Olá, {nome}.')


# cliente1('Maria')


# def cliente2(nome):
#     return f'Olá, {nome}.'


# cliente2('Guilherme')


# def soma(*numeros):
#     resultado = 0
#     for num in numeros:
#         resultado += num
#     return resultado


# x = soma(2, 3, 4, 7)
# print(x)

def agencia(**carro):
    return carro


print(agencia(marca='Gol', cor='Branco', motor=1.0, placa=1234))
print(agencia(marca='Gol', cor='Azul', motor=1.0))
print(agencia(marca='Gol', cor='Vermelho'))

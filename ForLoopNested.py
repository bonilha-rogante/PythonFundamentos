for numero in range(1, 6):
    print('Produto: ' + str(numero))
    for numero2 in range(5):
        print(numero, numero2)


for horas in range(1, 6):
    for minutos in range(1, 61):
        for segundos in range(1, 61):
            print(f'{horas} horas, {minutos} minutos, {segundos} segundos')

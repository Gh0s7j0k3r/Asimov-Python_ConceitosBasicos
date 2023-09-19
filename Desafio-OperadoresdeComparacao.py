fome=str(input('Está com fome? '))
if fome == 'sim':
    print('Estou com fome!')
    comida = str(input('Tem comida em casa? '))
    if comida == 'não':
        print('Tenho que ir ao mercado.')
        print('Voltar para casa.')
    print('Preparar uma refeição.')
    print('Comer a comida.')
else:
    print('Estou sem fome.')
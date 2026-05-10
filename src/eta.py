import time
from os import system
chave = True
while chave:
    try:
        print('-'*100)
        print('Recomendamos que antes de executar esse programa execute o\nprograma que calcula a variação da energia interna e o que\ncalcula a velocidade e anote os valores recebidos.')
        print('-'*100)

        continua = input("Pressione Enter pra continuar...")

        system('cls')

        print('-'*100)
        print('Bem vido ao módulo de cálculo do rendimento!')
        print('-'*100)

        delta_u = float(input('Digite o valor da Variação da Energia Interna em Joules: '))
        m = float(input('Digite o valor da massa do foguete em Kg: '))
        v = float(input('Digite o valor da velocidade do foguete em m/s: '))

        e_cinetica = (m*(v**2))/2

        eta = e_cinetica/delta_u

        print(f'O valor aproximado do rendimento (eta) é: {eta:.2f}')

        time.sleep(3)
        system('cls')

        reiniciar = input('Deseja utilizar o módulo novamente? (S/N): ').strip().upper()
        if reiniciar[0] == 'S':
            chave = True
            system('cls')
        else:
            chave = False
            system('cls')

    except ValueError:
        print('Valor inválido, tente novamente.')
        print('Carregando...')
        time.sleep(1)
        chave = True
        system('cls')
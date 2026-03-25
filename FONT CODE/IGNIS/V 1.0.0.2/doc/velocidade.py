import time
from os import system

chave = True
while chave:
    try:
        print('-'*100)
        print('Bem vindo ao módulo de cálculo da valocidade do foguete!')
        print('-'*100)

        temp = float(input('Digite o tempo de vôo do foguete em segundos: '))
        alc = float(input('Digite o alcance (distância da base para o local de pouso) do foguete em metros: '))

        velocidade = alc/temp

        print('-'*100)
        print(f'A velocidade do foguete é de: {velocidade:.2f} m/s.')

        time.sleep(3)
        system('cls')


        reiniciar = input('Deseja utilizar o módulo novamente? (S/N):').strip().upper()
        if reiniciar[0] == 'S':
            chave = True
            system('cls')

        else:
            print('Carregando...')
            chave = False
            system('cls')

    except ValueError:
        print('Valor inválido, tente novamente.')
        print('Carregando...')
        time.sleep(1)
        chave = True
        system('cls') 
from os import system
import time

chave = True

while chave:
    try:
        #Introdução ao módulo
        print('Bem vindo ao módulo de cálculo do Trabalho!')
        print('-' * 100)

        #Entrada de dados
        v = float(input('Digite o volume inicial em m3: '))
        p1 = float(input('Digite a pressão inicial em PA (Pascal): '))
        p2 = 101325
        y = 1.4

        #Fórmula
        w = ((p1*v)/(y-1))*(1-(p2/p1)**((-y+1)/y))

        print('-' * 100)
        print(f'O trabalho realizado pelo gás é de {w:.2f} Joules')

        time.sleep(5)
        system('cls')

        #Pergunta de reinicialização
        reiniciar = input('Deseja utilizar o programa novamente ? (S/N): ').strip().upper()
        if reiniciar[0] == 'S':
            chave = True
            system('cls')
        else:
            print('Carregando...')
            time.sleep(2)
            chave = False
            system('cls')

    except ValueError:
        print('\nValor inválido, tente novamente.')
        print('\nCarregando...')
        time.sleep(1)
        chave = True
        system('cls')
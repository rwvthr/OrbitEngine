from os import system
import time
import math

chave = True

while chave:
    try:
        #Introdução ao múdulo
        print('Bem vindo ao módulo de cálculo velocidade em função da variação da energia interna da base!')
        print('-'*100)

        #Entrada de dados
        v = float(input('Digite o volume inicial em m3: '))
        p1 = float(input('Digite a pressão inicial em PA (Pascal): '))
        p2 = 101325
        n = float(input('Digite o rendimento em decimal. Ex.: 30% = 0.3 '))
        m = float(input('Digite a massa do foguete em kg: '))

        #Fórmula
        va_ve_ener_int = math.sqrt(((5*v*n)*(p1-p2)/m))

        print('-'*100)

        print(f'A a velocidade em função da energia interna do gás é {va_ve_ener_int:.2f} m/s ou {va_ve_ener_int*3.6:.2f} km/h')

        time.sleep(5)
        system('cls')

        #Pergunta de reinicialização
        reiniciar = input('Deseja utilizar o módulo novamente ? (S/N): ').strip().upper()
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
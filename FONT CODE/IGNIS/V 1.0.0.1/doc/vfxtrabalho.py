import math
from os import system
import time

chave = True

while chave:
    try:
        #Introdução ao módulo
        print('Bem-vindo ao módulo de cálculo do Trabalho!')
        print('-'*100)

        #Entrada de dados
        n = float(input('Digite o rendimento em decimal. Ex.: 30% = 0.3: '))
        w = float(input('Digite o trabalho em Joule: '))
        m = float(input('Digite a massa do foguete em kg: '))

        #Fórmula
        vfxw = math.sqrt((2*w*n)/m)

        print('-'*100)
        print(f'A velocidade final do foguete é de {vfxw:.2f} m/s.')
        
        time.sleep(5)
        system('cls')

        #Pergunta de reinicialização
        inicializar = input('Deseja utilizar o programa novamente ? (S/N): ').strip().upper()
        if inicializar[0] == 'S':
            chave = True
            system('cls')        
        else:
            print('Carregando...')
            time.sleep(2)
            chave = False
            system('cls')

    except ValueError:
        print('Valor inválido, tente novamente.')
        print('Carregando...')
        time.sleep(1)
        chave = True
        system('cls')




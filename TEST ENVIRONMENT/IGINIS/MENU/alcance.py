import math
from os import system
import time

chave = True
while chave:
    try:
        #Introdução ao módulo
        print('Bem-vindo ao módulo de cálculo do Alcance do Foguete!')
        print('-'*100)

        #Entrada de dados
        v = float(input('Digite o volume em m3: '))
        m = float(input('Digite a massa do foguete em kg: '))
        n = float(input('Digite o rendimento em decimal. Ex.: 30% = 0.3: '))
        tet = float(input('Digite o ângulo da base de lançamento em graus: '))
        g = 9.81
        p1 = float(input('Digite a pressão inicial em PA (Pascal): '))
        p2 = 101325
        x = math.radians(2*tet)
        sen_2tet = math.sin(x)

        #Fórmula
        alcance = (5*v*n*(p1-p2)*sen_2tet)/(m*g)

        print('-'*100)
        print(f'O alcance do foguete é de {alcance:.2f} metros.')

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

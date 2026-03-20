import math
from os import system
import time
import numpy as np
import matplotlib.pyplot as plt

chave = True
while chave:
    try:
        print('Bem vindo ao módulo de geração do gráfico do Alcance x Pressão Final!')
        print('-'*100)

        #Entrada de dados
        alcance = float(input('Digite o alcance do foguete em m: '))
        pressao_final = float(input('Digite a pressão final do foguete em Pa: '))
        pressao_inicial = float(input('Digite a pressão inicial do foguete em Pa: '))

        print('-'*100)

        time.sleep(1)
        system('cls')

        #Gerando o gráfico de Alcance x Pressão Final
        a = np.linspace(0, alcance, 50)
        b = np.linspace(pressao_final, pressao_inicial, 50)

        plt.plot(b, a, label='Alcance x Pressão Final', linewidth=2, color='magenta')
        plt.title('Alcance x Pressão Final')
        plt.legend()
        plt.xlabel('Alcance (m)')
        plt.ylabel('Pressão Final (Pa)')
        plt.grid(True, linestyle='-.')
        plt.tight_layout()
        plt.show()

        time.sleep(1)
        system('cls')

        p = input('Deseja reajustar os valores e o gráfico? (S/N): ').strip().upper()
        if p[0] == 'S':
            chave = True
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

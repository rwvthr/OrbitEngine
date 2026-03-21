import math
from os import system
import time
import numpy as np
import matplotlib.pyplot as plt

chave = True
while chave:
    try:
        print('-'*100)
        print('Bem vindo ao módulo de geração de gráfico do Alcance x Rendimento!')

        print('-'*100)

        n = float(input('Digite o valor do rendimento (η) em porcentagem: '))
        alcance = float(input('Digite o valor do alcance em metros: '))

        alc = np.linspace(0, alcance, 10)
        eta = np.linspace(0, n, 10) 

        plt.plot(alc, eta, label='Alcance x Rendimento', linewidth=2, color='green')
        plt.title('Gráfico do Alcance x Rendimento')
        plt.xlabel('Alcance (m)')
        plt.ylabel('Rendimento (η)')
        plt.grid(True, linestyle='-.')
        plt.tight_layout()
        plt.legend()
        plt.show()

        time.sleep(1)
        system('cls')

        incializar = input('Deseja gerar outro gráfico? (S/N): ').strip().upper()
        if incializar[0] == 'S':
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
import time
from os import system
import math
from exevoy import alcance, vfxenerit, tet
import numpy as np
import matplotlib.pyplot as plt

chave = True
while chave:
    try:
        #Cálculo v0y
        voy = vfxenerit * math.sin(tet)
        vox = vfxenerit * math.cos(tet)
        tempo = alcance/vfxenerit

        print(f'O valor do V0y é de aproximadamente {voy:.2f} m/s.')
        print(f'O tempo de voo do foguete é de aproximadamente {tempo:.2f} segundos.')

        time.sleep(5)
        system('cls')

        temp = np.linspace(0, tempo, 10)
        ve0y = voy - (9.81 * temp)

        plt.plot(temp, ve0y, label='Componente V0y', linewidth=2, color='brown')
        plt.title('Velocidade Vertical (V0y) vs Tempo')
        plt.legend()
        plt.xlabel('Tempo (s)')
        plt.ylabel('Velocidade Horizontal (m/s)')
        plt.grid(True, linestyle='-.')
        plt.tight_layout()
        plt.show()

        time.sleep(3)
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



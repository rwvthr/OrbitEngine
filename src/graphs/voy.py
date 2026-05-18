import math
from src.graphs.exevoy import alcance, vfxenerit, tet
import numpy as np
import matplotlib.pyplot as plt
from src.functions import loading, clear_screen

def ascii():
    asciiart = r"""     
      ___       _     _ _                        
     / _ \ _ __| |__ (_) |_ _   _               
    | | | | '__| '_ \| | __| | | |              
    | |_| | |  | |_) | | |_| |_| |              
     \___/|_|  |_.__/|_|\__|\__, |             
                            |___/   

        O R B I T Y - v1.0.0.1
         Author: rwvthrdev        
""" 
    return asciiart

def header():
    asciiart = ascii()
    print(f"\033[38;5;208m{asciiart}\033[0m")

chave = 1
counter = 0

while chave > counter:
    try:
        print(' ')
        header()

        voy = vfxenerit * math.sin(tet)
        tempo = alcance/vfxenerit

        print(f'''
              
\033[38;5;208mO valor da velocidade vertical V0y é >>> \033[94m{voy:.2f} \033[38;5;208mmetros por segundo e o tempo de vôo do foguete é 
de >>> \033[94m{tempo:.2f} \033[38;5;208msegundos.
\033[0m''')

        espera = input('\033[94mAperte ENTER para mostrar o gráfico >>> \033[0m')

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

        print(' ')

        p = input('\033[94mDeseja ver novamente o gráfico? [Y/N] >>> \033[0m').strip().upper()
        if p[0] == 'Y':
            counter = 0
            clear_screen()

        elif p[0] == 'N':
            loading()
            counter += 1
            clear_screen()

        else:
            print('')
            print('\033[38;2;255;20;147mValor inválido, tente novamente.\033[0m')
            print('')
            loading()
            counter = 0
            clear_screen()
            
    except ValueError:
        print('')
        print('\033[38;2;255;20;147mValor inválido, tente novamente.\033[0m')
        print('')
        loading()
        counter = 0
        clear_screen()
    
    except ZeroDivisionError:
        print('')
        print('\033[38;2;255;20;147mNão é possível dividir por zero, tente novamente.\033[0m')
        print('')
        loading()
        counter = 0
        clear_screen()



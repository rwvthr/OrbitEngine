import numpy as np
import matplotlib.pyplot as plt
from src.functions import loadingcalc, clear_screen, loading

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

    options1 = r"""
[!] - Bem-vindo ao módulo 9: Gráfico do Alcance x Rendimento.
"""

    print(f"\033[38;5;208m{asciiart}\033[0m")
    print(f"\033[94m{options1}\033[0m")

chave = 1
counter = 0


while chave > counter:
    try:
        print(' ')
        header()

        n = float(input('\033[38;5;208mDigite o rendimento em porcentagem (Obs: sem o "%") >>> \033[0m'))
        alcance = float(input('\033[38;5;208mDigite o valor do alcance em metros >>> \033[0m'))

        print(' ')
        loadingcalc()

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
        
        print(''' 
''')

        inicializar = input('\033[94mDeseja utilizar o programa novamente ? [Y/N] >>> \033[0m').strip().upper()
        print(' ')
        if inicializar[0] == 'Y':
            counter = 0
            clear_screen()
                    
        elif inicializar[0] == 'N':
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
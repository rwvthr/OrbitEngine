import math
from src.functions import loading, loadingcalc, clear_screen

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
[!] - Bem-vindo ao módulo 4: Calculo da velocidade em função de W.
"""

    print(f"\033[38;5;208m{asciiart}\033[0m")
    print(f"\033[94m{options1}\033[0m")

chave = 1
counter = 0

while chave > counter:
    try:
        header()
        print('')

        n = float(input('\033[38;5;208mDigite o rendimento em numero decimal (Ex: 0.10) >>> \033[0m'))
        w = float(input('\033[38;5;208mDigite o trabalho em joules (J) >>> \033[0m'))
        m = float(input('\033[38;5;208mDigite a massa do foguete em kilogramas (kg) >>> \033[0m'))

        vfxw = math.sqrt((2*w*n)/m)

        print(' ')
        loadingcalc()
        
        print(f'''
              
\033[38;5;208mO resultado obtido para Velocidade >>> {vfxw:.2f} metros por segundo.\033[0m''')

        print(' ')
        
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




import time
from os import system
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
[!] - Bem-vindo ao módulo 6: Calculo da Velocidade.
"""

    print(f"\033[38;5;208m{asciiart}\033[0m")
    print(f"\033[94m{options1}\033[0m")

chave = 1
counter = 0

while chave > counter:
    try:
        header()
        print('')

        temp = float(input('\033[38;5;208mDigite o tempo de vôo do foguete em segundos (s) >>> \033[0m'))
        alc = float(input('\033[38;5;208mDigite o alcance (distância do foguete até a base) em metros (m) >>> \033[0m'))

        velocidade = alc/temp

        print(' ')
        loadingcalc()
        
        print(f'''
              
\033[38;5;208mO resultado obtido para Velocidade do foguete >>> {velocidade:.2f} m/s.\033[0m''')

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

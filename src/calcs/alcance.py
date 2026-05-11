import math
from os import system
import time
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
         Author: M.R.L Silva        
""" 
    return asciiart

def header():
    asciiart = ascii()

    options1 = r"""
[!] - Bem-vindo ao módulo 2: Calculo do Alcance.
"""

    print(f"\033[38;5;208m{asciiart}\033[0m")
    print(f"\033[94m{options1}\033[0m")


chave = 1
counter = 0

while chave > counter:
    try:
        header()
        print('')

        v = float(input('\033[38;5;208mDigite o volume em metros cúbicos (m³) >>> \033[0m'))
        m = float(input('\033[38;5;208mDigite a massa do foguete em kilogramas (kg) >>> \033[0m'))
        n = float(input('\033[38;5;208mDigite o rendimento em numero decimal (Ex: 0.10) >>> \033[0m'))
        tet = float(input('\033[38;5;208mDigite o ângulo da base de lancamento em graus (Ex: 45) >>> \033[0m'))
        g = 9.81
        p1 = float(input('\033[38;5;208mDigite a pressão inicial em Pascal (PA) >>> \033[0m'))
        p2 = 101325
        x = math.radians(2*tet)
        sen_2tet = math.sin(x)

        alcance = (5*v*n*(p2-p1)*sen_2tet)/(m*g)

        print(' ')
        loadingcalc()
        
        print(f'''
              
\033[38;5;208mO resultado obtido para o alcance é >>> {alcance:.2f} metros.\033[0m''')

        print(' ')

        #Pergunta de reinicialização
        inicializar = input('\033[94mDeseja utilizar o programa novamente ? [Y/N] >>> \033[0m').strip().upper()
        print(' ')
        if inicializar[0] == 'Y':
            counter = 0
            clear_screen()
                    
        elif inicializar[0] == 'N':
            loading()
            counter += 1
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

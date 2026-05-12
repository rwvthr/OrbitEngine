import time
from os import system
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
[!] - Bem-vindo ao módulo 7: Calculo do Rendimento.
"""

    print(f"\033[38;5;208m{asciiart}\033[0m")
    print(f"\033[94m{options1}\033[0m")

chave = 1
counter = 0

while chave > counter:
    try:
        header()
        print('')

        def aviso():
            print('\033[38;2;255;20;147mRecomendamos que, antes de executar este programa, você execute\nprimeiro os programas que calculam a variação da energia interna\ne a velocidade, anotando os valores obtidos.\033[0m')
            print('')

            continua = input("\033[38;5;208mPress Enter to continue >>> \033[0m")
            clear_screen()

            return continua
            
        aviso()

        header()
        print('')

        delta_u = float(input('\033[38;5;208mDigite o valor da Variação da Energia Interna em Joules (J) >>> \033[0m'))
        m = float(input('\033[38;5;208mDigite a massa do foguete em kilogramas (kg) >>> \033[0m'))
        v = float(input('\033[38;5;208mDigite a velocidade do foguete em metros por segundo (m/s) >>> \033[0m'))

        e_cinetica = (m*(v**2))/2

        eta = e_cinetica/delta_u

        print('')
        loadingcalc()

        print(f'''
              
\033[38;5;208mO resultado obtido para o rendimento é >>> {eta:.2f}.\033[0m''')
        
        print('')

        inicializar = input('\033[94mDeseja utilizar o programa novamente ? [Y/N] >>> \033[0m').strip().upper()
        print(' ')
        if inicializar[0] == 'Y':
            clear_screen()
            counter = 0
            
                    
        elif inicializar[0] == 'N':
            loading()
            clear_screen()
            counter += 1

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

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
[!] - Bem-vindo ao módulo 3: Calculo da Variação da Energia Interna.
"""

    print(f"\033[38;5;208m{asciiart}\033[0m")
    print(f"\033[94m{options1}\033[0m")

chave = 1
counter = 0

while chave > counter:
    try:
        header()
        print('')
        
        v = float(input('\033[38;5;208mDigite o volume inicial em metros cúbicos (m³) >>> \033[0m'))                                  
        p1 = float(input('\033[38;5;208mDigite a pressão inicial em Pascal (PA) >>> \033[0m'))
        p2 = 101325

        
        va_ener_int = (5/2)*v*(p1-p2)          

        print(' ')
        loadingcalc()
        
        print(f'''
              
\033[38;5;208mO resultado obtido para a Variação da Energia Interna é >>> {va_ener_int:.2f} Joules.\033[0m''')

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


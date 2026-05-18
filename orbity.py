import time
from os import system
import importlib
import sys

#Função Limpar Tela
def clear_screen():
    from os import system
    import platform
    if platform.system() == 'Windows':
        system('cls')
    else:
        system('clear')

#Animação de carregamento
def loadinganm():
    AZUL = '\033[94m'                      
    ROSA_VIBRANTE = '\033[38;2;255;20;147m' 
    NEGRITO = '\033[1m'                    
    RESET = '\033[0m'                      

    animation = ["\\", "|", "/", "-"]
    msg = "Loading code..."

    for _ in range(3):
        for i in range(len(animation)):
            time.sleep(0.2)
            
            sys.stdout.write(f"\r{AZUL}{msg}{RESET} {NEGRITO}{ROSA_VIBRANTE}{animation[i % len(animation)]}{RESET}")
            sys.stdout.flush()

#Animação de Saída
def loadinganmexit():
    AZUL = '\033[94m'                      
    ROSA_VIBRANTE = '\033[38;2;255;20;147m' 
    NEGRITO = '\033[1m'                    
    RESET = '\033[0m'                      

    animation = ["\\", "|", "/", "-"]
    msg = "Exiting..."

    for _ in range(3):
        for i in range(len(animation)):
            time.sleep(0.2)
            
            sys.stdout.write(f"\r{AZUL}{msg}{RESET} {NEGRITO}{ROSA_VIBRANTE}{animation[i % len(animation)]}{RESET}")
            sys.stdout.flush()

#Ascii art do Orbity
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

#Função para mostrar o cabeçalho do menu
def header():
    asciiart = ascii()

    options1 = r"""
[01] - More about the project
[02] - View Important Notices
[03] - Intrusions Manual
[04] - Start the program
[00] - Exit
"""

    print(f"\033[38;5;208m{asciiart}\033[0m")
    print(f"\033[38;2;64;224;208m{options1}\033[0m")

#Função da mensagem de voltar
def mensagemvoltar():
    print('\033[38;2;64;224;208mPress the Y key to return to the menu.\033[0m')
    print('\033[38;2;64;224;208mPressione a tecla Y para retornar ao menu.\033[0m')

    back = input('\033[38;5;208m>>>\033[0m').strip().lower()

    print(' ')
    return back

#Mensagem leave
def mensagemend():
    print('\033[38;2;64;224;208mYou chose to leave the program! Thanks for using. :)\033[0m')

    print(' ')

    loadinganmexit()

#Contador para o While (decidi usar essa lógica muito doida)
keyback = [0]
key = 1
index = 0


while key > keyback[index]:
    clear_screen()

    header()

    try:
        pergunta = int(input('\033[38;2;64;224;208mPlease select an option: \033[0m').strip())
        print(' ')

        loadinganm()
        clear_screen()

        if pergunta == 1:
            with open('docs/aboutproject.txt', 'r', encoding='utf-8') as arquivo:
                conteudo = arquivo.read()
                print(conteudo)
            
            mensagemvoltar()
            loadinganm()
            clear_screen()


        elif pergunta == 2:
            with open('docs/notices.txt', 'r', encoding='utf-8') as arquivo:
                conteudo = arquivo.read()
                print(conteudo)

            mensagemvoltar()
            loadinganm()
            clear_screen()

        elif pergunta == 3:
            with open('docs/manual.txt', 'r', encoding='utf-8') as arquivo:
                conteudo = arquivo.read()
                print(conteudo)

            mensagemvoltar()
            loadinganm()
            clear_screen()

        elif pergunta == 4:
            if 'src.menu' in sys.modules:
                importlib.reload(menu)
            else:
                from src import menu


        elif pergunta == 0:
            mensagemend()
            clear_screen()
            keyback.append(key)
            index += 1

        else:
            print('Invalid value, please try again.')
            loadinganm()
            clear_screen()
            continue

    except ValueError:
        print('Invalid value, please try again.')
        print('Loading...')
        time.sleep(1)
        key = 1
        clear_screen()

    
#End
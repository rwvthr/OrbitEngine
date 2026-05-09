import time
from os import system
import importlib
import sys

#Função limpa terminal
def clear_screen():
    from os import system
    import platform
    if platform.system() == 'Windows':
        system('cls')
    else:
        system('clear')

#Função animação de carregamento 
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

#Função da art em ascii
def ascii():
    asciiart = r"""     
   _        ___       _     _ _                        
  / \      / _ \ _ __| |__ (_) |_ _   _               
  | |     | | | | '__| '_ \| | __| | | |              
 /|_|\    | |_| | |  | |_) | | |_| |_| |              
///|\\\    \___/|_|  |_.__/|_|\__|\__, |             
                                  |___/   

         O R B I T Y - v1.0.0.1
          Author: M.R.L Silva        
""" 
    return asciiart

#função do menu
def initmenu():
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

#Call
initmenu()

#Pergunta
pergunta = input('\033[38;2;64;224;208mPlease select an option: \033[0m').strip()
print(' ')

#Call
loadinganm()
clear_screen()

if pergunta == 1:
    with open('aboutproject.txt', 'r', encoding='utf-8') as arquivo:
        conteudo = arquivo.read()
        print(conteudo)

elif pergunta == 2:
    with open('notices.txt', 'r', encoding='utf-8') as arquivo:
        conteudo = arquivo.read()
        print(conteudo)

elif pergunta == 3:
    with open('manual.txt', 'r', encoding='utf-8') as arquivo:
        conteudo = arquivo.read()
        print(conteudo)












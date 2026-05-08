import time
from os import system
import importlib
import sys

def clear_screen():
    from os import system
    import platform
    if platform.system() == 'Windows':
        system('cls')
    else:
        system('clear')

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

def ascii():
    asciiart = r"""     
   _        ___       _     _ _                        
  / \      / _ \ _ __| |__ (_) |_ _   _               
  | |     | | | | '__| '_ \| | __| | | |              
 /|_|\    | |_| | |  | |_) | | |_| |_| |              
///|\\\    \___/|_|  |_.__/|_|\__|\__, |             
                                  |___/   

         O R B I T Y - v1.0.1        
""" 
    return asciiart

def initmenu():
    asciiart= ascii()

    header = r"""
Author: M.R.L Silva;
Project: Orbity - A rockertics simulation software for educational purposes;
Institution: Instituto Federal de Educação, Ciência e Tecnologia de Alagoas - IFAL-PIN;
Advisor: Prof. Dr. Karciano José Silva Santos;
"""

    options1 = r"""
[01] - More about the project
[02] - View Important Notices
[03] - Intrusions Manual
[04] - Start the program
[00] - Exit
"""

    print(f"\033[38;5;208m{asciiart}\033[0m")
    print(f"\033[38;2;64;224;208m{header}\033[0m")
    print(f"\033[38;2;64;224;208m{options1}\033[0m")

    pergunta = input('\033[38;2;64;224;208mPlease select an option: \033[0m').strip()

    print(" ")

initmenu()

loadinganm()
clear_screen()

if 




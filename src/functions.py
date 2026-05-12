import sys
import time


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

def mensagemvoltar():
    print('\033[38;2;64;224;208mPress the Y key to return to the menu.\033[0m')
    print('\033[38;2;64;224;208mPressione a tecla Y para retornar ao menu.\033[0m')

    back = input('\033[38;5;208m>>>\033[0m').strip().lower()

    print(' ')
    return back

def mensagemend():
    print('\033[38;2;64;224;208mYou chose to leave the program! Thanks for using. :)\033[0m')

    print(' ')

    loadinganmexit()

def loadingcalc():
    AZUL = '\033[94m'                      
    ROSA_VIBRANTE = '\033[38;2;255;20;147m' 
    NEGRITO = '\033[1m'                    
    RESET = '\033[0m'                      

    animation = ["\\", "|", "/", "-"]
    msg = "Calculating... "

    for _ in range(3):
        for i in range(len(animation)):
            time.sleep(0.2)
            
            sys.stdout.write(f"\r{AZUL}{msg}{RESET} {NEGRITO}{ROSA_VIBRANTE}{animation[i % len(animation)]}{RESET}")
            sys.stdout.flush()

def loading():
    AZUL = '\033[94m'                      
    ROSA_VIBRANTE = '\033[38;2;255;20;147m' 
    NEGRITO = '\033[1m'                    
    RESET = '\033[0m'                      

    animation = ["\\", "|", "/", "-"]
    msg = "Loading ... "

    for _ in range(3):
        for i in range(len(animation)):
            time.sleep(0.2)
            
            sys.stdout.write(f"\r{AZUL}{msg}{RESET} {NEGRITO}{ROSA_VIBRANTE}{animation[i % len(animation)]}{RESET}")
            sys.stdout.flush()

def asciiart():
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
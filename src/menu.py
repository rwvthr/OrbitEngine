import time
from os import system
import importlib
import sys
from functions import clear_screen

def asciimenu():
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

def headermenu():
    asciiart = asciimenu()

    options1 = r"""

[+] Calculation

[01] - Calcular o trabalho realizado pelo gás dentro da base.
[02] - Calcular alcance do foguete.
[03] - Calcular a variação da energia interna do gás.
[04] - Calcular a velocidade do foguete em função de W.
[05] - Calcular a velocidade do foguete em função de ΔU.
[06] - Calcular a valocidade (para facilitar o cálculo do rendimento).
[07] - Calcular rendimento η.

[+] Graphics

[08] - Gerar gráfico do Alcance x Pressão Final.
[09] - Gerar gráfico do Alcance x Rendimento.
[10] - Gerar gráfico de V0x x Tempo.
[11] - Gerar gráfico de V0y x Tempo.
[00] - Encerrar programa.

"""

    print(f"\033[38;5;208m{asciiart}\033[0m")
    print(f"\033[38;2;64;224;208m{options1}\033[0m")



chaveanterior = [0]
chave = 1
index = 0

while chave > chaveanterior[index]:
    headermenu()

    try:
        pergunta = int(input('\033[38;2;64;224;208mPlease select an option: \033[0m').strip())
        print(' ')
        clear_screen()

        if pergunta == 1:
            if 'trabalho' in sys.modules:
                importlib.reload(trabalho)
            else:
                import src.trabalho as trabalho

        elif pergunta == 2:
            if 'alcance' in sys.modules:
                importlib.reload(alcance)
            else:
                import src.alcance as alcance
        
        elif pergunta == 3:
            if 'vaenergiainterna' in sys.modules:
                importlib.reload(vaenergiainterna)
            else:
                import src.vaenergiainterna as vaenergiainterna
        
        elif pergunta == 4:
            if 'vfxtrabalho' in sys.modules:
                importlib.reload(vfxtrabalho)
            else:
                from calcs import vfxtrabalho

        elif pergunta == 5:
            if 'vfxdedeltau' in sys.modules:
                importlib.reload(vfxdedeltau)
            else:
                from calcs import vfxdedeltau

        elif pergunta == 6:
            if 'velocidade' in sys.modules:
                importlib.reload(velocidade)
            else:
                import src.velocidade as velocidade

        elif pergunta == 7:
            if 'eta' in sys.modules:
                importlib.reload(eta)
            else:
                import src.eta as eta

        elif pergunta == 8:
            if 'alcancexpress' in sys.modules:
                importlib.reload(alcancexpress)
            else:
                import src.alcancexpress as alcancexpress
        
        elif pergunta == 9:
            if 'alcancexeta' in sys.modules:
                importlib.reload(alcancexeta)
            else:
                import src.alcancexeta as alcancexeta
        
        elif pergunta == 10:
            if 'vox' in sys.modules:
                importlib.reload(vox)
            else:
                import src.graphs.vox as vox
        
        elif pergunta == 11:
            if 'voy' in sys.modules:
                importlib.reload(voy)
            else:
                import src.graphs.voy as voy
    
        elif pergunta == 0:
            print('Encerrando programa...')
            time.sleep(1.5)
            chave = False
            system('cls')
        else:
            print('Número inválido, tente novamente.')
            print('Carregando...')
            time.sleep(1)
            system('cls')
            continue

        inicializar = input('Deseja retornar ao menu principal? (S/N) :').upper().strip()

        if inicializar[0] == 'S':
            chaveanterior.append(chave)
            chave += 1
            index += 1
            print('Retornando ao menu principal...')
            time.sleep(1.5)
            system('cls')
        
        elif inicializar[0] == 'N':
            print('Encerrando programa...')
            time.sleep(1.5)
            system('cls')
            break

    except ValueError:
        print('Valor inválido, tente novamente.')
        print('Carregando...')
        time.sleep(1)
        chave = True
        system('cls')



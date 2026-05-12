import time
from os import system
import importlib
import sys
from .functions import clear_screen, mensagemend, mensagemvoltar, loadinganm, loadinganmexit, loading

def asciimenu():
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
    asciiart = asciimenu()
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
            if 'src.calcs.trabalho' in sys.modules:
                importlib.reload(trabalho)
            else:
                from .calcs import trabalho

        elif pergunta == 2:
            if 'src.calcs.alcance' in sys.modules:
                importlib.reload(alcance)
            else:
                from .calcs import alcance
        
        elif pergunta == 3:
            if 'src.calcs.vaenergiainterna' in sys.modules:
                importlib.reload(vaenergiainterna)
            else:
                from .calcs import vaenergiainterna
        
        elif pergunta == 4:
            if 'src.calcs.vfxtrabalho' in sys.modules:
                importlib.reload(vfxtrabalho)
            else:
                from .calcs import vfxtrabalho

        elif pergunta == 5:
            if 'src.calcs.vfxdedeltau' in sys.modules:
                importlib.reload(vfxdedeltau)
            else:
                from .calcs import vfxdedeltau

        elif pergunta == 6:
            if 'src.calcs.velocidade' in sys.modules:
                importlib.reload(velocidade)
            else:
                from .calcs import velocidade

        elif pergunta == 7:
            if 'src.calcs.eta' in sys.modules:
                importlib.reload(eta)
            else:
                from .calcs import eta

        elif pergunta == 8:
            if 'src.graphs.alcancexpress' in sys.modules:
                importlib.reload(alcancexpress)
            else:
                from .graphs import alcancexpress
        
        elif pergunta == 9:
            if 'src.graphs.alcancexeta' in sys.modules:
                importlib.reload(alcancexeta)
            else:
                from .graphs import alcancexeta
        
        elif pergunta == 10:
            if 'src.graphs.vox' in sys.modules:
                importlib.reload(vox)
            else:
                from .graphs import vox
        
        elif pergunta == 11:
            if 'src.graphs.voy' in sys.modules:
                importlib.reload(voy)
            else:
                from .graphs import voy
    
        elif pergunta == 0:
            loadinganmexit()
            print('')
            clear_screen()
            break

        else:
            print('Número inválido, tente novamente.')
            print('Carregando...')
            time.sleep(1)
            system('cls')
            continue


        #Falta arrumar aqui---
        inicializar = input('\033[38;5;208mDeseja retornar ao menu principal? [Y/N] >>> \033[0m').upper().strip()

        if inicializar[0] == 'Y':
            chaveanterior.append(chave)
            chave += 1
            index += 1
            print('')
            loading()
            clear_screen()
        
        elif inicializar[0] == 'N':
            print('')
            mensagemend()
            clear_screen()
            break

    except ValueError:
        print('')
        print('\033[38;2;255;20;147mValor inválido, tente novamente.\033[0m')
        print('')
        loading()
        chaveanterior.append(chave)
        chave += 1
        index += 1
        clear_screen()



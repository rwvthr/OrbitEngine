from os import system
import time

chave = True

while chave:
    try:
        #Inicialização do módulo
        print('Bem vindo ao módulo de cálculo da variação da energia interna da base!')
        print('-'*100)

        #Entrada de dados
        v = float(input('Digite o volume inicial em m3: '))                                  
        p1 = float(input('Digite a pressão inicial em PA (Pascal): '))
        p2 = 101325

        #Cálculo da Energia Interna
        va_ener_int = (5/2)*v*(p1-p2)          

        #Retorno de dados
        print('-'*100)
        print(f'A variação energia interna do gás é {va_ener_int:.2f} Joules')

        #Limpeza de Terminal
        time.sleep(5)
        system('cls')

        #Pergunta de reinicialização
        reiniciar = input('Deseja utilizar o módulo novamente ? (S/N): ').strip().upper()
        if reiniciar[0] == 'S':
            chave = True
            system('cls')
        else:
            print('Carregando...')
            chave = False
            system('cls')

    except ValueError:
        print('\nValor inválido, tente novamente.')
        print('\nCarregando...')
        time.sleep(1)
        chave = True
        system('cls')


import time
from os import system

chaveanterior = [0]
chave = 1

index = 0

while chave > chaveanterior[index]:
    print('''
Confira o catálogo e os números correspondente ao serviço desejado:

    * Cálculo:
        
    1 - Calcular o Trabalho realizado pelo gás no lançamento do foguete.
    2 - Calcular o Alcance do Foguete.
    3 - Calcular a Variação da Energia Interna do Gás.
    4 - Calcular a Velocidade do Foguete em função do Trabalho (W).
    5 - Calcular a Velocidade do Foguete em função da Variação da Energia Interna (ΔU).
        
    * Geração de Gráficos:
        
    6 - Gerar o gráfico do Alcance em função da Pressão Final (P2).
    7 - Gerar o gráfico do Alcance em função do Rendimento (η).
    8 - Gerar o gráfico de V0x (velocidade horizontal) vs Tempo.
    9 - Gerar o gráfico de V0y (velocidade vertical) vs Tempo.   
    0 - Sair do programa.
    
Obs: Se digitardes algo que não corresponda aos números acima, o programa será encerrado.
''')

    pergunta = int(input('Digite o número correspondente ao serviço desejado: '))
    print('Processando...')
    time.sleep(1.5)
    system('cls')


    inicializar = input('Deseja retornar ao menu principal? (S/N) :').upper().strip()
    if inicializar[0] == 'S':
        chaveanterior.append(chave)
        chave += 1
        index += 1
        system('cls')
        print('Retornando ao menu principal...')
        time.sleep(1.5)
        system('cls')
        print('Menu Principal - IGNIS')
        print('-' * 100)

        print(chaveanterior)
        print(chave)
        print(index)
        
    elif inicializar[0] == 'N':
        print('Encerrando programa...')
        time.sleep(1.5)
        chaveanterior.append(chave)
        chave -= 1
        system('cls')

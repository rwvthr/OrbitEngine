import time
import os
from os import system

#APRESENTAÇÃO
print('-' * 100)
print('''Olá, seja bem-vindo ao menu do IGNIS! 
Iniciando...''')
print('-' * 100)

time.sleep(3)
system('cls')

print('-' * 100)
print('IGNIS - v1.0.0.1')
print('''Desenvolvido por: Silva, M.R.L & Lima, J.G.S - 2025 (c) All rights reserved;
Orientador: Prof. Dr. Karciano José Silva Santos;
      
-----------------------------------------------------------------------------------------------------
Título do projeto: Modelagem Matemática e Simulação Computacional
do Lançamento de Foguetes Educacionais com Resistência do Ar: Uma 
ferramenta para o ensino de Física e Tecnologias Aplicadas;
      
-----------------------------------------------------------------------------------------------------
Instituição: Instituto Federal de Educação, Ciência e Tecnologia de Alagoas
- IFAL Campus Palmeira dos Índios;

Projeto do Tipo: PIBITI - ES, promovido pela PRPPI - 
Pró-Reitoria de Pesquisa, Pós-Graduação e Inovação do IFAL;
Ano de desenvolvimento: 2025-2026;

-----------------------------------------------------------------------------------------------------
Uso livre para fins educacionais com a devida citação dos autores e do projeto.
      ''')

time.sleep(2)
system('cls')

#FIM DA APRESENTAÇÃO

#AVISO
per = input('Deseja ler alguns avisos importantes antes de prosseguir? (S/N) :').upper().strip()

if per[0] == 'S':
    print('-' * 100)

    print('''Avisos importantes:     
1- Os cálculos e gráficos são baseados em fórmulas da Termodinâmica e Física Clássica, não levando em consideração fatores como resistência do ar, variações de temperatura, umidade, entre outros;      
2- O programa IGNIS é destinado para o lançamento de foguetes acadêmicos, não recomendamos para outros fins;       
3- O código fonte está em constante atualização, novas funções e melhorias serão adicionadas futuramente, acesse o repositório oficial para acompanhar as novidades: https://github.com/rwvthr/OrbitEngine;       
4- O programa apresenta pequenas margens de erro, recomendamos sempre revisar os cálculos e os valores;              
5- Em caso sugestões ou problemas, por favor, entre em contato com os desenvolvedores através do e-mail: mrls9@aluno.ifal.edu.br ou jgsl6@aluno.ifal.edu.br''')
    print('-' * 100)
    time.sleep(8)
    system('cls')
    

elif per[0] == 'n':
    system('cls')
    print('Ignorando avisos, prosseguindo para o menu principal...')

#FIM DOS AVISOS

#EXPLICANDO O FUNCIONAMENTO
system('cls')

print('''-----------------------------------------------------------------------------------------------------
Antes de acessar o menu principal, vamos explicar como o programa funciona: 
-----------------------------------------------------------------------------------------------------
O programa IGNIS é dividido em duas partes principais: Cálculos e Geração de Gráficos.
Siga os passos recomendados para utilizar o programa de forma eficiente:
-----------------------------------------------------------------------------------------------------
1- Leia os avisos importantes para entender as limitações e recomendações do programa;   
2- Acesse o menu principal para escolher o serviço desejado, seja um cálculo específico ou a geração de um gráfico; 
3- Insira o número correspondente ao serviço desejado, e siga as instruções para fornecer os dados necessários para o cálculo ou gráfico;
4- Revise os resultados obtidos, e se necessário, faça ajustes nos dados de entrada para obter resultados mais precisos;    
5- Ao final, receberá uma mensagem perguntando se deseja retornar ao menu principal ou encerrar o programa, escolha a opção desejada para continuar ou finalizar sua experiência com o IGNIS.    
6- Agradeçemos por utilizar o IGNIS, esperamos que seja uma ferramenta útil para seus estudos e projetos relacionados ao lançamento de foguetes educacionais!
-----------------------------------------------------------------------------------------------------
            ''')

print('Aperte a telca Enter para acessar o menu principal...')
enter = input()
if enter == '':
    system('cls')
    print('Acessando o menu principal...')
    time.sleep(1.5)
#MENU PRINCIPAL

system('cls')
print('Menu Principal - IGNIS')
print('-' * 100)
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

chave = True
while chave:
    try:
        if pergunta == 1:
            import trabalho

        elif pergunta == 2:
            import alcance
        
        elif pergunta == 3:
            import vaenergiainterna
        
        elif pergunta == 4:
            import vfxtrabalho

        elif pergunta == 5:
            import vfxdedeltau

        elif pergunta == 6:
            import alcancexpress
        
        elif pergunta == 7:
            import alcancexeta
        
        elif pergunta == 8:
            import vox
        
        elif pergunta == 9:
            import voy
    
        elif pergunta == 0:
            print('Encerrando programa...')
            time.sleep(1.5)
            chave = False
            system('cls')

    except ValueError:
        print('Valor inválido, tente novamente.')
        print('Carregando...')
        time.sleep(1)
        chave = True
        system('cls')



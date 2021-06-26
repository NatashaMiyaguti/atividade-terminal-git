# Projeto 03 - Jogo de Dados:
# Utilizando os conceitos aprendidos até dicionários, crie um programa onde 4
# jogadores joguem um dado e tenham resultados aleatórios. O programa tem que:
# • Perguntar quantas rodadas você quer fazer; • Guardar os resultados dos
# dados em um dicionário.
# • Ordenar este dicionário, sabendo que o vencedor tirou o maior número no
# dado.
# • Mostrar no final qual jogador ganhou mais rodadas e foi o grande campeão.

from random import randint
from time import sleep
from rich import print #importa as cores e emotion, somente pode ser usados nos prints#
from operator import itemgetter # para ordenar o dicionario#
from collections import defaultdict # agrupa dados do dicionario#
from names import get_first_name 
from tqdm import tqdm # importa a barra de carregamento#

def linha():
    print(f'\n'+'-'*50+'\n')

    
jogadores = dict() 
jogadores_vitoria = dict()

while True:

    jogo = str(input('\nVamos jogar Dados? [S/N]: ')).strip().upper()[0]
    if jogo == 'N':
        print ('[blue]Até a próxima![blue]')
        break
    if jogo != 'S' and jogo != 'N':
        print ('[yellow]Resposta inválida[yellow]:confounded_face:')
        break
    jogadores.clear()    
    rodadas = int(input('\nDigite quantas rodadas iremos jogar: '))
    quantidade_jogadores = int(input('\nDigite a quantidade de jogadores: '))
    for j in range (quantidade_jogadores):
        # nome_jogadores = str(input('Digite o nome do jogador: ')).title().strip()
        nome_jogadores = get_first_name()  #caso nao queira escrever os nomes#
        
        jogadores[nome_jogadores] = 0
        jogadores_vitoria[nome_jogadores] = 0
    
    for n in range(rodadas):
        print('\n[blue]Vamos começar a rodada![blue]\n')
        print('[magenta]:game_die: Rolando os dados...[magenta]\n')
        sleep(1)
        for k, v in jogadores.items():
            jogadores[k] = randint(1,6)
        sleep(1)
        
        jogadas_agrupadas = defaultdict(list)
        for key, val in jogadores.items():
            jogadas_agrupadas[val].append(key)

        posicao = 0            
        for key, val in sorted(dict(jogadas_agrupadas).items(),reverse = True):
            posicao +=1
            print(f'Em {posicao}° lugar, com o dado {key}')
            for jogador in val:
                if posicao == 1:
                    jogadores_vitoria[jogador] +=1
                print(f'[blue] Jogador {jogador}[blue]')
            sleep(1)
    sleep(1)
    print(f'\n[magenta]Computando as vitórias...[magenta]\n')
    sleep(1)
    for i in tqdm(range (150)):
        sleep(0.0001)
    linha()
    ranking_final = sorted(jogadores_vitoria.items(), key = itemgetter(1), reverse = True)
    for key, val in ranking_final:
        posicao +=1
        print(f'[yellow]Jogador {key} teve {val} vitórias[yellow]')

    vitorias_agrupadas = defaultdict(list)
    for key, val in ranking_final:
        vitorias_agrupadas[val].append(key)
    sleep(2)
    vitoria_dict = sorted(dict(vitorias_agrupadas).items(),reverse = True)[0]
    campeoes = vitoria_dict[1]
    linha()
    if len(campeoes) > 1:
        print(f'[green]Os grandes campeões são:[green]')
        for i in campeoes:
            print(f':trophy: [green]{i}[green]'.center(50))
    else:
        print(f':trophy: [green]O grande campeão é:\n {campeoes[0].center(50)}[green]')



           

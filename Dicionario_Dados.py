'''
Crie um programa onde 4 jogadores joguem um dado e tenham
resultados aleatorios. Guarde esses resultados em um dicionario. 
No final, coloque esse dicionario em ordem, sabendo queo vencedor 
tirou o maior número no dado.
'''
from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1' : randint(1, 6),
        'jogador2' : randint(1, 6),
        'jogador3' : randint(1, 6),
        'jogador4' : randint(1, 6)}
ramking = list()
print('valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True )
print(ranking)
print('-=' * 30)
for i, v in enumerate(ranking):
    print(f'{i} lugar: {v[0]} com {v[1]}.')
    sleep(1)

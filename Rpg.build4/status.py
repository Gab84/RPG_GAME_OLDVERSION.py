from Player import *


Atributos = {
    'Forca' : 1,
    'Constituicao' : 1,
    'Mente': 1,
}


def distribuir_pt():
    for x in range(2):
        print('Você tem 2 pontos de atributos para distribuir')
        v = int(input('1 > Força | 2 > Constituição | ') )
        if v == 1:
            print(f"{player['nome']} Upou 1 ponto em força .")
            player['dano'][0] += Atributos['Forca']
            player['dano'][1] += Atributos['Forca']
            print(player['dano'])
        if v == 2:
            print(f"{player['nome']} Upou 1 ponto em Constituição .")
            player['vida_max'] += Atributos['Constituicao']
            print(player['vida_max'])


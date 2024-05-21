from Inimigo import *
from Player import *
from time import *

def chances():
  global chance
  chance = randint(0,6)
  return chance


def basico(player,inimigo):
    chances()
    print(f'essa foi a chance de golpe ======== {chance} ==============')
    if chance <= 3:
        sleep(1)
        print(f"{player} Usou ataque basico !\n ")
        sleep(1)
        print('Avançando no adversario')
        sleep(1)
        print('\nVocê acertou ! ')
        inimigo['vida'] -= player['dano'][0]
        sleep(1)
        print('====== Relatorio Combate =====')
        print(f"\nvocê causou {player['dano'][0]} de dano no inimigo e agora ele está com {inimigo['vida']} de pontos de vida\n")
        sleep(2)
        print('===============================')

    if chance >= 4:
        sleep(1)
        print(f"{player['nome']} Usou ataque basico !\n ")
        sleep(1)
        print('Avançando no adversario')
        sleep(1)
        print('\nVocê errou ! ')
        sleep(1)
        print('====== Relatorio Combate =====')
        sleep(1)
        print('Você não causou dano!')
        sleep(2)
        print('===============================')



#if atq == 2:
    
    def forte(player,inimigo):
        chances()
        print(f'essa foi a chance de golpe ======== {chance} ==============')
        if chance == 2:
            print(f"{player['nome']} Usou ataque forte ! ")
            inimigo['vida'][2] -= player['dano'][1]
            sleep(1)
            print('Avançando no adversario')
            sleep(1)
            print('\nVocê acertou ! ')
            sleep(1)
            print('====== Relatorio Combate =====')
            sleep(1)
            print(f"você causou {player['dano'][1]} de dano no inimigo e agora ele está com {inimigo['vida'][2]} de pontos de vida")
            sleep(2)
            print('===============================')

        if chance != 2:
            print(f"{player['nome']} Usou ataque forte ! ")
            sleep(1)
            print('Avançando no adversario')
            sleep(1)
            print('Você errou ! ')
            sleep(1)
            print('====== Relatorio Combate =====')
            sleep(1)
            print('Você não causou dano!')
            sleep(2)
            print('===============================')


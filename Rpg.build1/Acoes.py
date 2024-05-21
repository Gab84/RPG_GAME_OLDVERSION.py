from Inimigo import *
from Player import player
from time import sleep
from Textos import *

def chances():
  global chance
  chance = 2
  return chance



def upar_p(i_xp,i_vida):
    player['exp'] += i_xp
    if player['exp'] >= player['exp_max']:
        player['level'] += 1
        player['exp'] = 0
        player['exp_max'] +=20
        player['vida_max'] += 10
        player['vida'] += 2
        player['dano'][0] += 5
        player['dano'][1] += 5
        player['mana_max'] += 30
        player['cura'] += 2
        print(player)

def up():
    upar_p()

def luta(player,inimigo,i_vida,p_vida,p_dano,i_dano,p_dano2,i_dano2,p_cura,i_xp):
    if p_vida > 0:
        while p_vida >0:
                atq = int(input('Deseja usar qual golpe? '))
                if atq == 1:
                    chances()
                    print(f'essa foi a chance de golpe ======== {chance} ==============')
                    if chance <= 3:
                        sleep(1)
                        print(f"{player} Usou ataque basico !\n ")
                        sleep(1)
                        print('Avançando no adversario')
                        sleep(1)
                        print('\nVocê acertou ! ')
                        i_vida -= p_dano
                        sleep(1)
                        print('====== Relatorio Combate =====')
                        print(f"\nvocê causou {p_dano} de dano no inimigo {inimigo} e agora ele está com {i_vida} de pontos de vida\n")
                        sleep(2)
                        print('===============================')
                    if chance >= 4:
                        sleep(1)
                        print(f"{player} Usou ataque basico !\n ")
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
                elif atq == 2:
                    chances()
                    print(f'essa foi a chance de golpe ======== {chance} ==============')
                    if chance == 2:
                        print(f"{player} Usou ataque forte ! ")
                        i_vida -= p_dano2
                        sleep(1)
                        print('Avançando no adversario')
                        sleep(1)
                        print('\nVocê acertou ! ')
                        sleep(1)
                        print('====== Relatorio Combate =====')
                        sleep(1)
                        print(f"você causou {p_dano2} de dano no inimigo {inimigo} e agora ele está com {i_vida} de pontos de vida")
                        sleep(2)
                        print('===============================')

                    if chance != 2:
                        print(f"{player} Usou ataque forte ! ")
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

                elif atq == 3:
                    print(p_vida)
                    p_vida += p_cura
                    print(p_vida)
                if p_vida <=0:
                    print(f"{player} Morreu. ")
                if i_vida > 0 :
                        print(f"{inimigo} Avançou no Player ! ")
                        print('eu estou vivo')
                elif i_vida <=0:
                    print(f"{inimigo} Está incapacitado.  ")
                    upar_p(i_xp,i_vida)
                    print(f"{player} Eliminou {inimigo}. ")
                    Hud_player()
                    






def combate_orc():
    luta(player=player['nome'],
         p_dano=player['dano'][0],
         p_vida=player['vida'],
         p_cura=player['cura'] ,
         p_dano2=player['dano'][1],
         inimigo=Orc_caverna['nome'],
         i_vida=Orc_caverna['vida'],
         i_dano=Orc_caverna['dano'],
         i_dano2=Orc_caverna['dano2'],
         i_xp= Orc_caverna['exp']
        
         )    


def combate_mf():
    luta(player=player['nome'],
         p_dano=player['dano'][0],
         p_vida=player['vida'] ,
         p_cura=player['cura'] ,
         p_dano2=player['dano'][1],
         inimigo=Monstro_floresta['nome'],
         i_vida=Monstro_floresta['vida'],
         i_dano=Monstro_floresta['dano'],
         i_dano2=Monstro_floresta['dano2'],
         i_xp= Monstro_floresta['exp']
         )
def combate_bd():
    luta(player=player['nome'],
         p_dano=player['dano'][0],
         p_vida=player['vida'] ,
         p_cura=player['cura'] ,
         p_dano2=player['dano'][1],
         inimigo=Bandido['nome'],
         i_vida=Bandido['vida'],
         i_dano=Bandido['dano'],
         i_dano2=Bandido['dano2'],
         i_xp= Bandido['exp']
         )





#combate_mf()

#combate_bd()
#combate_orc()

def jogar():
    combate_orc()
    while player['vida'] >0:
        luta()

        if player['vida'] <=0:
            print('O player esta morto... ')
            x = int(input('Deseja tentar novamente ? 1)s 2)n '))
            if x == 1:
                jogar()


#jogar()

combate_mf()
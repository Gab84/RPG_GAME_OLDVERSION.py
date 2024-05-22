from Inimigo import *
from Player import player
from time import sleep
from Textos import *

def chances():
  global chance
  chance = 2
  return chance

def p_curar():
    player['vida'] += player['cura']
    

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

def golpe_a_i(i_dano,i_dano2,):
    chances()
    if chance >= 2:
        def golpe_f():
            print(f"Sou inimigo e usei golpe basico e causei {i_dano} de dano !")
            player['vida'] -= i_dano
        golpe_f()
    elif chance <= 2:
        def golpe_b():
            print(f"Sou inimigo e usei golpe forte e causei {i_dano2} !")
            player['vida'] -= i_dano2
        golpe_b()

def luta(p,inimigo,i_vida,p_vida,p_dano,i_dano,p_dano2,i_dano2,p_cura,i_level,i_xp,): #p_xp,p_nv
    print(f"{p} Está em batalha contra > {inimigo} <")
    if p_vida > 0:
        while p_vida >0:
                Hud_player()
                if i_vida > 0:
                    print(f"Inimigo: {inimigo} | Vida: {i_vida} | Nivel: {i_level} | Exp: {i_xp} |")
                atq = int(input('Deseja usar qual golpe? '))
                #golpe fraco
                if atq == 1:
                    chances()
                    print(f'essa foi a chance de golpe ======== {chance} ==============')
                    if chance <= 3:
                        sleep(1)
                        print(f"{p} Usou ataque basico !\n ")
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
                        print(f"{p} Usou ataque basico !\n ")
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
                #golpe forte
                elif atq == 2:
                    chances()
                    print(f'essa foi a chance de golpe ======== {chance} ==============')
                    if chance == 2:
                        print(f"{p} Usou ataque forte ! ")
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
                        print(f"{p} Usou ataque forte ! ")
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
                #Cura
                elif atq == 3:
                    print(p_vida)
                    p_curar()
                    print(f"{p} curou {p_cura} essa é a nova vida do p {player['vida']}")
                    
                    
                if p_vida <=0:
                    print(f"{p} Morreu. ")
                if i_vida > 0 :
                        print(f"{inimigo} Avançou no p ! ")
                        print('eu estou vivo')
                        golpe_a_i(i_dano,i_dano2)
                elif i_vida <=0:
                    upar_p(i_xp,i_vida)
                    Hud_player()
                    print(f"Inimigo: {inimigo} | Vida: {i_vida} | Nivel: {i_level} | Exp: {i_xp} |")
                    print(f"{inimigo} Está incapacitado.  ")
                    
                    print(f"{p} Eliminou {inimigo}. ")
                    perg = int(input("Deseja ir pro proximo inimigo? // usar item // seguir lore //"))
                    if  perg == 3:  #// faz ação desejada
                        print('Chamar função da proxima parte da historia') #
                        
                    if perg == 2:
                        x = int(input(f"Seus itens são {player['inventario']} deseja usar qual ? > "))
                        if x ==1:
                            p_curar()
                    
        
                        






def combate_orc():
    luta(p=player['nome'],
         p_dano=player['dano'][0],
         p_vida=player['vida'],
         p_cura=player['cura'] ,
         p_dano2=player['dano'][1],
         #p_xp=player['exp'],
         #p_nv=player['level'],
         inimigo=Orc_caverna['nome'],
         i_vida=Orc_caverna['vida'],
         i_dano=Orc_caverna['dano'],
         i_dano2=Orc_caverna['dano2'],
         i_xp= Orc_caverna['exp'],
         i_level=Orc_caverna['level']

         )    


def combate_mf():
    luta(p=player['nome'],
         p_dano=player['dano'][0],
         p_vida=player['vida'] ,
         p_cura=player['cura'] ,
         p_dano2=player['dano'][1],
         #p_xp=player['exp'],
         #p_nv=player['level'],
         inimigo=Monstro_floresta['nome'],
         i_vida=Monstro_floresta['vida'],
         i_dano=Monstro_floresta['dano'],
         i_dano2=Monstro_floresta['dano2'],
         i_xp= Monstro_floresta['exp'],
         i_level=Monstro_floresta['level']
         )
    
def combate_bd():
    luta(p=player['nome'],
         p_dano=player['dano'][0],
         p_vida=player['vida'] ,
         p_cura=player['cura'] ,
         p_dano2=player['dano'][1],
         #p_xp=player['exp'],
         #p_nv=player['level'],
         inimigo=Bandido['nome'],
         i_vida=Bandido['vida'],
         i_dano=Bandido['dano'],
         i_dano2=Bandido['dano2'],
         i_xp= Bandido['exp'],
         i_level=Bandido['level']
         )
def combate_goblin():
    luta(p=player['nome'],
         p_dano=player['dano'][0],
         p_vida=player['vida'] ,
         p_cura=player['cura'] ,
         p_dano2=player['dano'][1],
         #p_xp=player['exp'],
         #p_nv=player['level'],
         inimigo=Goblin['nome'],
         i_vida=Goblin['vida'],
         i_dano=Goblin['dano'],
         i_dano2=Goblin['dano2'],
         i_xp= Goblin['exp'],
         i_level=Goblin['level']
         )
def combate_Banche():
    luta(p=player['nome'],
         p_dano=player['dano'][0],
         p_vida=player['vida'] ,
         p_cura=player['cura'] ,
         p_dano2=player['dano'][1],
         #p_xp=player['exp'],
         #p_nv=player['level'],
         inimigo=Banche['nome'],
         i_vida=Banche['vida'],
         i_dano=Banche['dano'],
         i_dano2=Banche['dano2'],
         i_xp= Banche['exp'],
         i_level=Banche['level']
         )





#combate_mf()

#combate_bd()
#combate_orc()

"""def jogar():
    combate_orc()
    while player['vida'] >0:
        luta()

        if player['vida'] <=0:
            print('O player esta morto... ')
            x = int(input('Deseja tentar novamente ? 1)s 2)n '))
            if x == 1:
                jogar()


#jogar()"""

#combate_Banche()
import sys
import platform
import os
from Inimigo import *
from Player import player
from time import sleep
from Textos import *
from classes import *
from Itens import *
from status import distribuir_pt
from Loja import *

def parar():
   sys.exit()


def clear_terminal():
    system_name = platform.system()
    if system_name == "Windows":
        os.system('cls')
    else:
        os.system('clear')


def chances():
  global chance
  chance = randint(0,6)
  return chance

def p_curar():
    player['vida'] += player['cura']
    if player['vida'] > player['vida_max']:
        player['vida'] = player['vida_max']

def defender(dano):
    player['vida'] = dano
    

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
        distribuir_pt()
        print(player)

def up():
    upar_p()

def golpe_a_i(i_dano,i_dano2,i_nome):
    chances()
    if chance >= 2:
        def golpe_b():
            print(f"{i_nome} USOU ATAQUE BASICO !")
            sleep(1)
            if player['defesa'] > 0:
                player['defesa'] -= i_dano
                if player['defesa'] <= 0 :
                    player['vida'] -= i_dano
            print(f"{i_nome} ESTÁ AVANÇANDO !")
            sleep(1)
            print(f"{i_nome} ACERTOU O GOLPE ! !")
            sleep(1)
            print('====== RELATORIO =====')
            print(f"{i_nome} CAUSOU {i_dano} DE DANO")
            print('====== RELATORIO =====')
            sleep(2)
        golpe_b()                   
    elif chance <= 2:
        def golpe_b():
            print(f"{i_nome} USOU ATAQUE FORTE !")
            sleep(1)
            print(f"{i_nome} ESTÁ AVANÇANDO !")
            sleep(1)
            if player['defesa'] > 0:
                player['defesa'] -= i_dano2
                if player['defesa'] <= 0 :
                    player['vida'] -= i_dano2
            print(f"{i_nome} ACERTOU O GOLPE ! !")
            sleep(1)
            print('====== RELATORIO =====')
            print(f"{i_nome} CAUSOU {i_dano2} DE DANO")
            print('====== RELATORIO =====')
            sleep(2)

        golpe_b()

def inventario():
    print('*SE O SEU INVENTARIO ESTIVER VAZIO OU VOCÊ ESCOLHER UM ITEM QUE NÃO EXISTE, VOCÊ IRA AVANÇAR SEM UTILIZAR NENHUM ITEM*')
    x = int(input(f"Seus itens são {player['inventario']} deseja usar qual ? > "))-1
    if 0 <= x < len(player['inventario']): # Verificando se o índice está dentro do intervalo válido
        item_desejado = player['inventario'][x] # Acessando o item pelo índice fornecido
        print("VOCÊ QUER USAR :", item_desejado)
        sleep(1)
        print('PROCURANDO O ITEM NA BOLSA 🎒....')
        sleep(1)
        print('ACHEI !')
        # Removendo o item da lista
        player['inventario'].pop(x)
        print("ITEM FOI USADO E REMOVIDO DO SEU IVENTARIO")
            #Executando a função correspondente ao item
        if item_desejado in funcoes_consumiveis:
            funcoes_consumiveis[item_desejado]()
            novo_i_aleatorio()
            reset_inimigos() 

            
        else:
            print("COMO TU CONSEGUIU ESSE ITEM? NUM ERA NEM PRA ELE EXISTIR CARA")
        
    else:
        print("ESSE ITEM NÃO ESTÁ NO SEU INVENTARIO OU SEU INVENTARIO ESTÁ VAZIO.")
        novo_i_aleatorio()
        reset_inimigos() 


def inventario_m():
    print('*SE O SEU INVENTARIO ESTIVER VAZIO OU VOCÊ ESCOLHER UM ITEM QUE NÃO EXISTE, VOCÊ IRA AVANÇAR SEM UTILIZAR NENHUM ITEM*')
    x = int(input(f"Seus itens são {player['inventario']} deseja usar qual ? > "))-1
    if 0 <= x < len(player['inventario']): # Verificando se o índice está dentro do intervalo válido
        item_desejado = player['inventario'][x] # Acessando o item pelo índice fornecido
        print("VOCÊ QUER USAR :", item_desejado)
        sleep(1)
        print('PROCURANDO O ITEM NA BOLSA 🎒....')
        sleep(1)
        print('ACHEI !')
        # Removendo o item da lista
        player['inventario'].pop(x)
        print("ITEM FOI USADO E REMOVIDO DO SEU IVENTARIO")
            #Executando a função correspondente ao item
        if item_desejado in funcoes_consumiveis:
            funcoes_consumiveis[item_desejado]()
        else:
            print("COMO TU CONSEGUIU ESSE ITEM? NUM ERA NEM PRA ELE EXISTIR CARA")
        
    else:
        print("ESSE ITEM NÃO ESTÁ NO SEU INVENTARIO OU SEU INVENTARIO ESTÁ VAZIO.")



def luta(p,inimigo,i_vida,i_vida_m,p_vida,p_vida_m,p_dano,i_dano,p_dano2,i_dano2,p_cura,i_level,i_xp,p_atq_1,p_atq_2,): #p_xp,p_nv
    sleep(3)
    clear_terminal()
    sleep(1)
    txt_btl()
    if p_vida > 0:
        while p_vida >0:
                
                Hud_player()
                display_player_hp_bar(current_hp=p_vida,max_hp=p_vida,bar_length=10)
                if i_vida > 0:
                    display_npc_hp_bar(current_hp=i_vida,max_hp=i_vida_m,i_level=i_level,i_xp=i_xp,inimigo=inimigo,bar_length=10)
                atq = int(input(f"DESEJA FAZER OQUE? \nAÇÕOES -->  {player['golpes'][0]}🗡️  : DANO : {player['dano'][0]} ❤️  | {player['golpes'][1]}🗡️  : DANO : {player['dano'][1]} ❤️  | {player['golpes'][2]} 🩹 : CURA: {player['cura']} ❤️  | {player['golpes'][3]}🎒 : ABRIR INVENTARIO \n> "))
                clear_terminal()
                classe_tipo = determinar_classe_tipo(player['classe'])
                if classe_tipo == 'Magias':
                    if player['mana'] >0:
                        if atq == 1:
                            player['mana'] -= 10
                        if atq == 2:
                            player['mana'] -= 15
                    elif player['mana'] <=9:
                        print('Você não tem mana o suficiente. Utilize algum item. ')
                        inventario_m()
                        
                #golpe fraco
                if atq == 1:
                    chances()
                    #print(f'essa foi a chance de golpe ======== {chance} ==============')
                    if chance <= 4:
                        sleep(1)
                        print(f"{p} Usou {p_atq_1} !\n ")
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
                    if chance >= 5:
                        sleep(1)
                        print(f"{p} Usou {p_atq_1} !\n ")
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
                    #print(f'essa foi a chance de golpe ======== {chance} ==============')
                    if chance <= 3:
                        print(f"{p} Usou {p_atq_2} ! ")
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

                    if chance >= 4:
                        print(f"{p} Usou {p_atq_2} ! ")
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
                    #print(p_vida)
                    p_curar()
                    print(f"{p} curou {p_cura} essa é a nova vida do p {player['vida']}")
                
                elif atq == 4:
                    inventario_m()

                    

                if i_vida > 0 :
                        print(f"{inimigo} Avançou no p ! ")
                        sleep(1)
                        chances()
                        if chance > 2:
                            sleep(1)
                            golpe_a_i(i_dano,i_dano2,inimigo)
                        else:
                            sleep(1)
                            print(f"{inimigo} USOU ATAQUE BASICO !")
                            sleep(1)
                            print(f"{inimigo} ESTÁ AVANÇANDO !")
                            sleep(1)
                            print(f"{inimigo} ERROU ! !")
                            sleep(1)
                            print('====== RELATORIO =====')
                            print(f"{inimigo} NÃO CAUSOU NADINHA DE DANO")
                            print('====== RELATORIO =====')
                            sleep(2)

                if player['vida'] <=0:
                    Hud_player()
                    print(f"{p} NÃO TANKOU O BOSTIL E FOI DE F ")
                    sleep(2)
                    print('FIM DE JOGO, TENTE NOVAMENTE.')
                    sleep(2)
                    parar()

                elif i_vida <=0:
                    upar_p(i_xp,i_vida)
                    Hud_player()
                    print(f"Inimigo: {inimigo} | Vida: {i_vida} | Nivel: {i_level} | Exp: {i_xp} |")
                    sleep(2)
                    print(f"{inimigo} ESTÁ MORTIN DA SILVA  ")
                    
                    print(f"{p} Eliminou {inimigo}. ")
                    coin = randint(10,17)
                    print(F"O INIMIGO DEIXOU {coin} DINHEIROS💸, VOCÊ QUE NÃO É BOBO JÁ LANÇOU PROS BOLSO")
                    player['dinheiro'] += coin
                    perg = int(input("Deseja ir pro proximo inimigo? // usar item // seguir lore //"))
                    if  perg == 3:  #// faz ação desejada
                        reset_inimigos()
                        print('Chamar função da proxima parte da historia') #
                        
                    if perg == 2:
                        inventario()

                            
                    if perg == 1:
                        novo_i_aleatorio()
                        reset_inimigos()  
                    
                    
        
def combate_orc():
    luta(p=player['nome'],
         p_dano=player['dano'][0],
         p_vida=player['vida'],
         p_cura=player['cura'] ,
         p_dano2=player['dano'][1],
         p_atq_1=player['golpes'][0],
         p_atq_2=player['golpes'][1],
         inimigo='Orc_caverna',
         i_vida=Orc_caverna['vida'],
         i_dano=Orc_caverna['dano'],
         i_dano2=Orc_caverna['dano2'],
         i_xp= Orc_caverna['exp'],
         i_level=Orc_caverna['level'],
         p_vida_m=player['vida_max'],
         i_vida_m=Orc_caverna['vida_max']

         )    


def combate_mf():
    luta(p=player['nome'],
         p_dano=player['dano'][0],
         p_vida=player['vida'] ,
         p_cura=player['cura'] ,
         p_dano2=player['dano'][1],
         p_atq_1=player['golpes'][0],
         p_atq_2=player['golpes'][1],
         inimigo='Monstro da Floresta',
         i_vida=Monstro_floresta['vida'],
         i_dano=Monstro_floresta['dano'],
         i_dano2=Monstro_floresta['dano2'],
         i_xp= Monstro_floresta['exp'],
         i_level=Monstro_floresta['level'],
         p_vida_m=player['vida_max'],
         i_vida_m=Monstro_floresta['vida_max'],
        
         )
    
def combate_bd():
    luta(p=player['nome'],
         p_dano=player['dano'][0],
         p_vida=player['vida'] ,
         p_cura=player['cura'] ,
         p_dano2=player['dano'][1],
         p_atq_1=player['golpes'][0],
         p_atq_2=player['golpes'][1],
         inimigo='Bandido',
         i_vida=Bandido['vida'],
         i_dano=Bandido['dano'],
         i_dano2=Bandido['dano2'],
         i_xp= Bandido['exp'],
         i_level=Bandido['level'],
         p_vida_m=player['vida_max'],
         i_vida_m=Bandido['vida_max']
         
         )
def combate_goblin():
    luta(p=player['nome'],
         p_dano=player['dano'][0],
         p_vida=player['vida'] ,
         p_cura=player['cura'] ,
         p_dano2=player['dano'][1],
         p_atq_1=player['golpes'][0],
         p_atq_2=player['golpes'][1],
         inimigo='Goblin',
         i_vida=Goblin['vida'],
         i_dano=Goblin['dano'],
         i_dano2=Goblin['dano2'],
         i_xp= Goblin['exp'],
         i_level=Goblin['level'],
         p_vida_m=player['vida_max'],
         i_vida_m=Goblin['vida_max'],
         
         )
def combate_Banche():
    luta(p=player['nome'],
         p_dano=player['dano'][0],
         p_vida=player['vida'] ,
         p_cura=player['cura'] ,
         p_dano2=player['dano'][1],
         p_atq_1=player['golpes'][0],
         p_atq_2=player['golpes'][1],
         inimigo='Banche',
         i_vida=Banche['vida'],
         i_dano=Banche['dano'],
         i_dano2=Banche['dano2'],
         i_xp= Banche['exp'],
         i_level=Banche['level'],
         p_vida_m=player['vida_max'],
         i_vida_m=Banche['vida_max'],
         
         )

def novo_i_aleatorio():
    x = randint (1,5)
    if x == 1:
        combate_Banche()
    elif x == 2:
        combate_bd()
    elif x == 3:
        combate_goblin()
    elif x ==4:
        combate_mf()
    elif x ==5:
        combate_orc()
    

#escolha_classe()
#combate_Banche()

def Jogar():
    pass

#combate_orc()
#inventario_m()
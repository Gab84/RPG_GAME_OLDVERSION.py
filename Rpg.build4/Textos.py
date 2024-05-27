from Player import player
from Inimigo import *





def Hud_player():
    print(f"Nome: {player['nome']} | Vida: {player['vida']}/{player['vida_max']} | Mana: {player['mana']}/{player['mana_max']} | Arma: {player['armas']}  | Nivel: {player['level']} |Exp: {player['exp']}/{player['exp_max']} | Classe: {player['classe']} | Dinheiro: {player['dinheiro']} | INVENTARIO: {player['inventario']} \nDANO: FRACO: {player['dano'][0]} / FORTE: {player['dano'][1]} |")

def Hud_inimigo(i_nome,i_vida,i_level,i_xp):
    print(f"Inimigo: {i_nome} | Vida: {i_vida} | Nivel: {i_level} | Exp: {i_xp} |")

def Hud_inimigo_gb():
    Hud_inimigo(i_nome=Goblin['nome'],i_vida=Goblin['vida'],i_level=Goblin['level'],i_xp=Goblin['exp'])

def Hud_inimigo_orc():
    Hud_inimigo(i_nome=Orc_caverna['nome'],i_vida=Orc_caverna['vida'],i_level=Orc_caverna['level'],i_xp=Orc_caverna['exp'])

def Hud_inimigo_mf():
    Hud_inimigo(i_nome=Monstro_floresta['nome'],i_vida=Monstro_floresta['vida'],i_level=Monstro_floresta['level'],i_xp=Monstro_floresta['exp'])

def Hud_inimigo_bd():
    Hud_inimigo(i_nome=Bandido['nome'],i_vida=Bandido['vida'],i_level=Bandido['level'],i_xp=Bandido['exp'])
    
def Hud_inimigo_banche():
    Hud_inimigo(i_nome=Banche['nome'],i_vida=Banche['vida'],i_level=Banche['level'],i_xp=Banche['exp'])


def desc_Furtivo():
    print(f"BANDIDO  > \nVIDA : 40/80 |\nDANO: 7/5 |\nGOLPES : GOLPE_BASICO | GOLPE_FORTE | CURA |\nMANA : 50/100 | ")
    print("")
    print(f"GNOMO  > \nVIDA : 40/80 |\nDANO: 7/5 |\nGOLPES : GOLPE_BASICO | GOLPE_FORTE | CURA |\nMANA : 50/100 | ")
def desc_magia():
    pass
def desc_corpo_corpo():
    pass

def desc_armas():
    print('')
    print(f"ADAGA > DANO: 7/11 PREÇO: 10 |\nESPADA_CURTA > DANO: 15/20 PREÇO: 15 |\nCAJADO > DANO: 15/23 PREÇO: 15 |\nVARINHA > DANO: 10/20 PREÇO: 10 |\nMACHADO > DANO: 25/35 PREÇO: 20 ")

def desc_itens():
    print('')
    print(f"pot_cura > VIDA: 20 PREÇO: 15 |\npot_mana > MANA: 20 PREÇO: 10 |")


"""Hud_inimigo_gb()
Hud_inimigo_orc()
Hud_inimigo_gb()
Hud_inimigo_gb()"""
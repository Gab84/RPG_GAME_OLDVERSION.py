from Player import player
from Inimigo import *




def Hud_player():
    print(f"Nome: {player['nome']} | Vida: {player['vida']} | Nivel: {player['level']} |Exp: {player['exp']}/{player['exp_max']} |")

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



"""Hud_inimigo_gb()
Hud_inimigo_orc()
Hud_inimigo_gb()
Hud_inimigo_gb()"""
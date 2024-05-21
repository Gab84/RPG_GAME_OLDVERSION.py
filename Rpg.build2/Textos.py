from Player import player
from Inimigo import *




def Hud_player():
    print(f"Vida: {player['vida']} | Nivel: {player['level']} |Exp: {player['exp']}/{player['exp_max']} |")

def Hud_inimigo(i_vida,i_level,i_xp):
    print(f"Vida: {i_vida} | Nivel: {i_level} | Exp: {i_xp} |")

def Hud_inimigo_gb():
    Hud_inimigo(i_vida=Goblin['vida'],i_level=Goblin['level'],i_xp=Goblin['exp'])

def Hud_inimigo_orc():
    Hud_inimigo(i_vida=Orc_caverna['vida'],i_level=Orc_caverna['level'],i_xp=Orc_caverna['exp'])

def Hud_inimigo_mf():
    Hud_inimigo(i_vida=Monstro_floresta['vida'],i_level=Monstro_floresta['level'],i_xp=Monstro_floresta['exp'])

def Hud_inimigo_bd():
    Hud_inimigo(i_vida=Bandido['vida'],i_level=Bandido['level'],i_xp=Bandido['exp'])


Hud_inimigo_gb()
Hud_inimigo_orc()
Hud_inimigo_gb()
Hud_inimigo_gb()
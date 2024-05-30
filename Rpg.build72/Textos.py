from Player import player
from Inimigo import *
import time
import sys
from Raridadesf import exibir_item_com_cor
from Itens import armas

def calcular_defesa_total(p):
    defesa_total = 0
    for armadura in p['armaduras_equipadas']:
        defesa_total += armadura['def']
    return defesa_total
    


def display_npc_hp_bar(current_hp, max_hp,inimigo,i_level,i_xp, bar_length=10):
    ratio = current_hp / max_hp

    white_squares = int(ratio * bar_length)
    black_squares = bar_length - white_squares

    npc_hp_bar = "❤️ " * white_squares + "🤍" * black_squares
    print(f"""------------------------------
INIMIGO 💀 : \033[91m{inimigo}\033[0m 
------------------------------
Vida: {npc_hp_bar} 
            {current_hp}/{max_hp}           
Nivel 🌟 : {i_level} | Exp 📚 : {i_xp} 
            """)
    
    return npc_hp_bar

def display_player_hp_bar(current_hp, max_hp, bar_length=10):
    ratio = current_hp / max_hp

    white_squares = int(ratio * bar_length)
    black_squares = bar_length - white_squares

    player_hp_bar = "❤️ " * white_squares + "🤍" * black_squares

    #print(f"\033[36m{player['nome']}\033[0m {player_hp_bar}  ")
    

    return player_hp_bar

def xp_bar(xp_atual,xp_max,bar_lenght=10):
    ratio = xp_atual / xp_max

    white_squares = int(ratio * bar_lenght)
    black_squares = bar_lenght - white_squares

    player_xp_bar = "🔷 " * white_squares + "⚪" * black_squares

    #print(f"\033[36m{player['nome']}\033[0m {player_xp_bar}  ")
    
    
    return player_xp_bar    

def mana_bar(man_atual,mana_max,bar_lenght=10):
    ratio = man_atual / mana_max

    white_squares = int(ratio * bar_lenght)
    black_squares = bar_lenght - white_squares

    player_mana_bar = "🟣 " * white_squares + "⚪" * black_squares

    #print(f"\033[36m{player['nome']}\033[0m {player_xp_bar}  ")
    
    
    return player_mana_bar    



def Hud_player():
    player_mana_bar = mana_bar(man_atual=player['mana'], mana_max=player['mana_max'])
    player_xp_bar = xp_bar(xp_atual=player['exp'], xp_max=player['exp_max'])
    player_hp_bar = display_player_hp_bar(current_hp=player['vida'], max_hp=player['vida_max'])
    
    armaduras_equipadas = [armadura['nome_colorido'] for armadura in player['armaduras_equipadas'].values()]
    defesa_total = player['defesa']
    
    print(f"""------------------------------
JOGADOR 👤 : {player['nome']} 
------------------------------
Vida: {player_hp_bar} | Mana: {player_mana_bar} 
            {player['vida']}/{player['vida_max']}                       {player['mana']}/{player['mana_max']}                
------------------------------
Armaduras 🛡️ : {', '.join(armaduras_equipadas) if armaduras_equipadas else 'Nenhuma'} | INVENTÁRIO 🎒 : {player['inventario']} | Dinheiro 💰 : {player['dinheiro']}

Arma ⚔️ : {player['armas']}

Nível 🌟 : {player['level']} | Exp 📚 : {player['exp']}/{player['exp_max']} {player_xp_bar} 

Classe 🏋️‍♀️ : {player['classe']}

Defesa Total 🛡️ : {defesa_total}

AÇÕES -->  {player['golpes'][0]}🗡️  : DANO : {player['dano'][0]} ❤️  | {player['golpes'][1]}🗡️  : DANO : {player['dano'][1]} ❤️  | {player['golpes'][2]} 🩹 : CURA: {player['cura']} ❤️  | {player['golpes'][3]}🎒 : ABRIR INVENTÁRIO
------------------------------""")


def Hud_inimigo(i_nome,i_vida,i_vida_m,i_level,i_xp):
    npc_hp_bar=display_npc_hp_bar(current_hp=i_vida,max_hp=i_vida_m)
    print(f"Inimigo: {i_nome} | Vida: {i_vida} {npc_hp_bar} | Nivel: {i_level} | Exp: {i_xp} |")

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

def desc_armaduras():
    print('')
    print(f"CAPACETE > DEFESA: 3 PREÇO: 10 |\nPEITORAL > DEFESA: 5 PREÇO: 20 |\nCALÇA > DEFESA:  4 PREÇO: 15 |\nBOTA > DEFESA: 2 PREÇO: 5")

def desc_itens():
    print('')
    print(f"suco de maça🧃 > VIDA: 20 PREÇO: 15 |\ncafezin🥤 > MANA: 20 PREÇO: 10 |")


def txt_btl():
    print(f""" ██▒   █▓ ▒█████   ▄████▄  ▓█████    ▓█████   ██████ ▄▄▄█████▓ ▄▄▄         ▓█████  ███▄ ▄███▓    ▄▄▄▄    ▄▄▄     ▄▄▄█████▓ ▄▄▄       ██▓     ██░ ██  ▄▄▄      
▓██░   █▒▒██▒  ██▒▒██▀ ▀█  ▓█   ▀    ▓█   ▀ ▒██    ▒ ▓  ██▒ ▓▒▒████▄       ▓█   ▀ ▓██▒▀█▀ ██▒   ▓█████▄ ▒████▄   ▓  ██▒ ▓▒▒████▄    ▓██▒    ▓██░ ██▒▒████▄    
 ▓██  █▒░▒██░  ██▒▒▓█    ▄ ▒███      ▒███   ░ ▓██▄   ▒ ▓██░ ▒░▒██  ▀█▄     ▒███   ▓██    ▓██░   ▒██▒ ▄██▒██  ▀█▄ ▒ ▓██░ ▒░▒██  ▀█▄  ▒██░    ▒██▀▀██░▒██  ▀█▄  
  ▒██ █░░▒██   ██░▒▓▓▄ ▄██▒▒▓█  ▄    ▒▓█  ▄   ▒   ██▒░ ▓██▓ ░ ░██▄▄▄▄██    ▒▓█  ▄ ▒██    ▒██    ▒██░█▀  ░██▄▄▄▄██░ ▓██▓ ░ ░██▄▄▄▄██ ▒██░    ░▓█ ░██ ░██▄▄▄▄██ 
   ▒▀█░  ░ ████▓▒░▒ ▓███▀ ░░▒████▒   ░▒████▒▒██████▒▒  ▒██▒ ░  ▓█   ▓██▒   ░▒████▒▒██▒   ░██▒   ░▓█  ▀█▓ ▓█   ▓██▒ ▒██▒ ░  ▓█   ▓██▒░██████▒░▓█▒░██▓ ▓█   ▓██▒
   ░ ▐░  ░ ▒░▒░▒░ ░ ░▒ ▒  ░░░ ▒░ ░   ░░ ▒░ ░▒ ▒▓▒ ▒ ░  ▒ ░░    ▒▒   ▓▒█░   ░░ ▒░ ░░ ▒░   ░  ░   ░▒▓███▀▒ ▒▒   ▓▒█░ ▒ ░░    ▒▒   ▓▒█░░ ▒░▓  ░ ▒ ░░▒░▒ ▒▒   ▓▒█░
   ░ ░░    ░ ▒ ▒░   ░  ▒    ░ ░  ░    ░ ░  ░░ ░▒  ░ ░    ░      ▒   ▒▒ ░    ░ ░  ░░  ░      ░   ▒░▒   ░   ▒   ▒▒ ░   ░      ▒   ▒▒ ░░ ░ ▒  ░ ▒ ░▒░ ░  ▒   ▒▒ ░
     ░░  ░ ░ ░ ▒  ░           ░         ░   ░  ░  ░    ░        ░   ▒         ░   ░      ░       ░    ░   ░   ▒    ░        ░   ▒     ░ ░    ░  ░░ ░  ░   ▒   
      ░      ░ ░  ░ ░         ░  ░      ░  ░      ░                 ░  ░      ░  ░       ░       ░            ░  ░              ░  ░    ░  ░ ░  ░  ░      ░  ░
     ░            ░                                                                                   ░                                                       """)



def txt_lj_i():
    print("""▄▄▌         ▐▄▄▄ ▄▄▄·     ·▄▄▄▄  ▄▄▄ .    ▪  ▄▄▄▄▄▄▄▄ . ▐ ▄ .▄▄ · 
██•  ▪       ·██▐█ ▀█     ██▪ ██ ▀▄.▀·    ██ •██  ▀▄.▀·•█▌▐█▐█ ▀. 
██▪   ▄█▀▄ ▪▄ ██▄█▀▀█     ▐█· ▐█▌▐▀▀▪▄    ▐█· ▐█.▪▐▀▀▪▄▐█▐▐▌▄▀▀▀█▄
▐█▌▐▌▐█▌.▐▌▐▌▐█▌▐█ ▪▐▌    ██. ██ ▐█▄▄▌    ▐█▌ ▐█▌·▐█▄▄▌██▐█▌▐█▄▪▐█
.▀▀▀  ▀█▄▀▪ ▀▀▀• ▀  ▀     ▀▀▀▀▀•  ▀▀▀     ▀▀▀ ▀▀▀  ▀▀▀ ▀▀ █▪ ▀▀▀▀ """)
    
    

def txt_lj_a():
    print(""" ▄█        ▄██████▄       ▄█    ▄████████      ████████▄     ▄████████         ▄████████    ▄████████   ▄▄▄▄███▄▄▄▄      ▄████████    ▄████████
███       ███    ███     ███   ███    ███      ███   ▀███   ███    ███        ███    ███   ███    ███ ▄██▀▀▀███▀▀▀██▄   ███    ███   ███    ███
███       ███    ███     ███   ███    ███      ███    ███   ███    █▀         ███    ███   ███    ███ ███   ███   ███   ███    ███   ███    █▀ 
███       ███    ███     ███   ███    ███      ███    ███  ▄███▄▄▄            ███    ███  ▄███▄▄▄▄██▀ ███   ███   ███   ███    ███   ███       
███       ███    ███     ███ ▀███████████      ███    ███ ▀▀███▀▀▀          ▀███████████ ▀▀███▀▀▀▀▀   ███   ███   ███ ▀███████████ ▀███████████
███       ███    ███     ███   ███    ███      ███    ███   ███    █▄         ███    ███ ▀███████████ ███   ███   ███   ███    ███          ███
███▌    ▄ ███    ███     ███   ███    ███      ███   ▄███   ███    ███        ███    ███   ███    ███ ███   ███   ███   ███    ███    ▄█    ███
█████▄▄██  ▀██████▀  █▄ ▄███   ███    █▀       ████████▀    ██████████        ███    █▀    ███    ███  ▀█   ███   █▀    ███    █▀   ▄████████▀ 
▀                    ▀▀▀▀▀▀                                                                ███    ███                                          """)

"""Hud_inimigo_gb()
Hud_inimigo_orc()
Hud_inimigo_gb()
Hud_inimigo_gb()"""

#xp_bar(xp_atual=player['exp'],xp_max=player['exp_max'])

#Hud_player()

def txt_lj_ar():
    print(""" █████          ███████          █████   █████████      ██████████   ██████████      █████████   ███████████   ██████   ██████   █████████   ██████████   █████  █████ ███████████     █████████    █████████ 
░░███         ███░░░░░███       ░░███   ███░░░░░███    ░░███░░░░███ ░░███░░░░░█     ███░░░░░███ ░░███░░░░░███ ░░██████ ██████   ███░░░░░███ ░░███░░░░███ ░░███  ░░███ ░░███░░░░░███   ███░░░░░███  ███░░░░░███
 ░███        ███     ░░███       ░███  ░███    ░███     ░███   ░░███ ░███  █ ░     ░███    ░███  ░███    ░███  ░███░█████░███  ░███    ░███  ░███   ░░███ ░███   ░███  ░███    ░███  ░███    ░███ ░███    ░░░ 
 ░███       ░███      ░███       ░███  ░███████████     ░███    ░███ ░██████       ░███████████  ░██████████   ░███░░███ ░███  ░███████████  ░███    ░███ ░███   ░███  ░██████████   ░███████████ ░░█████████ 
 ░███       ░███      ░███       ░███  ░███░░░░░███     ░███    ░███ ░███░░█       ░███░░░░░███  ░███░░░░░███  ░███ ░░░  ░███  ░███░░░░░███  ░███    ░███ ░███   ░███  ░███░░░░░███  ░███░░░░░███  ░░░░░░░░███
 ░███      █░░███     ███  ███   ░███  ░███    ░███     ░███    ███  ░███ ░   █    ░███    ░███  ░███    ░███  ░███      ░███  ░███    ░███  ░███    ███  ░███   ░███  ░███    ░███  ░███    ░███  ███    ░███
 ███████████ ░░░███████░  ░░████████   █████   █████    ██████████   ██████████    █████   █████ █████   █████ █████     █████ █████   █████ ██████████   ░░████████   █████   █████ █████   █████░░█████████ 
░░░░░░░░░░░    ░░░░░░░     ░░░░░░░░   ░░░░░   ░░░░░    ░░░░░░░░░░   ░░░░░░░░░░    ░░░░░   ░░░░░ ░░░░░   ░░░░░ ░░░░░     ░░░░░ ░░░░░   ░░░░░ ░░░░░░░░░░     ░░░░░░░░   ░░░░░   ░░░░░ ░░░░░   ░░░░░  ░░░░░░░░░  """)

def txt_str():
    print(""" 

▄▀▀▀▀▄  ▄▀▀█▄   ▄▀▄▄▄▄   ▄▀▀▄▀▀▀▄  ▄▀▀█▄   ▄▀▀▄ ▄▀▄  ▄▀▀█▄▄▄▄  ▄▀▀▄ ▀▄  ▄▀▀▀█▀▀▄  ▄▀▀▀▀▄ 
█ █   ▐ ▐ ▄▀ ▀▄ █ █    ▌ █   █   █ ▐ ▄▀ ▀▄ █  █ ▀  █ ▐  ▄▀   ▐ █  █ █ █ █    █  ▐ █      █
   ▀▄     █▄▄▄█ ▐ █      ▐  █▀▀█▀    █▄▄▄█ ▐  █    █   █▄▄▄▄▄  ▐  █  ▀█ ▐   █     █      █
▀▄   █   ▄▀   █   █       ▄▀    █   ▄▀   █   █    █    █    ▌    █   █     █      ▀▄    ▄▀
 █▀▀▀   █   ▄▀   ▄▀▄▄▄▄▀ █     █   █   ▄▀  ▄▀   ▄▀    ▄▀▄▄▄▄   ▄▀   █    ▄▀         ▀▀▀▀  
 ▐      ▐   ▐   █     ▐  ▐     ▐   ▐   ▐   █    █     █    ▐   █    ▐   █                 
                ▐                          ▐    ▐     ▐        ▐        ▐                 
                
                                                                                                    LORE BY > CLEBER/GAB 
                                                                                                    PROGRAMAÇÃO > GAB 
          """)




def txtlore(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  
    

#txtlore("TEXTO", delay=0.05)
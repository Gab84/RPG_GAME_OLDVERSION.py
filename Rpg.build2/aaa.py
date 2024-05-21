a = 0
b = 1


def combate_orc_x():
    luta(player=Orc_caverna['nome'],
         p_dano=Orc_caverna['dano'][0],
         p_vida=Orc_caverna['vida'],
         p_cura=Orc_caverna['cura'] ,
         p_dano2=Orc_caverna['dano'][1],
         inimigo=player['nome'],
         i_vida=player['vida'],
         i_dano=player['dano'],
         i_dano2=player['dano2'],
         i_xp= player['exp']
        
         )    
    

def p_a_luta_mf():
    def up_player():
        if player['exp'] >= player['exp_max']:
            print('OMG !! Você Upou de nível, confira seus novos atributos!!!!')
            player['level'] += 1
            player['exp'] = 0
            player['exp_max'] += 15
            player['vida_max'] += 20
            player['dano'][0] += 5
            player['dano'][1] += 7
            player['vida'] = player['vida_max']
            player['mana_max'] += 30
            print(player)
    up_player()


def combate_Banche():
    luta(player=player['nome'],
         p_dano=player['dano'][0],
         p_vida=player['vida'] ,
         p_cura=player['cura'] ,
         p_dano2=player['dano'][1],
         inimigo=Banche['nome'],
         i_vida=Banche['vida'],
         i_dano=Banche['dano'],
         i_dano2=Banche['dano2'],
         i_xp= Banche['exp']
         )


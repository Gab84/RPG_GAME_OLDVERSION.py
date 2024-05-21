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
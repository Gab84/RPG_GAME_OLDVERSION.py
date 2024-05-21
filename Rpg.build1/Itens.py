from Player import player

#danos spada madeira
spd_madeira_f = player['dano'][0] * 20
spd_madeira_ft = (player['dano'][1] * 25) + 5
spd_pedra_f = player['dano'][0] * 20
spd_pedra_ft = (player['dano'][1] * 35) + 5
## dano player vai ser dano da arma *** por dano base  /// fazer isso

armas = {

    'nome' : ['madeira','pedra',],
    'dano' : [spd_madeira_f,spd_madeira_ft,spd_pedra_f,spd_pedra_ft,],

}
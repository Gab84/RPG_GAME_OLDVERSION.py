from random import randint

level = randint(1,3)  #master piece


#definindo os atb do inimigo tbm
dano_Mf = 7*level
dano_bd = 3*level
dano_orc = 11*level
dano_Mf2 = 9*level
dano_bd2 = 4*level
dano_orc2 = 15*level
vida_mf = 40*level
vida_bd = 20*level
vida_orc = 60*level
xp_mf = 8*level
xp_bd = 7*level
xp_orc = 13*level

dano_goblin = 2*level
dano_goblin2 = 3*level
vida_goblin = 5*level
xp_goblin = 3*level

dano_Banche = 15*level
dano_Banche2 = 20*level
vida_Banche = 5*level
xp_Banche = 9*level
    


Monstro_floresta = {
      'nome': 'Monstro da Floresta',
      'level': level,
      'dano': dano_Mf,
      'dano2': dano_Mf2,
      'vida': vida_mf,
      'vida_max' : vida_mf,
      'exp' : xp_mf,
      'vida_min' : 0,
  }

Bandido = {
      'nome': 'Bandido',
      'level': level,
      'dano': dano_bd,
      'dano2': dano_bd2,
      'vida': vida_bd,
      'vida_max' : vida_bd,
      'exp' : xp_bd,
      'vida_min' : 0,
  }

Orc_caverna = {
      'nome': 'Orc_caverna',
      'level': level,
      'dano': dano_orc,
      'dano2': dano_orc2,
      'vida': vida_orc,
      'vida_max' : vida_orc,
      'exp' : xp_orc,
      'vida_min' : 0,
  }

Goblin = {
      'nome': 'Goblin',
      'level': level,
      'dano': dano_goblin,
      'dano2': dano_goblin2,
      'vida': vida_goblin,
      'vida_max' : vida_goblin,
      'exp' : xp_goblin,
      'vida_min' : 0,
  }

Banche = {
      'nome': 'Banche',
      'level': level,
      'dano': dano_Banche,
      'dano2': dano_Banche2,
      'vida': vida_Banche,
      'vida_max' : vida_Banche,
      'exp' : xp_Banche,
      'vida_min' : 0,
  }


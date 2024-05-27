from Player import player
from Textos import desc_armas,Hud_player

armas = {
    'adaga':{
        'nome':'adaga',
        'dano':[7,11],
        'preco' : 10,
    },
    
    'espada_curta':{
        'dano':[15,20],
        'nome':'espada_curta',
        'preco' : 15,

    },
    'cajado':{
        'dano':[15,23],
        'nome': 'cajado',
        'preco' : 10,
    },
    'varinha':{
        'dano':[10,20],
        'nome': 'varinha',
        'preco' : 10,
    },
    'machado':{
        'dano':[25,35],
        'nome' : 'machado',
        'preco' : 20,
    },
    
    
}

consumiveis = {

    'pot_cura' : {
        'nome' : 'pot_cura',
        'cura' : 20,
        'preco' : 15,
    },
    'pot_mana' : {
        'nome' : 'pot_mana',
        'cura' : 20,
        'preco' : 10
    },

}

equipamentos = {
    'capacete' : {
        'nome' : 'capacete',
        'def' : 20,
    },
    'peitoral' : {
        'nome' : 'peitoral',
        'def' : 20,
    },
    'calca' : {
        'nome' : 'calca',
        'def' : 20,
    },
    'bota' : {
        'nome' : 'bota',
        'def' : 20,
    },

    
}




#Fazer para a arma equipada ir por inventario/excluir  // fazer uma função generica pra sempre equipar a arma.
def equi_arma(p,arma,d1,d2,p_db1,p_db2):
    print(f"A arma {p['armas']} foi removido do inventario do player. ")
    p['armas'] = []
    p['armas'].append(arma)
    
    p['dano'][0] = p_db1
    p['dano'][1] = p_db2
    
    p['dano'][0] = (d1+p_db1)
    p['dano'][1] = (d2+p_db2)
    print(f"{arma} foi adicionado a mão do player. ")


def equip_adaga():    
    equi_arma(p_db1=player['dano_base'][0],p_db2=player['dano_base'][1],p=player,arma=armas['adaga']['nome'],d1=armas['adaga']['dano'][0],d2=armas['adaga']['dano'][1])
def equip_espada_curta():    
    equi_arma(p_db1=player['dano_base'][0],p_db2=player['dano_base'][1],p=player,arma=armas['espada_curta']['nome'],d1=armas['espada_curta']['dano'][0],d2=armas['espada_curta']['dano'][1])
def equip_cajado():    
    equi_arma(p_db1=player['dano_base'][0],p_db2=player['dano_base'][1],p=player,arma=armas['cajado']['nome'],d1=armas['cajado']['dano'][0],d2=armas['cajado']['dano'][1])
def equip_varinha():    
    equi_arma(p_db1=player['dano_base'][0],p_db2=player['dano_base'][1],p=player,arma=armas['varinha']['nome'],d1=armas['varinha']['dano'][0],d2=armas['varinha']['dano'][1])
def equip_machado():    
    equi_arma(p_db1=player['dano_base'][0],p_db2=player['dano_base'][1],p=player,arma=armas['machado']['nome'],d1=armas['machado']['dano'][0],d2=armas['machado']['dano'][1])


def equip_(item,p_inv):
    print(p_inv)
    
    p_inv.append(item)

    print(f"{item} foi adicionado ao do player. ")
    print(p_inv)

def equip_cura():    
    equip_(item=consumiveis['pot_cura']['nome'],p_inv=player['inventario'])
def equip_mana():    
    equip_(item=consumiveis['pot_mana']['nome'],p_inv=player['inventario'])


def usar_pot_cura():
    print("Usando Poção de Cura. Cura 20 pontos de vida.")
    player['vida'] += 20

def usar_pot_mana():
    print("Usando Poção de Mana. Recupera 20 pontos de mana.")
    player['mana'] += 20



funcoes_consumiveis = {
    'pot_cura': usar_pot_cura,
    'pot_mana': usar_pot_mana,
}



def escolha_arma():
    print('')
    print("escolha uma arma pra te acompanhar na sua viagem: ")
    print('')
    desc_armas()
    x = int(input('1) ADAGA | 2) ESPADA_CURTA | 3) CAJADO | 4) VARINHA | 5) MACHADO |'))
    if x == 1:
        equip_adaga()
        Hud_player()
    elif x ==2:
        equip_espada_curta()
        Hud_player()
    elif x == 3:
        equip_cajado()
        Hud_player()
    elif x == 4:
        equip_varinha()
        Hud_player()
    elif x == 5:
        equip_machado()
        Hud_player()
    else:
        print('ARMA NAO ENCONTRADA')
        escolha_arma()
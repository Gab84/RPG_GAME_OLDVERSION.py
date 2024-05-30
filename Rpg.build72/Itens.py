from Player import player

armas = {
    'adaga':{
        'nome':'adaga',
        'dano':[7,11],
        'preco' : 10,
        'raridade': [],
    },
    
    'espada_curta':{
        'dano':[15,20],
        'nome':'espada_curta',
        'preco' : 15,
        'raridade': [],

    },
    'cajado':{
        'dano':[15,23],
        'nome': 'cajado',
        'preco' : 10,
        'raridade': [],
    },
    'varinha':{
        'dano':[10,20],
        'nome': 'varinha',
        'preco' : 10,
        'raridade': [],
    },
    'machado':{
        'dano':[25,35],
        'nome' : 'machado',
        'preco' : 20,
        'raridade': [],
    },
    
    
}

consumiveis = {

    'suco_maça' : {
        'nome' : 'suco_maça',
        'cura' : 20,
        'preco' : 15,
        'raridade': [],
    },
    'cafezin' : {
        'nome' : 'cafezin',
        'cura' : 20,
        'preco' : 10,
        'raridade': [],
    },

}

equipamentos = {
    'capacete' : {
        'nome' : 'capacete',
        'def' : 3,
        'raridade': [],
        'preco': 10
    },
    'peitoral' : {
        'nome' : 'peitoral',
        'def' : 5,
        'raridade': [],
        'preco': 20
    },
    'calca' : {
        'nome' : 'calca',
        'def' : 4,
        'raridade': [],
        'preco': 15
    },
    'bota' : {
        'nome' : 'bota',
        'def' : 2,
        'raridade': [],
        'preco': 5
    },

    
}




#Fazer para a arma equipada ir por inventario/excluir  // fazer uma função generica pra sempre equipar a arma.


def equip_(item,p_inv):
    print(p_inv)
    
    p_inv.append(item)

    print(f"{item} foi adicionado ao do player. ")
    print(p_inv)

def equip_cura():    
    equip_(item=consumiveis['suco_maça']['nome'],p_inv=player['inventario'])
def equip_mana():    
    equip_(item=consumiveis['cafezin']['nome'],p_inv=player['inventario'])


def usar_suco_maça():
    print("Usando Suco de maça🧃 . Cura 20 pontos de vida.")
    player['vida'] += 20

def usar_cafezin():
    print("Usando Cafezin🥤 . Recupera 20 pontos de mana.")
    player['mana'] += 20



funcoes_consumiveis = {
    'suco_maça': usar_suco_maça,
    'cafezin': usar_cafezin,
}






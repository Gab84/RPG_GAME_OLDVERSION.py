from Player import player
from Personagens import *
from Textos import desc_Furtivo,Hud_player
from Itens import escolha_arma

Furtivo = {
    'nome' : player['nome'],
    'level' : player['level'],
    'exp' : player['exp'],
    'exp_max' : player['exp_max'],
    'vida' : 40,
    'vida_min': 0,
    'vida_max' : 80,
    'dano_base': [5,7,0],
    'dano' : [1000, 7, 0],
    'golpes': ["golpe_basico (1)", 'golpe_forte (2)', 'defesa(3)'],
    'armas' : [],
    'mana' : 50,
    'mana_inicial':50,
    'mana_max' : 100,
    'cura' : 10,
    'inventario' : ["pot_cura"],
    'classe' : ['1 > Bandido', '2 > Gnomo']
}

Magias = {
    'nome' : player['nome'],
    'level' : player['level'],
    'exp' : player['exp'],
    'exp_max' : player['exp_max'],
    'vida' : 30,
    'vida_min': 0,
    'vida_max' : 60,
    'dano_base': [15,3,0],
    'dano' : [15, 3, 0],
    'golpes': ["golpe_magico (1)", 'feitiço_forte (2)', 'cura(3)'],
    'armas' : [],
    'mana' : 100,
    'mana_inicial':100,
    'mana_max' : 200,
    'cura' : 5,
    'inventario' : ["pot_cura"],
    'classe' : ['1 > Bruxo', '2 > Mago']
}

Corpo_a_corpo = {
    'nome' : player['nome'],
    'level' : player['level'],
    'exp' : player['exp'],
    'exp_max' : player['exp_max'],
    'vida' : 60,
    'vida_min': 0,
    'vida_max' : 120,
    'dano_base': [1000,4,0],
    'dano' : [12, 4, 0],
    'golpes': ["soco (1)", 'chute (2)', 'bloqueio(3)'],
    'armas' : [],
    'mana' : 0,
    'mana_inicial':0,
    'mana_max' : 50,
    'cura' : 50,
    'inventario' : ["pot_cura"],
    'classe' : ['1 > Guerreiro', '2 > Barbaro']
}

def escolha_classe():
    print(f"Escolha sua classe, {player['nome']}.")
    print("Categorias disponíveis:")
    print("1 > Furtivo")
    print("2 > Magias")
    print("3 > Corpo a corpo")
    
    categoria = input('Digite o número da categoria que deseja > ')
    
    if categoria == '1':
        categorias = Furtivo
        bandido_gnomo()
        desc_Furtivo()
    elif categoria == '2':
        categorias = Magias
        bruxo_mago()
    elif categoria == '3':
        categorias = Corpo_a_corpo
        guerreiro_barbaro()
    else:
        print("Categoria não encontrada")
        return
    
    print(f"Classes disponíveis: {categorias['classe']}")
    x = input('Digite o número da classe que deseja > ')
    
    # Encontrar a classe correspondente
    classe_selecionada = None
    for c in categorias['classe']:
        if c.startswith(x + ' >'):
            classe_selecionada = c
            break
    
    if classe_selecionada:
        print(f'Você selecionou: {classe_selecionada}')
        
        # Atualizar o player com os valores da classe selecionada
        player.update({
            'vida': categorias['vida'],
            'vida_min': categorias['vida_min'],
            'vida_max': categorias['vida_max'],
            'dano': categorias['dano'],
            'dano_base':categorias['dano_base'],
            'golpes': categorias['golpes'],
            'armas': categorias['armas'],
            'mana': categorias['mana'],
            'mana_inicial':categorias['mana_inicial'],
            'mana_max': categorias['mana_max'],
            'cura': categorias['cura'],
            'classe': classe_selecionada
        })
        
        print(f"Player atualizado:")
        Hud_player()
        escolha_arma()
    else:
        print('Classe não encontrada')
        print('')
        escolha_classe()



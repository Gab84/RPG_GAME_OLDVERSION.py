from Player import player



Furtivo = {
    'classe' : ['1 > Bandido', '2 > Gnomo'],

    '1 > Bandido':{
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
        'armas' : ['adaga'],
        'mana' : 50,
        'mana_max' : 100,
        'cura' : 10,
        'inventario' : ["poção cura(1)"],
        
    },

    '2 > Gnomo': {

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
        'armas' : ['adaga'],
        'mana' : 50,
        'mana_max' : 100,
        'cura' : 10,
        'inventario' : ["poção cura(1)"],        

    }
}



categoria = input('Digite o número da categoria que deseja > ')

if categoria == '1':
    categorias = Furtivo
else:
    print("Categoria não encontrada")
    

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
        'vida': categorias[classe_selecionada]['vida'],
        'vida_min': categorias[classe_selecionada]['vida_min'],
        'vida_max': categorias[classe_selecionada]['vida_max'],
        'dano': categorias[classe_selecionada]['dano'],
        'dano_base':categorias[classe_selecionada]['dano_base'],
        'golpes': categorias[classe_selecionada]['golpes'],
        'armas': categorias[classe_selecionada]['armas'],
        'mana': categorias[classe_selecionada]['mana'],
        'mana_max': categorias[classe_selecionada]['mana_max'],
        'cura': categorias[classe_selecionada]['cura'],
        'classe': classe_selecionada
    })
    
    print(f"Player atualizado: {player}")
else:
    print('Classe não encontrada')


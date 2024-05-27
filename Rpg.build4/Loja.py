from Itens import * 
from Textos import Hud_player, desc_itens

l_itens_alexandre = ['pot_cura', 'pot_mana',]
l_itens_bathemofh = ['adaga', 'espada_curta','cajado','varinha','machado']



loja_Alexandre = {
    #nome do npc
    'nome' : 'Alexandre',
    'itens' : l_itens_alexandre,
    'preco' : ['Pot_Cura : 15 Coins ','Pot_mana : 10 Coins ']
}
loja_Bathemofh = {
    #nome do npc
    'nome' : 'Bathemofh',
    'itens' : l_itens_bathemofh,
    'preco' : ['adaga : 10','espada_curta : 15','cajado : 10','varinha : 10','machado : 20',]
}



def loja(npc):
    print(f"Você encontrou a Loja do >> {npc['nome']} << ")
    print(f"O seu inventario atual é >> {player['inventario']}")
    print(f"Seu dinheiro atual > {player['dinheiro']}")
    print('')
    print("VOCÊ SÓ PODE COMPRAR UM ITEM POR ENCONTRO, ESCOLHA COM SABEDORIA. ")
    desc_itens()
    print('')
    x = int(input(f"Os itens da loja são {npc['itens']} deseja comprar qual ? > "))
    if 0 <= x < len(npc['itens']): # Verificando se o índice está dentro do intervalo válido
        item_desejado = npc['itens'][x] # Acessando o item pelo índice fornecido
        if player['dinheiro'] >= consumiveis[item_desejado]['preco'] :
            print("Item Comprado:", item_desejado)
            # Removendo o item da lista
            npc['itens'].pop(x)
            print(f"Item comprado foi removido da loja, a nova loja de itens é essa >> {npc['itens']}")
            #add ao inv player
            player['inventario'].append(item_desejado)
            player['dinheiro'] -= consumiveis[item_desejado]['preco']
            print(f"Item adicionado ao Iventario do player, seu inventario atualizado é >> {player['inventario']}") 
            Hud_player()      
        else:
            print('Voce não tem dinheiro o suficiente para comprar esse item')
            loja(npc)
    else:
        print("Índice fora do intervalo. Tente novamente.")
        loja(npc)

def loja_a(npc):
    print(f"Você encontrou a Loja do >> {npc['nome']} << ")
    print(f"O seu inventario atual é >> {player['armas']}")
    print(f"Seu dinheiro atual > {player['dinheiro']}")
    print('')
    print("VOCÊ SÓ PODE COMPRAR UM ITEM POR ENCONTRO, ESCOLHA COM SABEDORIA. ")
    desc_armas()
    print('')
    x = int(input(f"Os itens da loja são {npc['itens']} deseja comprar qual ? > "))
    if 0 <= x < len(npc['itens']): # Verificando se o índice está dentro do intervalo válido
        item_desejado = npc['itens'][x] # Acessando o item pelo índice fornecido
        if player['dinheiro'] >= armas[item_desejado]['preco'] :
            print("Item Comprado:", item_desejado)
            # Removendo o item da lista
            npc['itens'].pop(x)
            print(f"Item comprado foi removido da loja, a nova loja de itens é essa >> {npc['itens']}")
            #add ao inv player
            if armas[item_desejado]['nome'] == 'adaga':
                equip_adaga()
            elif armas[item_desejado]['nome'] == 'espada_curta':
                equip_espada_curta()
            elif armas[item_desejado]['nome'] == 'cajado':
                equip_cajado()
            elif armas[item_desejado]['nome'] == 'varinha':
                equip_varinha()
            elif armas[item_desejado]['nome'] == 'machado':
                equip_machado()
            print(f"{armas[item_desejado]['nome']} foi adicionado a mão do player")
            player['dinheiro'] -= armas[item_desejado]['preco']
            Hud_player()
        else:
            print('Voce não tem dinheiro o suficiente para comprar esse item')
            loja(npc)
    else:
        print("Índice fora do intervalo. Tente novamente.")
        loja(npc)



##loja_a(npc=loja_Bathemofh)
loja(npc=loja_Alexandre)
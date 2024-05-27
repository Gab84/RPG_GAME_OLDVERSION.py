# Definindo as funções específicas para cada item consumível
def usar_pot_cura():
    print("Usando Poção de Cura. Cura 20 pontos de vida.")

def usar_pot_mana():
    print("Usando Poção de Mana. Recupera 20 pontos de mana.")

# Mapeando os nomes dos itens para as funções correspondentes
funcoes_consumiveis = {
    'pot_cura': usar_pot_cura,
    'pot_mana': usar_pot_mana,
}

# Inicializando a lista de itens
itens = ['pot_cura', 'pot_mana']
novos_itens = ['pot_cura']

# Adicionando novos itens à lista
itens.append(novos_itens[0])

# Solicitando ao usuário que insira o índice do item que deseja acessar
x = int(input('Deseja chamar qual item? (Digite o índice começando de 0) '))

# Verificando se o índice está dentro do intervalo válido
if 0 <= x < len(itens):
    # Acessando o item pelo índice fornecido
    item_desejado = itens[x]
    print("Item acessado:", item_desejado)
    
    # Removendo o item da lista
    itens.pop(x)
    print("Item removido. Lista atualizada:", itens)
    
    # Executando a função correspondente ao item
    if item_desejado in funcoes_consumiveis:
        funcoes_consumiveis[item_desejado]()
    else:
        print("Nenhuma função associada a este item.")
else:
    print("Índice fora do intervalo. Tente novamente.")

from Acoes import *
from Player import player
from time import sleep

def part1():
    print(f"Em uma caverna, {player['nome']}, acorda devido a forte agitação, do som de metal, e risadas direcionadadas a {player['nome']}, ao abrir os olhos, uma voz rouca te chama. ")
    sleep(1)
    print(f"VOZ > Ei, princesa! Acorda, você não está em um spa. Depois que esses malditos entram na merda do Ether virão mesmo uns preguiçosos. por falar nisso, sou Heclito, o Hemosiano. ")
    sleep(1)
    print(f"Vamos, pegue alguns equipamentos. Precisamos de mais gente, mesmo que você não pareça fazer diferença nesse lugar.")
    escolha_classe()
    
    

#escolha parte 2

def A_B01_1():
    print(f"{player['nome']} prossegue seu caminho e mais a frente encontra novamente heclito, ele diz que estão indo para fora das defesas da cidade e que precisa que você venha junto.")
    print(f"{player['nome']} segue Heclito até os portões da cidade e lá eles percebem uma dupla de orcs, Heclito diz para você cuidar de um que ele promete finalizar o outro.")
    combate_orc()

def A_B01():
    sleep(1)
    print(f"Ao tentar prosseguir ver uma escritura na parede que aparentemente foi escrito por uma comunidade distante.")
    x = int(input('Deseaja tentar ler ? \n1)SIM \n2)NAO \n > '))
    if x == 1:
        if player['classe'] == '2 > Mago':
            if player['mana'] == (player['mana_inicial'] +20):
                print('Você já leu.')
                A_B01()
            else:
                print('Você conseguiu ler e adquiriu informações importantes')
                player['mana'] += 20
                A_B01()
        else:
            print('Você se esforça, mas não consegue entender a ligua que aquilo está escrito. ')
            A_B01()
    elif x == 2:
        print('você segue adiante e encontar uma uma cidade absurdamente surreal e um rapaz ao canto te chama para o lado dele.')
        b = int(input('Deseaja se aproximar ? ? \n1)SIM \n2)NAO \n > '))
        if b == 1 :
            print(f"Ele se apresenta, seu nome é Alexandre, ele rapidamente diz: eu tenho oque você vai precisar. se aproxime.")
            loja(npc=loja_Alexandre)
            print('Após visitar a loja.')
            A_B01_1()
        elif b == 2:
            A_B01_1()



def part2():
    print(f"Após a coleta de seus itens, {player['nome']} vê dois caminhos a serem seguidos.")
    print('Uma porta a direita que alguns dos soldados estão indo. Uma porta a esquerda que você percebe um velho bebado indo. ')
    x = int(input('Qual caminho seguir ? \n1)direita \n2)esquerda \n> '))
    if x == 1:
        A_B01()


def p():
    part1()
    part2()

p()
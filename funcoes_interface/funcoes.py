# Primeiro menu de interface do programa

from classes.videos import Videos
from classes.playlist import Playlist

from time import sleep

def linha(tamanho=90):
    print('='*tamanho)


def cabecalho(texto='Extraindo Dados Da Api Do Youtube'):
    linha()
    print(texto.center(90))
    linha()


def menu_inicial():
    cabecalho()
    print('1 - Inserir o id do video ou a playlist que desaja analisar os dados \n'
          '2 - Sair do sistema')
    opcao: int = int(input('Informe sua opção: '))
    menu_secundario(opcao)
    pass


def menu_secundario(opcao):
    cabecalho()
    if opcao == 1:
        url: str = str(input('Inserir o id do video ou a playlist que desaja analisar os dados'))
        if len(url) > 15:
            playlist = Playlist()
        else:
            videos = Videos()
    elif opcao == 2:
        exit()
    else:
        print('Opção inválida')
        sleep(1)
        menu_inicial()


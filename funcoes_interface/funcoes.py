# Primeiro menu de interface do programa

'''from classes.videos import Videos'''
from Classes.Playlist import Playlist
from Classes.Graficos import Graficos

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
        url: str = str(input('Inserir o id do video ou a playlist que deseja analisar os dados: '))
        if len(url) > 15:
            print('1 - Dados\n'
                  '2 - Total de visualições por video\n'
                  '3 - Total de likes por videos\n'
                  '4 - Top 10 videos com mais visualizações\n'
                  '5 - Relação entre visualizações e likes\n'
                  '6 - Comentários relevantes\n'
                  '7 - Visualização preditiva\n'
                  '8 - Sair do programa')
            op: int = int(input("Informe sua opção: "))
            menu_opcao(url=url, opcao=op)
        else:
            """videos = Videos(url)"""
            pass
    elif opcao == 2:
        exit()
    else:
        print('Opção inválida')
        sleep(1)
        menu_inicial()


def menu_opcao(url, opcao):
    if opcao == 1:
        playlist = Playlist(url)
        print(playlist.dataframe())
    elif opcao == 2:
        grafico = Graficos(url)
        grafico.graph_visualizacoes()
        #print(grafico.teste())
    elif opcao == 3:
        grafico = Graficos(url)
        grafico.graph_likes()
    elif opcao == 4:
        grafico = Graficos(url)
        grafico.graph_10()
    elif opcao == 5:
        grafico = Graficos(url)
        grafico.graph_relacao()
    elif opcao == 6:
        pass
    elif opcao == 7:
        pass
    elif opcao == 8:
        print('Saindo do sistema')
        sleep(3)
        exit()
    else:
        print('Opção inválida')
        sleep(2)
        """menu_opcao()"""

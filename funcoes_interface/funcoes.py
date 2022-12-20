# Primeiro menu de interface do programa

'''from classes.videos import Videos'''
from classes.playlist import Playlist
from classes.estatistica import EstatisticaPlaylist
# from classes.dataframe import EstruturaDataFrame

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
                  '4 - Total de comentario por video\n'
                  '5 - Top 10 videos com mais visualizações\n'
                  '6 - Relação entre visualizações e likes\n'
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
        #print(url)

        dados = Playlist(url)
        print(dados.dataframe)

    elif opcao == 2:
        pass
    elif opcao == 3:
        pass
    elif opcao == 4:
        pass
    elif opcao == 5:
        pass
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

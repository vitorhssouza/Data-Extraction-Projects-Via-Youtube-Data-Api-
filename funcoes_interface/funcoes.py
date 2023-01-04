# Primeiro menu de interface do programa

'''from classes.videos import Videos'''
from Classes.Playlist import Playlist
from Classes.Graficos import Graficos
from Classes.Video import Video
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


def menu_secundario(op):
    cabecalho()
    if op == 1:
        url: str = str(input('Inserir o id do video ou a playlist que deseja analisar os dados: '))
        if len(url) > 15:
            while True:
                cabecalho()
                print('1 - Dados\n'
                      '2 - Total de visualições por video\n'
                      '3 - Total de likes por videos\n'
                      '4 - Top 10 videos com mais visualizações\n'
                      '5 - Relação entre visualizações e likes\n'
                      '6 - Visualização preditiva\n'
                      '7 - Sair do programa')
                linha()
                opcao: int = int(input("Informe sua opção: "))
                linha()
                if opcao == 1:
                    playlist = Playlist(url)
                    print(playlist.dataframe())
                elif opcao == 2:
                    grafico = Graficos(url)
                    grafico.graph_visualizacoes()
                    # print(grafico.teste())
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
                    print('Saindo do sistema')
                    sleep(2)
                    exit()
                else:
                    print('Opção inválida')
                    sleep(2)
        else:
            while True:
                cabecalho()
                print('1 - Visualizar gráfico de nuvens de comentarios\n'
                      '2 - Sair do programa')
                linha()
                op: int = int(input('Informe sua opção: '))
                linha()
                if op == 1:
                    video = Video(url)
                    video.graph_nuvem()

                elif op == 2:
                    print('Saindo do sistema')
                    break
    elif op == 2:
        exit()
    else:
        print('Opção inválida')
        sleep(1)
        menu_inicial()